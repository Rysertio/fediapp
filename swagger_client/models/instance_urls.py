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

class InstanceUrls(object):
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
        'streaming_api': 'object'
    }

    attribute_map = {
        'streaming_api': 'streaming_api'
    }

    def __init__(self, streaming_api=None):  # noqa: E501
        """InstanceUrls - a model defined in Swagger"""  # noqa: E501
        self._streaming_api = None
        self.discriminator = None
        self.streaming_api = streaming_api

    @property
    def streaming_api(self):
        """Gets the streaming_api of this InstanceUrls.  # noqa: E501

        Websockets address for push streaming.  # noqa: E501

        :return: The streaming_api of this InstanceUrls.  # noqa: E501
        :rtype: object
        """
        return self._streaming_api

    @streaming_api.setter
    def streaming_api(self, streaming_api):
        """Sets the streaming_api of this InstanceUrls.

        Websockets address for push streaming.  # noqa: E501

        :param streaming_api: The streaming_api of this InstanceUrls.  # noqa: E501
        :type: object
        """
        if streaming_api is None:
            raise ValueError("Invalid value for `streaming_api`, must not be `None`")  # noqa: E501

        self._streaming_api = streaming_api

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
        if issubclass(InstanceUrls, dict):
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
        if not isinstance(other, InstanceUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other