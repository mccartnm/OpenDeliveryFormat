# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenDeliveryFormat Project.
from __future__ import absolute_import

from .abstract import _DataContainer


class Container(_DataContainer):
    """
    Container represents a single collection of work to be done.

    This is typically boiled into a Shot, Asset, or something that will
    contain tasks within it.
    """
    def __init__(self, data, filepath=None):
        super(Container, self).__init__(data, filepath)


    @property
    def name(self):
        return self['name']


    @property
    def group(self):
        return self['group']


    @property
    def type(self):
        return self['type']

    # @classmethod
    # def _validate(cls, data):
    #     """
    #     Validate a container
    #     """
    #     validator = cls.get_schema('manifest_container')

