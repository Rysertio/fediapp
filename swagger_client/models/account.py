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

class Account(object):
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
        'username': 'object',
        'acct': 'object',
        'url': 'object',
        'moved': 'Account',
        'fields': 'Field',
        'bot': 'object',
        'suspended': 'object',
        'mute_expires_at': 'object',
        'created_at': 'object',
        'last_status_at': 'object',
        'statuses_count': 'object',
        'followers_count': 'object',
        'following_count': 'object',
        'display_name': 'object',
        'note': 'object',
        'avatar': 'object',
        'avatar_static': 'object',
        'header': 'object',
        'header_static': 'object',
        'locked': 'object',
        'emojis': 'object',
        'discoverable': 'object'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'acct': 'acct',
        'url': 'url',
        'moved': 'moved',
        'fields': 'fields',
        'bot': 'bot',
        'suspended': 'suspended',
        'mute_expires_at': 'mute_expires_at',
        'created_at': 'created_at',
        'last_status_at': 'last_status_at',
        'statuses_count': 'statuses_count',
        'followers_count': 'followers_count',
        'following_count': 'following_count',
        'display_name': 'display_name',
        'note': 'note',
        'avatar': 'avatar',
        'avatar_static': 'avatar_static',
        'header': 'header',
        'header_static': 'header_static',
        'locked': 'locked',
        'emojis': 'emojis',
        'discoverable': 'discoverable'
    }

    def __init__(self, id=None, username=None, acct=None, url=None, moved=None, fields=None, bot=None, suspended=None, mute_expires_at=None, created_at=None, last_status_at=None, statuses_count=None, followers_count=None, following_count=None, display_name=None, note=None, avatar=None, avatar_static=None, header=None, header_static=None, locked=None, emojis=None, discoverable=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._acct = None
        self._url = None
        self._moved = None
        self._fields = None
        self._bot = None
        self._suspended = None
        self._mute_expires_at = None
        self._created_at = None
        self._last_status_at = None
        self._statuses_count = None
        self._followers_count = None
        self._following_count = None
        self._display_name = None
        self._note = None
        self._avatar = None
        self._avatar_static = None
        self._header = None
        self._header_static = None
        self._locked = None
        self._emojis = None
        self._discoverable = None
        self.discriminator = None
        self.id = id
        self.username = username
        self.acct = acct
        self.url = url
        if moved is not None:
            self.moved = moved
        if fields is not None:
            self.fields = fields
        if bot is not None:
            self.bot = bot
        if suspended is not None:
            self.suspended = suspended
        if mute_expires_at is not None:
            self.mute_expires_at = mute_expires_at
        self.created_at = created_at
        if last_status_at is not None:
            self.last_status_at = last_status_at
        self.statuses_count = statuses_count
        self.followers_count = followers_count
        self.following_count = following_count
        self.display_name = display_name
        self.note = note
        self.avatar = avatar
        self.avatar_static = avatar_static
        self.header = header
        self.header_static = header_static
        self.locked = locked
        self.emojis = emojis
        self.discoverable = discoverable

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501

        The account id `header`. Cast from an integer but not guaranteed to be a number.  # noqa: E501

        :return: The id of this Account.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

        The account id `header`. Cast from an integer but not guaranteed to be a number.  # noqa: E501

        :param id: The id of this Account.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this Account.  # noqa: E501

        The username of the account, **not including the domain**.  # noqa: E501

        :return: The username of this Account.  # noqa: E501
        :rtype: object
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Account.

        The username of the account, **not including the domain**.  # noqa: E501

        :param username: The username of this Account.  # noqa: E501
        :type: object
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def acct(self):
        """Gets the acct of this Account.  # noqa: E501

        The webfinger account URI. Equal to `username` for local users, or `username@domain` for remote users.  # noqa: E501

        :return: The acct of this Account.  # noqa: E501
        :rtype: object
        """
        return self._acct

    @acct.setter
    def acct(self, acct):
        """Sets the acct of this Account.

        The webfinger account URI. Equal to `username` for local users, or `username@domain` for remote users.  # noqa: E501

        :param acct: The acct of this Account.  # noqa: E501
        :type: object
        """
        if acct is None:
            raise ValueError("Invalid value for `acct`, must not be `None`")  # noqa: E501

        self._acct = acct

    @property
    def url(self):
        """Gets the url of this Account.  # noqa: E501

        The location of the user's profile page (HTTPS URI).  # noqa: E501

        :return: The url of this Account.  # noqa: E501
        :rtype: object
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Account.

        The location of the user's profile page (HTTPS URI).  # noqa: E501

        :param url: The url of this Account.  # noqa: E501
        :type: object
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def moved(self):
        """Gets the moved of this Account.  # noqa: E501


        :return: The moved of this Account.  # noqa: E501
        :rtype: Account
        """
        return self._moved

    @moved.setter
    def moved(self, moved):
        """Sets the moved of this Account.


        :param moved: The moved of this Account.  # noqa: E501
        :type: Account
        """

        self._moved = moved

    @property
    def fields(self):
        """Gets the fields of this Account.  # noqa: E501


        :return: The fields of this Account.  # noqa: E501
        :rtype: Field
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Account.


        :param fields: The fields of this Account.  # noqa: E501
        :type: Field
        """

        self._fields = fields

    @property
    def bot(self):
        """Gets the bot of this Account.  # noqa: E501

        A presentational flag. Indicates that the account may perform automated actions, may not be monitored, or identifies as a robot.  # noqa: E501

        :return: The bot of this Account.  # noqa: E501
        :rtype: object
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this Account.

        A presentational flag. Indicates that the account may perform automated actions, may not be monitored, or identifies as a robot.  # noqa: E501

        :param bot: The bot of this Account.  # noqa: E501
        :type: object
        """

        self._bot = bot

    @property
    def suspended(self):
        """Gets the suspended of this Account.  # noqa: E501

        An extra entity returned when an account is suspended.  # noqa: E501

        :return: The suspended of this Account.  # noqa: E501
        :rtype: object
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this Account.

        An extra entity returned when an account is suspended.  # noqa: E501

        :param suspended: The suspended of this Account.  # noqa: E501
        :type: object
        """

        self._suspended = suspended

    @property
    def mute_expires_at(self):
        """Gets the mute_expires_at of this Account.  # noqa: E501

        When a timed mute will expire, if applicable (ISO 8601 Datetime).  # noqa: E501

        :return: The mute_expires_at of this Account.  # noqa: E501
        :rtype: object
        """
        return self._mute_expires_at

    @mute_expires_at.setter
    def mute_expires_at(self, mute_expires_at):
        """Sets the mute_expires_at of this Account.

        When a timed mute will expire, if applicable (ISO 8601 Datetime).  # noqa: E501

        :param mute_expires_at: The mute_expires_at of this Account.  # noqa: E501
        :type: object
        """

        self._mute_expires_at = mute_expires_at

    @property
    def created_at(self):
        """Gets the created_at of this Account.  # noqa: E501

        When the account was created (ISO 8601 Datetime).  # noqa: E501

        :return: The created_at of this Account.  # noqa: E501
        :rtype: object
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Account.

        When the account was created (ISO 8601 Datetime).  # noqa: E501

        :param created_at: The created_at of this Account.  # noqa: E501
        :type: object
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def last_status_at(self):
        """Gets the last_status_at of this Account.  # noqa: E501

        When the most recent status was posted (ISO 8601 Datetime).  # noqa: E501

        :return: The last_status_at of this Account.  # noqa: E501
        :rtype: object
        """
        return self._last_status_at

    @last_status_at.setter
    def last_status_at(self, last_status_at):
        """Sets the last_status_at of this Account.

        When the most recent status was posted (ISO 8601 Datetime).  # noqa: E501

        :param last_status_at: The last_status_at of this Account.  # noqa: E501
        :type: object
        """

        self._last_status_at = last_status_at

    @property
    def statuses_count(self):
        """Gets the statuses_count of this Account.  # noqa: E501

        How many statuses are attached to this account.  # noqa: E501

        :return: The statuses_count of this Account.  # noqa: E501
        :rtype: object
        """
        return self._statuses_count

    @statuses_count.setter
    def statuses_count(self, statuses_count):
        """Sets the statuses_count of this Account.

        How many statuses are attached to this account.  # noqa: E501

        :param statuses_count: The statuses_count of this Account.  # noqa: E501
        :type: object
        """
        if statuses_count is None:
            raise ValueError("Invalid value for `statuses_count`, must not be `None`")  # noqa: E501

        self._statuses_count = statuses_count

    @property
    def followers_count(self):
        """Gets the followers_count of this Account.  # noqa: E501

        The reported followers of this profile.  # noqa: E501

        :return: The followers_count of this Account.  # noqa: E501
        :rtype: object
        """
        return self._followers_count

    @followers_count.setter
    def followers_count(self, followers_count):
        """Sets the followers_count of this Account.

        The reported followers of this profile.  # noqa: E501

        :param followers_count: The followers_count of this Account.  # noqa: E501
        :type: object
        """
        if followers_count is None:
            raise ValueError("Invalid value for `followers_count`, must not be `None`")  # noqa: E501

        self._followers_count = followers_count

    @property
    def following_count(self):
        """Gets the following_count of this Account.  # noqa: E501

        The reported follows of this profile.  # noqa: E501

        :return: The following_count of this Account.  # noqa: E501
        :rtype: object
        """
        return self._following_count

    @following_count.setter
    def following_count(self, following_count):
        """Sets the following_count of this Account.

        The reported follows of this profile.  # noqa: E501

        :param following_count: The following_count of this Account.  # noqa: E501
        :type: object
        """
        if following_count is None:
            raise ValueError("Invalid value for `following_count`, must not be `None`")  # noqa: E501

        self._following_count = following_count

    @property
    def display_name(self):
        """Gets the display_name of this Account.  # noqa: E501

        The profile's display name.  # noqa: E501

        :return: The display_name of this Account.  # noqa: E501
        :rtype: object
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Account.

        The profile's display name.  # noqa: E501

        :param display_name: The display_name of this Account.  # noqa: E501
        :type: object
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def note(self):
        """Gets the note of this Account.  # noqa: E501

        The profile's bio / description (HTML string).  # noqa: E501

        :return: The note of this Account.  # noqa: E501
        :rtype: object
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Account.

        The profile's bio / description (HTML string).  # noqa: E501

        :param note: The note of this Account.  # noqa: E501
        :type: object
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def avatar(self):
        """Gets the avatar of this Account.  # noqa: E501

        An image icon that is shown next to statuses and in the profile.  # noqa: E501

        :return: The avatar of this Account.  # noqa: E501
        :rtype: object
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this Account.

        An image icon that is shown next to statuses and in the profile.  # noqa: E501

        :param avatar: The avatar of this Account.  # noqa: E501
        :type: object
        """
        if avatar is None:
            raise ValueError("Invalid value for `avatar`, must not be `None`")  # noqa: E501

        self._avatar = avatar

    @property
    def avatar_static(self):
        """Gets the avatar_static of this Account.  # noqa: E501

        A static version of the avatar. Equal to `avatar` if its value is a static image; different if `avatar` is an animated GIF.  # noqa: E501

        :return: The avatar_static of this Account.  # noqa: E501
        :rtype: object
        """
        return self._avatar_static

    @avatar_static.setter
    def avatar_static(self, avatar_static):
        """Sets the avatar_static of this Account.

        A static version of the avatar. Equal to `avatar` if its value is a static image; different if `avatar` is an animated GIF.  # noqa: E501

        :param avatar_static: The avatar_static of this Account.  # noqa: E501
        :type: object
        """
        if avatar_static is None:
            raise ValueError("Invalid value for `avatar_static`, must not be `None`")  # noqa: E501

        self._avatar_static = avatar_static

    @property
    def header(self):
        """Gets the header of this Account.  # noqa: E501

        An image banner that is shown above the profile and in profile cards.  # noqa: E501

        :return: The header of this Account.  # noqa: E501
        :rtype: object
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Account.

        An image banner that is shown above the profile and in profile cards.  # noqa: E501

        :param header: The header of this Account.  # noqa: E501
        :type: object
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def header_static(self):
        """Gets the header_static of this Account.  # noqa: E501

        A static version of the header. Equal to `header` if its value is a static image; different if `header` is an animated GIF.  # noqa: E501

        :return: The header_static of this Account.  # noqa: E501
        :rtype: object
        """
        return self._header_static

    @header_static.setter
    def header_static(self, header_static):
        """Sets the header_static of this Account.

        A static version of the header. Equal to `header` if its value is a static image; different if `header` is an animated GIF.  # noqa: E501

        :param header_static: The header_static of this Account.  # noqa: E501
        :type: object
        """
        if header_static is None:
            raise ValueError("Invalid value for `header_static`, must not be `None`")  # noqa: E501

        self._header_static = header_static

    @property
    def locked(self):
        """Gets the locked of this Account.  # noqa: E501

        Whether the account manually approves follow requests.  # noqa: E501

        :return: The locked of this Account.  # noqa: E501
        :rtype: object
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this Account.

        Whether the account manually approves follow requests.  # noqa: E501

        :param locked: The locked of this Account.  # noqa: E501
        :type: object
        """
        if locked is None:
            raise ValueError("Invalid value for `locked`, must not be `None`")  # noqa: E501

        self._locked = locked

    @property
    def emojis(self):
        """Gets the emojis of this Account.  # noqa: E501

        Custom emoji entities to be used when rendering the profile. If none, an empty array will be returned.  # noqa: E501

        :return: The emojis of this Account.  # noqa: E501
        :rtype: object
        """
        return self._emojis

    @emojis.setter
    def emojis(self, emojis):
        """Sets the emojis of this Account.

        Custom emoji entities to be used when rendering the profile. If none, an empty array will be returned.  # noqa: E501

        :param emojis: The emojis of this Account.  # noqa: E501
        :type: object
        """
        if emojis is None:
            raise ValueError("Invalid value for `emojis`, must not be `None`")  # noqa: E501

        self._emojis = emojis

    @property
    def discoverable(self):
        """Gets the discoverable of this Account.  # noqa: E501

        Whether the account has opted into discovery features such as the profile directory.  # noqa: E501

        :return: The discoverable of this Account.  # noqa: E501
        :rtype: object
        """
        return self._discoverable

    @discoverable.setter
    def discoverable(self, discoverable):
        """Sets the discoverable of this Account.

        Whether the account has opted into discovery features such as the profile directory.  # noqa: E501

        :param discoverable: The discoverable of this Account.  # noqa: E501
        :type: object
        """
        if discoverable is None:
            raise ValueError("Invalid value for `discoverable`, must not be `None`")  # noqa: E501

        self._discoverable = discoverable

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
