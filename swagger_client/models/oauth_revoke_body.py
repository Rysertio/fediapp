# coding: utf-8

"""
    Mastodon API

    The API for interacting with Mastodon.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OauthRevokeBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_id': 'object',
        'client_secret': 'object',
        'token': 'object'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'token': 'token'
    }

    def __init__(self, client_id=None, client_secret=None, token=None):  # noqa: E501
        """OauthRevokeBody - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._client_secret = None
        self._token = None
        self.discriminator = None
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token

    @property
    def client_id(self):
        """Gets the client_id of this OauthRevokeBody.  # noqa: E501

        Client ID, obtained during app registration.  # noqa: E501

        :return: The client_id of this OauthRevokeBody.  # noqa: E501
        :rtype: object
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OauthRevokeBody.

        Client ID, obtained during app registration.  # noqa: E501

        :param client_id: The client_id of this OauthRevokeBody.  # noqa: E501
        :type: object
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this OauthRevokeBody.  # noqa: E501

        Client secret, obtained during app registration.  # noqa: E501

        :return: The client_secret of this OauthRevokeBody.  # noqa: E501
        :rtype: object
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this OauthRevokeBody.

        Client secret, obtained during app registration.  # noqa: E501

        :param client_secret: The client_secret of this OauthRevokeBody.  # noqa: E501
        :type: object
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def token(self):
        """Gets the token of this OauthRevokeBody.  # noqa: E501

        The previously obtained token, to be invalidated.  # noqa: E501

        :return: The token of this OauthRevokeBody.  # noqa: E501
        :rtype: object
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this OauthRevokeBody.

        The previously obtained token, to be invalidated.  # noqa: E501

        :param token: The token of this OauthRevokeBody.  # noqa: E501
        :type: object
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OauthRevokeBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OauthRevokeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other