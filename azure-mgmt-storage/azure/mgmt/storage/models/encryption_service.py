# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EncryptionService(Model):
    """An encrypted service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param enabled: A boolean indicating whether or not the service is
     encrypted.
    :type enabled: bool
    :ivar last_enabled_time: Gets a time value indicating when was the
     encryption enabled by the user last time. We return this value only when
     encryption is enabled. There might be some unencrypted blobs which were
     written after this time. This time is just to give a rough estimate of
     when encryption was enabled.
    :vartype last_enabled_time: datetime
    """ 

    _validation = {
        'last_enabled_time': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'last_enabled_time': {'key': 'lastEnabledTime', 'type': 'iso-8601'},
    }

    def __init__(self, enabled=None):
        self.enabled = enabled
        self.last_enabled_time = None
