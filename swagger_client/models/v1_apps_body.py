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

class V1AppsBody(object):
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
        'client_name': 'object',
        'redirect_uris': 'object',
        'scopes': 'object',
        'website': 'object'
    }

    attribute_map = {
        'client_name': 'client_name',
        'redirect_uris': 'redirect_uris',
        'scopes': 'scopes',
        'website': 'website'
    }

    def __init__(self, client_name=None, redirect_uris=None, scopes=None, website=None):  # noqa: E501
        """V1AppsBody - a model defined in Swagger"""  # noqa: E501
        self._client_name = None
        self._redirect_uris = None
        self._scopes = None
        self._website = None
        self.discriminator = None
        self.client_name = client_name
        self.redirect_uris = redirect_uris
        if scopes is not None:
            self.scopes = scopes
        if website is not None:
            self.website = website

    @property
    def client_name(self):
        """Gets the client_name of this V1AppsBody.  # noqa: E501


        :return: The client_name of this V1AppsBody.  # noqa: E501
        :rtype: object
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this V1AppsBody.


        :param client_name: The client_name of this V1AppsBody.  # noqa: E501
        :type: object
        """
        if client_name is None:
            raise ValueError("Invalid value for `client_name`, must not be `None`")  # noqa: E501

        self._client_name = client_name

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this V1AppsBody.  # noqa: E501

        Where the user should be redirected after authorization. Called this because it's apparently possible to pass multiple redirect_uris, but is documented nowhere on what syntax you need to use.  # noqa: E501

        :return: The redirect_uris of this V1AppsBody.  # noqa: E501
        :rtype: object
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this V1AppsBody.

        Where the user should be redirected after authorization. Called this because it's apparently possible to pass multiple redirect_uris, but is documented nowhere on what syntax you need to use.  # noqa: E501

        :param redirect_uris: The redirect_uris of this V1AppsBody.  # noqa: E501
        :type: object
        """
        if redirect_uris is None:
            raise ValueError("Invalid value for `redirect_uris`, must not be `None`")  # noqa: E501

        self._redirect_uris = redirect_uris

    @property
    def scopes(self):
        """Gets the scopes of this V1AppsBody.  # noqa: E501

        Space separated list of scopes.  # noqa: E501

        :return: The scopes of this V1AppsBody.  # noqa: E501
        :rtype: object
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this V1AppsBody.

        Space separated list of scopes.  # noqa: E501

        :param scopes: The scopes of this V1AppsBody.  # noqa: E501
        :type: object
        """

        self._scopes = scopes

    @property
    def website(self):
        """Gets the website of this V1AppsBody.  # noqa: E501

        A URL to the homepage of your app.  # noqa: E501

        :return: The website of this V1AppsBody.  # noqa: E501
        :rtype: object
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this V1AppsBody.

        A URL to the homepage of your app.  # noqa: E501

        :param website: The website of this V1AppsBody.  # noqa: E501
        :type: object
        """

        self._website = website

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
        if issubclass(V1AppsBody, dict):
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
        if not isinstance(other, V1AppsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
