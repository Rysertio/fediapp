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

class Emoji(object):
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
        'shortcode': 'object',
        'url': 'object',
        'static_url': 'object',
        'visible_in_picker': 'object',
        'category': 'object'
    }

    attribute_map = {
        'shortcode': 'shortcode',
        'url': 'url',
        'static_url': 'static_url',
        'visible_in_picker': 'visible_in_picker',
        'category': 'category'
    }

    def __init__(self, shortcode=None, url=None, static_url=None, visible_in_picker=None, category=None):  # noqa: E501
        """Emoji - a model defined in Swagger"""  # noqa: E501
        self._shortcode = None
        self._url = None
        self._static_url = None
        self._visible_in_picker = None
        self._category = None
        self.discriminator = None
        self.shortcode = shortcode
        self.url = url
        self.static_url = static_url
        self.visible_in_picker = visible_in_picker
        if category is not None:
            self.category = category

    @property
    def shortcode(self):
        """Gets the shortcode of this Emoji.  # noqa: E501

        The name of the custom emoji.  # noqa: E501

        :return: The shortcode of this Emoji.  # noqa: E501
        :rtype: object
        """
        return self._shortcode

    @shortcode.setter
    def shortcode(self, shortcode):
        """Sets the shortcode of this Emoji.

        The name of the custom emoji.  # noqa: E501

        :param shortcode: The shortcode of this Emoji.  # noqa: E501
        :type: object
        """
        if shortcode is None:
            raise ValueError("Invalid value for `shortcode`, must not be `None`")  # noqa: E501

        self._shortcode = shortcode

    @property
    def url(self):
        """Gets the url of this Emoji.  # noqa: E501

        A link to the custom emoji.  # noqa: E501

        :return: The url of this Emoji.  # noqa: E501
        :rtype: object
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Emoji.

        A link to the custom emoji.  # noqa: E501

        :param url: The url of this Emoji.  # noqa: E501
        :type: object
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def static_url(self):
        """Gets the static_url of this Emoji.  # noqa: E501

        A link to a static copy of the custom emoji.  # noqa: E501

        :return: The static_url of this Emoji.  # noqa: E501
        :rtype: object
        """
        return self._static_url

    @static_url.setter
    def static_url(self, static_url):
        """Sets the static_url of this Emoji.

        A link to a static copy of the custom emoji.  # noqa: E501

        :param static_url: The static_url of this Emoji.  # noqa: E501
        :type: object
        """
        if static_url is None:
            raise ValueError("Invalid value for `static_url`, must not be `None`")  # noqa: E501

        self._static_url = static_url

    @property
    def visible_in_picker(self):
        """Gets the visible_in_picker of this Emoji.  # noqa: E501

        Whether this Emoji should be visible in the picker or unlisted.  # noqa: E501

        :return: The visible_in_picker of this Emoji.  # noqa: E501
        :rtype: object
        """
        return self._visible_in_picker

    @visible_in_picker.setter
    def visible_in_picker(self, visible_in_picker):
        """Sets the visible_in_picker of this Emoji.

        Whether this Emoji should be visible in the picker or unlisted.  # noqa: E501

        :param visible_in_picker: The visible_in_picker of this Emoji.  # noqa: E501
        :type: object
        """
        if visible_in_picker is None:
            raise ValueError("Invalid value for `visible_in_picker`, must not be `None`")  # noqa: E501

        self._visible_in_picker = visible_in_picker

    @property
    def category(self):
        """Gets the category of this Emoji.  # noqa: E501

        Used for sorting custom emoji in the picker.  # noqa: E501

        :return: The category of this Emoji.  # noqa: E501
        :rtype: object
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Emoji.

        Used for sorting custom emoji in the picker.  # noqa: E501

        :param category: The category of this Emoji.  # noqa: E501
        :type: object
        """

        self._category = category

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
        if issubclass(Emoji, dict):
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
        if not isinstance(other, Emoji):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
