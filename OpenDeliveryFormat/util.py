# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenDeliveryFormat Project.

import os
import six
import json
import shutil
import tempfile

from contextlib import contextmanager


@contextmanager
def cd(dir_, cleanup = lambda: True):
    """
    Context manager for swapping to a directory for a given
    period of time.
    :param dir_: The directory to change to
    :param cleanup: callable that we'll execute upon finishing the command
    :return: None
    """
    previous = os.getcwd()
    os.chdir(os.path.expanduser(dir_))
    try:
        yield
    finally:
        os.chdir(previous)
        cleanup()


@contextmanager
def temp_dir(change_dir=True):
    """
    Quick temp directory that we move into to do our work
    :return: The new temp directory (we've also cd'd into it) 
    """
    dirpath = tempfile.mkdtemp()
    def _clean():
        shutil.rmtree(dirpath)
    if change_dir:
        with cd(dirpath, _clean):
            yield dirpath
    else:
        yield dirpath
