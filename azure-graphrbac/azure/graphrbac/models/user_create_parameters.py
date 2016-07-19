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


class UserCreateParameters(Model):
    """Request parameters for create a new work or school account user.

    :param account_enabled: Enable the account. If it is enabled then true
     else false.
    :type account_enabled: bool
    :param display_name: User display name
    :type display_name: str
    :param password_profile: Password Profile
    :type password_profile: :class:`PasswordProfile
     <azure.graphrbac.models.PasswordProfile>`
    :param user_principal_name: The user principal name
     (someuser@contoso.com). It must contain one of the verified domains for
     the tenant.
    :type user_principal_name: str
    :param mail_nickname: The mail alias for the user
    :type mail_nickname: str
    :param immutable_id: Needs to be specified if you are using a federated
     domain for the user's userPrincipalName (UPN) property while creating a
     new user account. It is used to associate an on-premises Active
     Directory user account to their Azure AD user object.
    :type immutable_id: str
    """ 

    _validation = {
        'account_enabled': {'required': True},
        'display_name': {'required': True},
        'password_profile': {'required': True},
        'user_principal_name': {'required': True},
        'mail_nickname': {'required': True},
    }

    _attribute_map = {
        'account_enabled': {'key': 'accountEnabled', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'password_profile': {'key': 'passwordProfile', 'type': 'PasswordProfile'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
        'immutable_id': {'key': 'immutableId', 'type': 'str'},
    }

    def __init__(self, account_enabled, display_name, password_profile, user_principal_name, mail_nickname, immutable_id=None):
        self.account_enabled = account_enabled
        self.display_name = display_name
        self.password_profile = password_profile
        self.user_principal_name = user_principal_name
        self.mail_nickname = mail_nickname
        self.immutable_id = immutable_id
