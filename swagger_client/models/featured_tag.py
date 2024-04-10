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

class FeaturedTag(object):
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
        'id': 'object',
        'name': 'object',
        'url': 'object',
        'statuses_count': 'object',
        'last_status_at': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'url': 'url',
        'statuses_count': 'statuses_count',
        'last_status_at': 'last_status_at'
    }

    def __init__(self, id=None, name=None, url=None, statuses_count=None, last_status_at=None):  # noqa: E501
        """FeaturedTag - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._url = None
        self._statuses_count = None
        self._last_status_at = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.url = url
        self.statuses_count = statuses_count
        self.last_status_at = last_status_at

    @property
    def id(self):
        """Gets the id of this FeaturedTag.  # noqa: E501

        The internal ID of the featured tag in the database. Cast from integer but not guaranteed to be a number.  # noqa: E501

        :return: The id of this FeaturedTag.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeaturedTag.

        The internal ID of the featured tag in the database. Cast from integer but not guaranteed to be a number.  # noqa: E501

        :param id: The id of this FeaturedTag.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this FeaturedTag.  # noqa: E501

        The name of the hashtag being featured.  # noqa: E501

        :return: The name of this FeaturedTag.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeaturedTag.

        The name of the hashtag being featured.  # noqa: E501

        :param name: The name of this FeaturedTag.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this FeaturedTag.  # noqa: E501

        A link to all statuses by a user that contain this hashtag.  # noqa: E501

        :return: The url of this FeaturedTag.  # noqa: E501
        :rtype: object
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FeaturedTag.

        A link to all statuses by a user that contain this hashtag.  # noqa: E501

        :param url: The url of this FeaturedTag.  # noqa: E501
        :type: object
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def statuses_count(self):
        """Gets the statuses_count of this FeaturedTag.  # noqa: E501

        The number of authored statuses containing this hashtag.  # noqa: E501

        :return: The statuses_count of this FeaturedTag.  # noqa: E501
        :rtype: object
        """
        return self._statuses_count

    @statuses_count.setter
    def statuses_count(self, statuses_count):
        """Sets the statuses_count of this FeaturedTag.

        The number of authored statuses containing this hashtag.  # noqa: E501

        :param statuses_count: The statuses_count of this FeaturedTag.  # noqa: E501
        :type: object
        """
        if statuses_count is None:
            raise ValueError("Invalid value for `statuses_count`, must not be `None`")  # noqa: E501

        self._statuses_count = statuses_count

    @property
    def last_status_at(self):
        """Gets the last_status_at of this FeaturedTag.  # noqa: E501

        The timestamp of the last authored status containing this hashtag.ISO 8601 Datetime.  # noqa: E501

        :return: The last_status_at of this FeaturedTag.  # noqa: E501
        :rtype: object
        """
        return self._last_status_at

    @last_status_at.setter
    def last_status_at(self, last_status_at):
        """Sets the last_status_at of this FeaturedTag.

        The timestamp of the last authored status containing this hashtag.ISO 8601 Datetime.  # noqa: E501

        :param last_status_at: The last_status_at of this FeaturedTag.  # noqa: E501
        :type: object
        """
        if last_status_at is None:
            raise ValueError("Invalid value for `last_status_at`, must not be `None`")  # noqa: E501

        self._last_status_at = last_status_at

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
        if issubclass(FeaturedTag, dict):
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
        if not isinstance(other, FeaturedTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
