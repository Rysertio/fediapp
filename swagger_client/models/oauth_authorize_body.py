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

class OauthAuthorizeBody(object):
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
        'response_type': 'object',
        'client_id': 'object',
        'redirect_uri': 'object',
        'scope': 'object',
        'force_login': 'object'
    }

    attribute_map = {
        'response_type': 'response_type',
        'client_id': 'client_id',
        'redirect_uri': 'redirect_uri',
        'scope': 'scope',
        'force_login': 'force_login'
    }

    def __init__(self, response_type=None, client_id=None, redirect_uri=None, scope=None, force_login=None):  # noqa: E501
        """OauthAuthorizeBody - a model defined in Swagger"""  # noqa: E501
        self._response_type = None
        self._client_id = None
        self._redirect_uri = None
        self._scope = None
        self._force_login = None
        self.discriminator = None
        self.response_type = response_type
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        if scope is not None:
            self.scope = scope
        if force_login is not None:
            self.force_login = force_login

    @property
    def response_type(self):
        """Gets the response_type of this OauthAuthorizeBody.  # noqa: E501

        Should be equal to `code`.  # noqa: E501

        :return: The response_type of this OauthAuthorizeBody.  # noqa: E501
        :rtype: object
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this OauthAuthorizeBody.

        Should be equal to `code`.  # noqa: E501

        :param response_type: The response_type of this OauthAuthorizeBody.  # noqa: E501
        :type: object
        """
        if response_type is None:
            raise ValueError("Invalid value for `response_type`, must not be `None`")  # noqa: E501

        self._response_type = response_type

    @property
    def client_id(self):
        """Gets the client_id of this OauthAuthorizeBody.  # noqa: E501

        Client ID, obtained during app registration.  # noqa: E501

        :return: The client_id of this OauthAuthorizeBody.  # noqa: E501
        :rtype: object
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OauthAuthorizeBody.

        Client ID, obtained during app registration.  # noqa: E501

        :param client_id: The client_id of this OauthAuthorizeBody.  # noqa: E501
        :type: object
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this OauthAuthorizeBody.  # noqa: E501

        Set a URI to redirect the user to. If this parameter is set to `urn:ietf:wg:oauth:2.0:oob` then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration.  # noqa: E501

        :return: The redirect_uri of this OauthAuthorizeBody.  # noqa: E501
        :rtype: object
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this OauthAuthorizeBody.

        Set a URI to redirect the user to. If this parameter is set to `urn:ietf:wg:oauth:2.0:oob` then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration.  # noqa: E501

        :param redirect_uri: The redirect_uri of this OauthAuthorizeBody.  # noqa: E501
        :type: object
        """
        if redirect_uri is None:
            raise ValueError("Invalid value for `redirect_uri`, must not be `None`")  # noqa: E501

        self._redirect_uri = redirect_uri

    @property
    def scope(self):
        """Gets the scope of this OauthAuthorizeBody.  # noqa: E501

        List of requested OAuth scopes, separated by spaces. Must be a subset of scopes declared during app registration. If not provided, defaults to `read`.  # noqa: E501

        :return: The scope of this OauthAuthorizeBody.  # noqa: E501
        :rtype: object
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OauthAuthorizeBody.

        List of requested OAuth scopes, separated by spaces. Must be a subset of scopes declared during app registration. If not provided, defaults to `read`.  # noqa: E501

        :param scope: The scope of this OauthAuthorizeBody.  # noqa: E501
        :type: object
        """

        self._scope = scope

    @property
    def force_login(self):
        """Gets the force_login of this OauthAuthorizeBody.  # noqa: E501

        Added in `2.6.0`. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance.  # noqa: E501

        :return: The force_login of this OauthAuthorizeBody.  # noqa: E501
        :rtype: object
        """
        return self._force_login

    @force_login.setter
    def force_login(self, force_login):
        """Sets the force_login of this OauthAuthorizeBody.

        Added in `2.6.0`. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance.  # noqa: E501

        :param force_login: The force_login of this OauthAuthorizeBody.  # noqa: E501
        :type: object
        """

        self._force_login = force_login

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
        if issubclass(OauthAuthorizeBody, dict):
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
        if not isinstance(other, OauthAuthorizeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
