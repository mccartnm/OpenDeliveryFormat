# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenDeliveryFormat Project.

import os
import unittest

from OpenDeliveryFormat.manifest import Manifest
from OpenDeliveryFormat.exceptions import ODFValidationError
from OpenDeliveryFormat.util import temp_dir

static_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'test_files'
)

class TestManifest(unittest.TestCase):

    def test_manifest_schema(self):
        """
        ...
        """
        manifest = Manifest.from_file(os.path.join(
            static_path, 'test_manifest.odf'
        ))

        print ([c.name for c in manifest.containers()])
