# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenDeliveryFormat Project.

from __future__ import absolute_import

import os
import six
import yaml
import json

from .exceptions import ODFFileError, ODFValidationError


class _DataContainer(object):
    """
    Abstract class with the ability to read/pull from YAML, JSON, and
    potentially other formats with dynamic getters, setters, and
    ability to write out to either the same filepath or others.

    Subclass this to introduce validation and other utilities.
    """
    def __init__(self, data={}, filepath=None):
        self.__d = data
        self._filepath = filepath

    # -- Magic

    def __getitem__(self, key):
        return self.__d[key]


    def __setitem__(self, key, value):
        # -- We validate that all data is JSON compliant
        try:
            json.dumps(value)
        except Exception as err:
            raise ODFValidationError(
                'Invalid value: {} - must be JSON compliant!'
                .format(value)
            )
        self.__d[str(key)] = value

    # -- Properties

    @property
    def filepath(self):
        """ :return: ``str`` Path that's set for this container """
        return self._filepath


    @filepath.setter
    def filepath(self, path):
        """ Set the filepath for this container """
        if not isinstance(path, six.string_types):
            raise TypeError('Filepath must be a string! Got: {}'
                            .format(type(path)))
        self._filepath = path


    @property
    def extension(self):
        """ :return: Extension (no leading '.') or None if not filepath set """
        if not self.filepath:
            return None
        return os.path.splitext(self.filepath)[-1][1:]


    # -- Public Methods

    def save(self, make_dirs=True):
        """
        Save this container to disk. Filepath must be set before
        calling this.
        :param make_dirs: Create any required parent directories before saving
        :return: None
        """
        if not self.filepath:
            raise ODFFileError('Must set a filepath before saving!')

        # -- Find out what data format we should be storing this information in
        if self.extension in ('odf', 'spec', 'yaml'):
            writter = yaml
        elif self.extension in ('jodf', 'jspec', 'json'):
            writter = json
        else:
            raise ODFFileError('Unsupported file extension: {}'
                               .format(self.extension))

        if make_dirs:
            dir_ = os.path.dirname(self.filepath)
            if dir_ and not os.path.isdir(dir_):
                os.makedirs(os.path.dirname(self.filepath))

        with open(self.filepath, 'w') as file:
            if writter is yaml:
                yaml.dump(self.__d, file, default_flow_style=False)
            elif writter is json:
                json.jump(self.__d, file, indent=4)


    # -- Classmethods

    @classmethod
    def _validate_data(cls, data):
        """
        Protected classmethod

        Overload per-class if required. This is called on initialization
        to verify that the data is in fact valid for whatever type of
        work that might be done with it.

        Raise an exception (preferably an exceptions.ODFValidationError)
        if something isn't quite right. By default this does nothing.

        :param data: Information pulled from a file. This _should_ be a ``dict``
            but that's not guaranteed
        :return: None
        """
        pass


    @classmethod
    def from_file(cls, filepath):
        """
        Based on the file extension, try to read a file in various
        ways.

        :param filepath: ``str`` Filepath to read from
        :return: Instance of this class
        """
        if not os.path.isfile(filepath):
            raise ODFFileError(
                'The file "{}" cannot be found'.format(filepath)
            )

        extension = os.path.splitext(filepath)[-1][1:]

        if extension in ('odf', 'spec', 'yaml'):
            return cls.from_yaml(filepath)
        elif extension in ('jodf', 'jspec', 'json'):
            return cls.from_json(filepath)
        else:
            raise ODFFileError(
                'Unknown file format. Cannot read from "{}"'
                .format(filepath)
            )


    @classmethod
    def from_yaml(cls, filepath):
        """
        Attempt to open the file via the YAML format

        :param filepath: ``str`` Filepath to read from
        :return: Instance of this class
        """
        try:
            with open(filepath) as f:
                data = yaml.safe_load(f.read())
        except Exception as err:
            raise ODFFileError('ODF Could not read: {}. Reason: {}'
                               .format(filepath, str(err)))

        cls._validate_data(data)
        return cls(data, filepath)



    @classmethod
    def from_json(cls, filepath):
        """
        Attempt to open the file via the JSON format

        :param filepath: ``str`` Filepath to read from
        :return: Instance of this class
        """
        try:
            with open(filepath) as f:
                data = json.load(f)
        except Exception as err:
            raise ODFFileError('ODF Could not read: {}. Reason: {}'
                               .format(filepath, str(err)))

        cls._validate_data(data)
        return cls(data, filepath)
