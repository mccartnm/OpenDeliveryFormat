# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenDeliveryFormat Project.

import os
import unittest

from OpenDeliveryFormat.abstract import _DataContainer
from OpenDeliveryFormat.exceptions import ODFValidationError
from OpenDeliveryFormat.util import temp_dir

static_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'test_files'
)

class TestAbstractTools(unittest.TestCase):
    """
    Test various utilities and the abstract data container
    """
    def test_read_to_data_container(self):
        """
        Basic test - validate we can read from a file and introspect
        it's contents
        """
        fpath = '{}/{}'.format(static_path, 'test_manifest.odf')
        container  = _DataContainer.from_file(fpath)

        # __getitem__
        self.assertEqual(container['meta']['odf_version'], "1.0.0")
        self.assertTrue(isinstance(container['items'], list))

        # __setitem__
        container['foo'] = 'bar'
        self.assertEqual(container['foo'], 'bar')

        # .filepath
        self.assertEqual(container.filepath, fpath)

        def _t():
            container.filepath = 123
        self.assertRaises(TypeError, _t)


    def test_write_to_data_container(self):
        """
        Verify we can do some basic file writing and then reload
        it. Also assert JSON compliance
        """
        with temp_dir() as tdir:
            container = _DataContainer()

            container['test_key'] = 'test_value'
            container['test_key_2'] = [
                'A sequence of values',
                32412
            ]

            def _t():
                class OBJ(object):
                    pass
                container['an_object'] = OBJ()
            self.assertRaises(ODFValidationError, _t)

            container.filepath = 'test.odf'
            container.save()

            loadit = _DataContainer.from_file(container.filepath)
            self.assertEqual(loadit['test_key'], 'test_value')
