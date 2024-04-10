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

class ResultsV2(object):
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
        'accounts': 'object',
        'statuses': 'object',
        'hashtags': 'object'
    }

    attribute_map = {
        'accounts': 'accounts',
        'statuses': 'statuses',
        'hashtags': 'hashtags'
    }

    def __init__(self, accounts=None, statuses=None, hashtags=None):  # noqa: E501
        """ResultsV2 - a model defined in Swagger"""  # noqa: E501
        self._accounts = None
        self._statuses = None
        self._hashtags = None
        self.discriminator = None
        self.accounts = accounts
        self.statuses = statuses
        self.hashtags = hashtags

    @property
    def accounts(self):
        """Gets the accounts of this ResultsV2.  # noqa: E501

        Accounts which match the given query.  # noqa: E501

        :return: The accounts of this ResultsV2.  # noqa: E501
        :rtype: object
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this ResultsV2.

        Accounts which match the given query.  # noqa: E501

        :param accounts: The accounts of this ResultsV2.  # noqa: E501
        :type: object
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def statuses(self):
        """Gets the statuses of this ResultsV2.  # noqa: E501

        Statuses which match the given query.  # noqa: E501

        :return: The statuses of this ResultsV2.  # noqa: E501
        :rtype: object
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this ResultsV2.

        Statuses which match the given query.  # noqa: E501

        :param statuses: The statuses of this ResultsV2.  # noqa: E501
        :type: object
        """
        if statuses is None:
            raise ValueError("Invalid value for `statuses`, must not be `None`")  # noqa: E501

        self._statuses = statuses

    @property
    def hashtags(self):
        """Gets the hashtags of this ResultsV2.  # noqa: E501

        Hashtags which match the given query.  # noqa: E501

        :return: The hashtags of this ResultsV2.  # noqa: E501
        :rtype: object
        """
        return self._hashtags

    @hashtags.setter
    def hashtags(self, hashtags):
        """Sets the hashtags of this ResultsV2.

        Hashtags which match the given query.  # noqa: E501

        :param hashtags: The hashtags of this ResultsV2.  # noqa: E501
        :type: object
        """
        if hashtags is None:
            raise ValueError("Invalid value for `hashtags`, must not be `None`")  # noqa: E501

        self._hashtags = hashtags

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
        if issubclass(ResultsV2, dict):
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
        if not isinstance(other, ResultsV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other