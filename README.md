# Snowflake SQL API Client
The Snowflake SQL API is a REST API that you can use to access and update data in a Snowflake database.

Contact Support - Email: tungnq@gmail.com

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install -r requirements.txt
```

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import snowflake_sql_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import snowflake_sql_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import snowflake_sql_api_client
from snowflake_sql_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = snowflake_sql_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

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

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/Home4677/Snowflake_SQL_API_V2/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Apiv2statementsApi* | [**api_v2_statements_post**](docs/Apiv2statementsApi.md#api_v2_statements_post) | **POST** /api/v2/statements | Submits a SQL statement for execution.
*Apiv2statementsStatementHandleApi* | [**api_v2_statements_statement_handle_cancel_post**](docs/Apiv2statementsStatementHandleApi.md#api_v2_statements_statement_handle_cancel_post) | **POST** /api/v2/statements/{statementHandle}/cancel | Cancels the execution of a statement.
*Apiv2statementsStatementHandleApi* | [**api_v2_statements_statement_handle_get**](docs/Apiv2statementsStatementHandleApi.md#api_v2_statements_statement_handle_get) | **GET** /api/v2/statements/{statementHandle} | Checks the status of the execution of a statement

## Documentation For Models


## Documentation For Authorization


## bearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author
