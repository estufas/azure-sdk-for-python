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


class Sku(Model):
    """The SKU of the storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Gets or sets the sku name. Required for account creation,
     optional for update. Note that in older versions, sku name was called
     accountType. Possible values include: 'Standard_LRS', 'Standard_GRS',
     'Standard_RAGRS', 'Standard_ZRS', 'Premium_LRS'
    :type name: str or :class:`SkuName <azure.mgmt.storage.models.SkuName>`
    :ivar tier: Gets the sku tier. This is based on the SKU name. Possible
     values include: 'Standard', 'Premium'
    :vartype tier: str or :class:`SkuTier <azure.mgmt.storage.models.SkuTier>`
    """ 

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'SkuName'},
        'tier': {'key': 'tier', 'type': 'SkuTier'},
    }

    def __init__(self, name):
        self.name = name
        self.tier = None
