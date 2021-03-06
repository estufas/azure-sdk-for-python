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


class RetentionPolicy(Model):
    """Specifies the retention policy for the log.

    :param enabled: a value indicating whether the retention policy is
     enabled.
    :type enabled: bool
    :param days: the number of days for the retention in days. A value of 0
     will retain the events indefinitely.
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'days': {'key': 'days', 'type': 'int'},
    }

    def __init__(self, enabled, days):
        self.enabled = enabled
        self.days = days
