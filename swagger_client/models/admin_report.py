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

class AdminReport(object):
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
        'action_taken': 'object',
        'comment': 'object',
        'created_at': 'object',
        'updated_at': 'object',
        'account': 'Account',
        'target_account': 'Account',
        'assigned_account': 'Account',
        'action_taken_by_account': 'object',
        'statuses': 'object'
    }

    attribute_map = {
        'id': 'id',
        'action_taken': 'action_taken',
        'comment': 'comment',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'account': 'account',
        'target_account': 'target_account',
        'assigned_account': 'assigned_account',
        'action_taken_by_account': 'action_taken_by_account',
        'statuses': 'statuses'
    }

    def __init__(self, id=None, action_taken=None, comment=None, created_at=None, updated_at=None, account=None, target_account=None, assigned_account=None, action_taken_by_account=None, statuses=None):  # noqa: E501
        """AdminReport - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._action_taken = None
        self._comment = None
        self._created_at = None
        self._updated_at = None
        self._account = None
        self._target_account = None
        self._assigned_account = None
        self._action_taken_by_account = None
        self._statuses = None
        self.discriminator = None
        self.id = id
        if action_taken is not None:
            self.action_taken = action_taken
        if comment is not None:
            self.comment = comment
        self.created_at = created_at
        self.updated_at = updated_at
        self.account = account
        self.target_account = target_account
        self.assigned_account = assigned_account
        self.action_taken_by_account = action_taken_by_account
        self.statuses = statuses

    @property
    def id(self):
        """Gets the id of this AdminReport.  # noqa: E501

        The ID of the report in the database.  # noqa: E501

        :return: The id of this AdminReport.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminReport.

        The ID of the report in the database.  # noqa: E501

        :param id: The id of this AdminReport.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def action_taken(self):
        """Gets the action_taken of this AdminReport.  # noqa: E501

        The action taken to resolve this report.  # noqa: E501

        :return: The action_taken of this AdminReport.  # noqa: E501
        :rtype: object
        """
        return self._action_taken

    @action_taken.setter
    def action_taken(self, action_taken):
        """Sets the action_taken of this AdminReport.

        The action taken to resolve this report.  # noqa: E501

        :param action_taken: The action_taken of this AdminReport.  # noqa: E501
        :type: object
        """

        self._action_taken = action_taken

    @property
    def comment(self):
        """Gets the comment of this AdminReport.  # noqa: E501

        An optional reason for reporting.  # noqa: E501

        :return: The comment of this AdminReport.  # noqa: E501
        :rtype: object
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AdminReport.

        An optional reason for reporting.  # noqa: E501

        :param comment: The comment of this AdminReport.  # noqa: E501
        :type: object
        """

        self._comment = comment

    @property
    def created_at(self):
        """Gets the created_at of this AdminReport.  # noqa: E501

        The time the report was filed.  # noqa: E501

        :return: The created_at of this AdminReport.  # noqa: E501
        :rtype: object
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AdminReport.

        The time the report was filed.  # noqa: E501

        :param created_at: The created_at of this AdminReport.  # noqa: E501
        :type: object
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AdminReport.  # noqa: E501

        The time of last action on this report.  # noqa: E501

        :return: The updated_at of this AdminReport.  # noqa: E501
        :rtype: object
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AdminReport.

        The time of last action on this report.  # noqa: E501

        :param updated_at: The updated_at of this AdminReport.  # noqa: E501
        :type: object
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def account(self):
        """Gets the account of this AdminReport.  # noqa: E501


        :return: The account of this AdminReport.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AdminReport.


        :param account: The account of this AdminReport.  # noqa: E501
        :type: Account
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def target_account(self):
        """Gets the target_account of this AdminReport.  # noqa: E501


        :return: The target_account of this AdminReport.  # noqa: E501
        :rtype: Account
        """
        return self._target_account

    @target_account.setter
    def target_account(self, target_account):
        """Sets the target_account of this AdminReport.


        :param target_account: The target_account of this AdminReport.  # noqa: E501
        :type: Account
        """
        if target_account is None:
            raise ValueError("Invalid value for `target_account`, must not be `None`")  # noqa: E501

        self._target_account = target_account

    @property
    def assigned_account(self):
        """Gets the assigned_account of this AdminReport.  # noqa: E501


        :return: The assigned_account of this AdminReport.  # noqa: E501
        :rtype: Account
        """
        return self._assigned_account

    @assigned_account.setter
    def assigned_account(self, assigned_account):
        """Sets the assigned_account of this AdminReport.


        :param assigned_account: The assigned_account of this AdminReport.  # noqa: E501
        :type: Account
        """
        if assigned_account is None:
            raise ValueError("Invalid value for `assigned_account`, must not be `None`")  # noqa: E501

        self._assigned_account = assigned_account

    @property
    def action_taken_by_account(self):
        """Gets the action_taken_by_account of this AdminReport.  # noqa: E501

        The action taken by the moderator who handled the report.  # noqa: E501

        :return: The action_taken_by_account of this AdminReport.  # noqa: E501
        :rtype: object
        """
        return self._action_taken_by_account

    @action_taken_by_account.setter
    def action_taken_by_account(self, action_taken_by_account):
        """Sets the action_taken_by_account of this AdminReport.

        The action taken by the moderator who handled the report.  # noqa: E501

        :param action_taken_by_account: The action_taken_by_account of this AdminReport.  # noqa: E501
        :type: object
        """
        if action_taken_by_account is None:
            raise ValueError("Invalid value for `action_taken_by_account`, must not be `None`")  # noqa: E501

        self._action_taken_by_account = action_taken_by_account

    @property
    def statuses(self):
        """Gets the statuses of this AdminReport.  # noqa: E501

        Statuses attached to the report, for context.  # noqa: E501

        :return: The statuses of this AdminReport.  # noqa: E501
        :rtype: object
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this AdminReport.

        Statuses attached to the report, for context.  # noqa: E501

        :param statuses: The statuses of this AdminReport.  # noqa: E501
        :type: object
        """
        if statuses is None:
            raise ValueError("Invalid value for `statuses`, must not be `None`")  # noqa: E501

        self._statuses = statuses

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
        if issubclass(AdminReport, dict):
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
        if not isinstance(other, AdminReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
