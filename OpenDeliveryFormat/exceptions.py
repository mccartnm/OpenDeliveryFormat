# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenDeliveryFormat Project.


class ODFFileError(IOError):
    """
    Exception relating to File reading errors within ODF
    """
    pass


class ODFValidationError(Exception):
    """
    Exception relating to invalid information
    """
    pass
