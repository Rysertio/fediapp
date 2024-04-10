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

class History(object):
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
        'day': 'object',
        'uses': 'object',
        'accounts': 'object'
    }

    attribute_map = {
        'day': 'day',
        'uses': 'uses',
        'accounts': 'accounts'
    }

    def __init__(self, day=None, uses=None, accounts=None):  # noqa: E501
        """History - a model defined in Swagger"""  # noqa: E501
        self._day = None
        self._uses = None
        self._accounts = None
        self.discriminator = None
        self.day = day
        self.uses = uses
        self.accounts = accounts

    @property
    def day(self):
        """Gets the day of this History.  # noqa: E501

        UNIX timestamp on midnight of the given day.  # noqa: E501

        :return: The day of this History.  # noqa: E501
        :rtype: object
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this History.

        UNIX timestamp on midnight of the given day.  # noqa: E501

        :param day: The day of this History.  # noqa: E501
        :type: object
        """
        if day is None:
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    @property
    def uses(self):
        """Gets the uses of this History.  # noqa: E501

        The counted usage of the tag within that day. Cast from integer.  # noqa: E501

        :return: The uses of this History.  # noqa: E501
        :rtype: object
        """
        return self._uses

    @uses.setter
    def uses(self, uses):
        """Sets the uses of this History.

        The counted usage of the tag within that day. Cast from integer.  # noqa: E501

        :param uses: The uses of this History.  # noqa: E501
        :type: object
        """
        if uses is None:
            raise ValueError("Invalid value for `uses`, must not be `None`")  # noqa: E501

        self._uses = uses

    @property
    def accounts(self):
        """Gets the accounts of this History.  # noqa: E501

        The total of accounts using the tag within that day. Cast from integer.  # noqa: E501

        :return: The accounts of this History.  # noqa: E501
        :rtype: object
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this History.

        The total of accounts using the tag within that day. Cast from integer.  # noqa: E501

        :param accounts: The accounts of this History.  # noqa: E501
        :type: object
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

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
        if issubclass(History, dict):
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
        if not isinstance(other, History):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
