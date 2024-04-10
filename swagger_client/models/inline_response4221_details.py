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

class InlineResponse4221Details(object):
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
        'email': 'object',
        'password': 'object',
        'username': 'object',
        'agreement': 'object'
    }

    attribute_map = {
        'email': 'email',
        'password': 'password',
        'username': 'username',
        'agreement': 'agreement'
    }

    def __init__(self, email=None, password=None, username=None, agreement=None):  # noqa: E501
        """InlineResponse4221Details - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._password = None
        self._username = None
        self._agreement = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if username is not None:
            self.username = username
        if agreement is not None:
            self.agreement = agreement

    @property
    def email(self):
        """Gets the email of this InlineResponse4221Details.  # noqa: E501


        :return: The email of this InlineResponse4221Details.  # noqa: E501
        :rtype: object
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse4221Details.


        :param email: The email of this InlineResponse4221Details.  # noqa: E501
        :type: object
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this InlineResponse4221Details.  # noqa: E501


        :return: The password of this InlineResponse4221Details.  # noqa: E501
        :rtype: object
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineResponse4221Details.


        :param password: The password of this InlineResponse4221Details.  # noqa: E501
        :type: object
        """

        self._password = password

    @property
    def username(self):
        """Gets the username of this InlineResponse4221Details.  # noqa: E501


        :return: The username of this InlineResponse4221Details.  # noqa: E501
        :rtype: object
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InlineResponse4221Details.


        :param username: The username of this InlineResponse4221Details.  # noqa: E501
        :type: object
        """

        self._username = username

    @property
    def agreement(self):
        """Gets the agreement of this InlineResponse4221Details.  # noqa: E501


        :return: The agreement of this InlineResponse4221Details.  # noqa: E501
        :rtype: object
        """
        return self._agreement

    @agreement.setter
    def agreement(self, agreement):
        """Sets the agreement of this InlineResponse4221Details.


        :param agreement: The agreement of this InlineResponse4221Details.  # noqa: E501
        :type: object
        """

        self._agreement = agreement

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
        if issubclass(InlineResponse4221Details, dict):
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
        if not isinstance(other, InlineResponse4221Details):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other