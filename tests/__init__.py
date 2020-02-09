from __future__ import absolute_import

import os
import sys
import time
import unittest

_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_root_path)

def run_tests(scan, pattern):
    """
    Simple test runner

    :param scan: The root directory to scan
    :param pattern: The fnmatch pattern to use when searching for tests
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.discover(
        scan,
        pattern=pattern
    ))
    res = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()


if __name__ == '__main__':
    run_tests(_root_path + '/tests', 'test_*')
