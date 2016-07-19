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


class ImageReference(Model):
    """The image reference.

    :param publisher: the image publisher.
    :type publisher: str
    :param offer: the image offer.
    :type offer: str
    :param sku: the image sku.
    :type sku: str
    :param version: the image version. The allowed formats are
     Major.Minor.Build or 'latest'. Major, Minor and Build being decimal
     numbers. Specify 'latest' to use the latest version of image.
    :type version: str
    """ 

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, publisher=None, offer=None, sku=None, version=None):
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version
