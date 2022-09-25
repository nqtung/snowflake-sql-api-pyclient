# snowflake_sql_api_client.Apiv2statementsStatementHandleApi

All URIs are relative to *https://virtserver.swaggerhub.com/Home4677/Snowflake_SQL_API_V2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_statements_statement_handle_cancel_post**](Apiv2statementsStatementHandleApi.md#api_v2_statements_statement_handle_cancel_post) | **POST** /api/v2/statements/{statementHandle}/cancel | Cancels the execution of a statement.
[**api_v2_statements_statement_handle_get**](Apiv2statementsStatementHandleApi.md#api_v2_statements_statement_handle_get) | **GET** /api/v2/statements/{statementHandle} | Checks the status of the execution of a statement

# **api_v2_statements_statement_handle_cancel_post**
> object api_v2_statements_statement_handle_cancel_post(statement_handle, user_agent=user_agent, x_snowflake_authorization_token_type=x_snowflake_authorization_token_type, accept=accept, request_id=request_id)

Cancels the execution of a statement.

Cancels the execution of the statement with the specified statement handle.

### Example
```python
from __future__ import print_function
import time
import snowflake_sql_api_client
from snowflake_sql_api_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = snowflake_sql_api_client.Apiv2statementsStatementHandleApi(snowflake_sql_api_client.ApiClient(configuration))
statement_handle = 'statement_handle_example' # str | (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution).
user_agent = 'user_agent_example' # str | (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231. (optional)
x_snowflake_authorization_token_type = 'x_snowflake_authorization_token_type_example' # str | Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed. (optional)
accept = 'accept_example' # str |  (optional)
request_id = 'request_id_example' # str | Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned. (optional)

try:
    # Cancels the execution of a statement.
    api_response = api_instance.api_v2_statements_statement_handle_cancel_post(statement_handle, user_agent=user_agent, x_snowflake_authorization_token_type=x_snowflake_authorization_token_type, accept=accept, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Apiv2statementsStatementHandleApi->api_v2_statements_statement_handle_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_handle** | **str**| (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution). | 
 **user_agent** | **str**| (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231. | [optional] 
 **x_snowflake_authorization_token_type** | **str**| Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed. | [optional] 
 **accept** | **str**|  | [optional] 
 **request_id** | **str**| Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned. | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_statements_statement_handle_get**
> object api_v2_statements_statement_handle_get(statement_handle, user_agent=user_agent, x_snowflake_authorization_token_type=x_snowflake_authorization_token_type, accept=accept, request_id=request_id, partition=partition)

Checks the status of the execution of a statement

Checks the status of the execution of the statement with the specified statement handle. If the statement was executed successfully, the operation returns the requested partition of the result set.

### Example
```python
from __future__ import print_function
import time
import snowflake_sql_api_client
from snowflake_sql_api_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = snowflake_sql_api_client.Apiv2statementsStatementHandleApi(snowflake_sql_api_client.ApiClient(configuration))
statement_handle = 'statement_handle_example' # str | (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution).
user_agent = 'user_agent_example' # str | (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231. (optional)
x_snowflake_authorization_token_type = 'x_snowflake_authorization_token_type_example' # str | Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed. (optional)
accept = 'accept_example' # str |  (optional)
request_id = 'request_id_example' # str | Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned. (optional)
partition = 'partition_example' # str | Number of the partition of results to return. The number can range from 0 to the total number of partitions minus 1. (optional)

try:
    # Checks the status of the execution of a statement
    api_response = api_instance.api_v2_statements_statement_handle_get(statement_handle, user_agent=user_agent, x_snowflake_authorization_token_type=x_snowflake_authorization_token_type, accept=accept, request_id=request_id, partition=partition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Apiv2statementsStatementHandleApi->api_v2_statements_statement_handle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_handle** | **str**| (Required) The handle of the statement that you want to use (e.g. to fetch the result set or cancel execution). | 
 **user_agent** | **str**| (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231. | [optional] 
 **x_snowflake_authorization_token_type** | **str**| Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed. | [optional] 
 **accept** | **str**|  | [optional] 
 **request_id** | **str**| Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned. | [optional] 
 **partition** | **str**| Number of the partition of results to return. The number can range from 0 to the total number of partitions minus 1. | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

