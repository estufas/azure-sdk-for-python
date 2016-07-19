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


class AddStorageAccountParameters(Model):
    """Additional Azure Storage account parameters.

    :param properties: the properties for the Azure Storage account being
     added.
    :type properties: :class:`StorageAccountProperties
     <azure.mgmt.datalake.analytics.account.models.StorageAccountProperties>`
    """ 

    _validation = {
        'properties': {'required': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'StorageAccountProperties'},
    }

    def __init__(self, properties):
        self.properties = properties
