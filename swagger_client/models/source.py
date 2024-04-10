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

class Source(object):
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
        'note': 'object',
        'fields': 'object',
        'privacy': 'object',
        'sensitive': 'object',
        'language': 'object',
        'follower_requests_count': 'object'
    }

    attribute_map = {
        'note': 'note',
        'fields': 'fields',
        'privacy': 'privacy',
        'sensitive': 'sensitive',
        'language': 'language',
        'follower_requests_count': 'follower_requests_count'
    }

    def __init__(self, note=None, fields=None, privacy=None, sensitive=None, language=None, follower_requests_count=None):  # noqa: E501
        """Source - a model defined in Swagger"""  # noqa: E501
        self._note = None
        self._fields = None
        self._privacy = None
        self._sensitive = None
        self._language = None
        self._follower_requests_count = None
        self.discriminator = None
        self.note = note
        self.fields = fields
        if privacy is not None:
            self.privacy = privacy
        if sensitive is not None:
            self.sensitive = sensitive
        if language is not None:
            self.language = language
        if follower_requests_count is not None:
            self.follower_requests_count = follower_requests_count

    @property
    def note(self):
        """Gets the note of this Source.  # noqa: E501

        Profile bio.  # noqa: E501

        :return: The note of this Source.  # noqa: E501
        :rtype: object
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Source.

        Profile bio.  # noqa: E501

        :param note: The note of this Source.  # noqa: E501
        :type: object
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def fields(self):
        """Gets the fields of this Source.  # noqa: E501

        Metadata about the account.  # noqa: E501

        :return: The fields of this Source.  # noqa: E501
        :rtype: object
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Source.

        Metadata about the account.  # noqa: E501

        :param fields: The fields of this Source.  # noqa: E501
        :type: object
        """
        if fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def privacy(self):
        """Gets the privacy of this Source.  # noqa: E501

        The default post privacy to be used for new statuses. `public` = Public post, `unlisted` = unlisted post, `private` = followers-only post, and `direct` = direct post.  # noqa: E501

        :return: The privacy of this Source.  # noqa: E501
        :rtype: object
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this Source.

        The default post privacy to be used for new statuses. `public` = Public post, `unlisted` = unlisted post, `private` = followers-only post, and `direct` = direct post.  # noqa: E501

        :param privacy: The privacy of this Source.  # noqa: E501
        :type: object
        """

        self._privacy = privacy

    @property
    def sensitive(self):
        """Gets the sensitive of this Source.  # noqa: E501

        Whether new statuses should be marked sensitive by default.  # noqa: E501

        :return: The sensitive of this Source.  # noqa: E501
        :rtype: object
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this Source.

        Whether new statuses should be marked sensitive by default.  # noqa: E501

        :param sensitive: The sensitive of this Source.  # noqa: E501
        :type: object
        """

        self._sensitive = sensitive

    @property
    def language(self):
        """Gets the language of this Source.  # noqa: E501

        The default posting langauge for new statuses (ISO 639-1 language two-letter code).  # noqa: E501

        :return: The language of this Source.  # noqa: E501
        :rtype: object
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Source.

        The default posting langauge for new statuses (ISO 639-1 language two-letter code).  # noqa: E501

        :param language: The language of this Source.  # noqa: E501
        :type: object
        """

        self._language = language

    @property
    def follower_requests_count(self):
        """Gets the follower_requests_count of this Source.  # noqa: E501

        The number of pending follow requests.  # noqa: E501

        :return: The follower_requests_count of this Source.  # noqa: E501
        :rtype: object
        """
        return self._follower_requests_count

    @follower_requests_count.setter
    def follower_requests_count(self, follower_requests_count):
        """Sets the follower_requests_count of this Source.

        The number of pending follow requests.  # noqa: E501

        :param follower_requests_count: The follower_requests_count of this Source.  # noqa: E501
        :type: object
        """

        self._follower_requests_count = follower_requests_count

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
        if issubclass(Source, dict):
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
        if not isinstance(other, Source):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
