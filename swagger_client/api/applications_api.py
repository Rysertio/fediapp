# coding: utf-8

"""
    Mastodon API

    The API for interacting with Mastodon.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ApplicationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_api_v1_apps_verify_credentials(self, **kwargs):  # noqa: E501
        """Verify your app works  # noqa: E501

        Confirm that the app's OAuth2 credentials work.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_v1_apps_verify_credentials(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_v1_apps_verify_credentials_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_api_v1_apps_verify_credentials_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_api_v1_apps_verify_credentials_with_http_info(self, **kwargs):  # noqa: E501
        """Verify your app works  # noqa: E501

        Confirm that the app's OAuth2 credentials work.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_v1_apps_verify_credentials_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_v1_apps_verify_credentials" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['client-auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/apps/verify_credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_api_v1_apps(self, **kwargs):  # noqa: E501
        """Create an application  # noqa: E501

        Create a new application to obtain OAuth2 credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_api_v1_apps(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object client_name:
        :param object redirect_uris:
        :param object scopes:
        :param object website:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_api_v1_apps_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_api_v1_apps_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_api_v1_apps_with_http_info(self, **kwargs):  # noqa: E501
        """Create an application  # noqa: E501

        Create a new application to obtain OAuth2 credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_api_v1_apps_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object client_name:
        :param object redirect_uris:
        :param object scopes:
        :param object website:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_name', 'redirect_uris', 'scopes', 'website']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_api_v1_apps" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'client_name' in params:
            form_params.append(('client_name', params['client_name']))  # noqa: E501
        if 'redirect_uris' in params:
            form_params.append(('redirect_uris', params['redirect_uris']))  # noqa: E501
        if 'scopes' in params:
            form_params.append(('scopes', params['scopes']))  # noqa: E501
        if 'website' in params:
            form_params.append(('website', params['website']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/apps', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
