# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenDeliveryFormat Project.
from __future__ import absolute_import

from jsonschema import validate

from .abstract import _DataContainer
from .exceptions import ODFValidationError
from .container import Container


class Manifest(_DataContainer):
    """
    The manifest represents the culmination of the items and their
    components to be processed.
    """
    def __init__(self, data, filepath=None):
        super(Manifest, self).__init__(data, filepath)

    # -- Validation

    @classmethod
    def _validate_data(cls, data):
        """
        Make sure this is a valid manifest.
        """
        validator = cls.get_schema('manifest')

        try:
            validator.validate(data)
        except Exception as err:
            raise ODFValidationError('Invalid Manifest! Reason: {}'
                                     .format(str(err)))

    # -- Public Interface

    def containers(self):
        """
        Iterate through the Containers in this manifest
        """
        for container_descriptor in self['containers']:
            yield Container(container_descriptor)
