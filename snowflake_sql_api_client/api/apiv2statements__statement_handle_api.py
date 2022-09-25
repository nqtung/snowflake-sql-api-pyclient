# coding: utf-8

"""
    Snowflake SQL API V2

    The Snowflake SQL API is a REST API that you can use to access and update data in a Snowflake database.     # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from snowflake_sql_api_client.api_client import ApiClient


class Apiv2statementsStatementHandleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_statements_statement_handle_cancel_post(self, statement_handle, **kwargs):  # noqa: E501
        """Cancels the execution of a statement.  # noqa: E501

        Cancels the execution of the statement with the specified statement handle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_statements_statement_handle_cancel_post(statement_handle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str statement_handle: (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution). (required)
        :param str user_agent: (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231.
        :param str x_snowflake_authorization_token_type: Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed.
        :param str accept:
        :param str request_id: Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_statements_statement_handle_cancel_post_with_http_info(statement_handle, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_statements_statement_handle_cancel_post_with_http_info(statement_handle, **kwargs)  # noqa: E501
            return data

    def api_v2_statements_statement_handle_cancel_post_with_http_info(self, statement_handle, **kwargs):  # noqa: E501
        """Cancels the execution of a statement.  # noqa: E501

        Cancels the execution of the statement with the specified statement handle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_statements_statement_handle_cancel_post_with_http_info(statement_handle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str statement_handle: (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution). (required)
        :param str user_agent: (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231.
        :param str x_snowflake_authorization_token_type: Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed.
        :param str accept:
        :param str request_id: Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['statement_handle', 'user_agent', 'x_snowflake_authorization_token_type', 'accept', 'request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_statements_statement_handle_cancel_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'statement_handle' is set
        if ('statement_handle' not in params or
                params['statement_handle'] is None):
            raise ValueError("Missing the required parameter `statement_handle` when calling `api_v2_statements_statement_handle_cancel_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'statement_handle' in params:
            path_params['statementHandle'] = params['statement_handle']  # noqa: E501

        query_params = []
        if 'request_id' in params:
            query_params.append(('requestId', params['request_id']))  # noqa: E501

        header_params = {}
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'x_snowflake_authorization_token_type' in params:
            header_params['X-Snowflake-Authorization-Token-Type'] = params['x_snowflake_authorization_token_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/statements/{statementHandle}/cancel', 'POST',
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

    def api_v2_statements_statement_handle_get(self, statement_handle, **kwargs):  # noqa: E501
        """Checks the status of the execution of a statement  # noqa: E501

        Checks the status of the execution of the statement with the specified statement handle. If the statement was executed successfully, the operation returns the requested partition of the result set.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_statements_statement_handle_get(statement_handle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str statement_handle: (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution). (required)
        :param str user_agent: (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231.
        :param str x_snowflake_authorization_token_type: Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed.
        :param str accept:
        :param str request_id: Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned.
        :param str partition: Number of the partition of results to return. The number can range from 0 to the total number of partitions minus 1.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_statements_statement_handle_get_with_http_info(statement_handle, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_statements_statement_handle_get_with_http_info(statement_handle, **kwargs)  # noqa: E501
            return data

    def api_v2_statements_statement_handle_get_with_http_info(self, statement_handle, **kwargs):  # noqa: E501
        """Checks the status of the execution of a statement  # noqa: E501

        Checks the status of the execution of the statement with the specified statement handle. If the statement was executed successfully, the operation returns the requested partition of the result set.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_statements_statement_handle_get_with_http_info(statement_handle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str statement_handle: (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution). (required)
        :param str user_agent: (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231.
        :param str x_snowflake_authorization_token_type: Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed.
        :param str accept:
        :param str request_id: Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned.
        :param str partition: Number of the partition of results to return. The number can range from 0 to the total number of partitions minus 1.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['statement_handle', 'user_agent', 'x_snowflake_authorization_token_type', 'accept', 'request_id', 'partition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_statements_statement_handle_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'statement_handle' is set
        if ('statement_handle' not in params or
                params['statement_handle'] is None):
            raise ValueError("Missing the required parameter `statement_handle` when calling `api_v2_statements_statement_handle_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'statement_handle' in params:
            path_params['statementHandle'] = params['statement_handle']  # noqa: E501

        query_params = []
        if 'request_id' in params:
            query_params.append(('requestId', params['request_id']))  # noqa: E501
        if 'partition' in params:
            query_params.append(('partition', params['partition']))  # noqa: E501

        header_params = {}
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'x_snowflake_authorization_token_type' in params:
            header_params['X-Snowflake-Authorization-Token-Type'] = params['x_snowflake_authorization_token_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/statements/{statementHandle}', 'GET',
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
