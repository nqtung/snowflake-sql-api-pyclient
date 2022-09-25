# snowflake_sql_api_client.Apiv2statementsApi

All URIs are relative to *https://virtserver.swaggerhub.com/Home4677/Snowflake_SQL_API_V2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_statements_post**](Apiv2statementsApi.md#api_v2_statements_post) | **POST** /api/v2/statements | Submits a SQL statement for execution.

# **api_v2_statements_post**
> object api_v2_statements_post(body=body, user_agent=user_agent, x_snowflake_authorization_token_type=x_snowflake_authorization_token_type, content_type=content_type, accept=accept, request_id=request_id, _async=_async, nullable=nullable)

Submits a SQL statement for execution.

Submits a single statement for execution. You can specify that the statement should be executed asynchronously.

### Example
```python
from __future__ import print_function
import time
import snowflake_sql_api_client
from snowflake_sql_api_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = snowflake_sql_api_client.Apiv2statementsApi(snowflake_sql_api_client.ApiClient(configuration))
body = NULL # object |  (optional)
user_agent = 'user_agent_example' # str | (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231. (optional)
x_snowflake_authorization_token_type = 'x_snowflake_authorization_token_type_example' # str | Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed. (optional)
content_type = 'content_type_example' # str |  (optional)
accept = 'accept_example' # str |  (optional)
request_id = 'request_id_example' # str | Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned. (optional)
_async = '_async_example' # str | Set to true to execute the statement asynchronously and return the statement handle. If the parameter is not specified or is set to false, a statement is executed and the first result is returned if the execution is completed in 45 seconds. If the statement execution takes longer to complete, the statement handle is returned. (optional)
nullable = 'nullable_example' # str | Set to true to execute the statement to generate the result set including null. If the parameter is set to false, the result set value null will be replaced with a string 'null'. (optional)

try:
    # Submits a SQL statement for execution.
    api_response = api_instance.api_v2_statements_post(body=body, user_agent=user_agent, x_snowflake_authorization_token_type=x_snowflake_authorization_token_type, content_type=content_type, accept=accept, request_id=request_id, _async=_async, nullable=nullable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Apiv2statementsApi->api_v2_statements_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **user_agent** | **str**| (Required) Set this to the name and version of your application (e.g. “applicationName/applicationVersion”). You must use a value that complies with RFC 7231. | [optional] 
 **x_snowflake_authorization_token_type** | **str**| Specify the authorization token type for the Authorization header. KEYPAIR_JWT is for Keypair JWT or OAUTH for oAuth token. If not specified, OAUTH is assumed. | [optional] 
 **content_type** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 
 **request_id** | **str**| Unique ID of the API request. This ensures that the execution is idempotent. If not specified, a new UUID is generated and assigned. | [optional] 
 **_async** | **str**| Set to true to execute the statement asynchronously and return the statement handle. If the parameter is not specified or is set to false, a statement is executed and the first result is returned if the execution is completed in 45 seconds. If the statement execution takes longer to complete, the statement handle is returned. | [optional] 
 **nullable** | **str**| Set to true to execute the statement to generate the result set including null. If the parameter is set to false, the result set value null will be replaced with a string &#x27;null&#x27;. | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

