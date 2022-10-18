import logging
from datetime import timedelta
import sys
from typing import Text
import uuid
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
import logging
import snowflake_sql_api_client
from snowflake_sql_api_client.rest import ApiException
from pprint import pprint
from snowflake_sql_api_client.utilities.sql_api_generate_jwt import JWTGenerator 

class  SqlApiUtils(object):
    ######################################################## 
    # Generate JWT Token
    ########################################################
    def get_jwt_token(self, account_identifier: Text, user: Text, sa_prv_key: Text, sa_prv_key_pw: Text, lifetime_in_minutes = 59, renewal_delay_in_minutes=54) -> Text:
        private_key = None
        # Load the private key from the specified file.
        try:
            # Try to access the private key without a passphrase.
            private_key = load_pem_private_key(sa_prv_key.encode(), None, default_backend())
        except TypeError:
            # If that fails, provide the passphrase returned from get_private_key_passphrase().
            private_key = load_pem_private_key(sa_prv_key.encode(), sa_prv_key_pw.encode(), default_backend())

        token = JWTGenerator(
            account=account_identifier
            , user=user
            , private_key=private_key
            , lifetime=timedelta(minutes=lifetime_in_minutes)
            , renewal_delay=timedelta(minutes=renewal_delay_in_minutes)
            ).get_token()

        return token

    ######################################################## 
    # Get Snokwflake SQL API instance
    # 
    ########################################################
    def get_api_instance(self, account_identifier: Text, user: Text, host_url: Text, sa_prv_key: Text, sa_prv_key_pw: Text) -> snowflake_sql_api_client.Apiv2statementsApi:
        ### Get JWT Token
        jwt_token = self.get_jwt_token(
            account_identifier=account_identifier,
            user=user,
            sa_prv_key=sa_prv_key,
            sa_prv_key_pw=sa_prv_key_pw
            )

        ### Call Snowflake SQL API
        configuration = snowflake_sql_api_client.Configuration()

        # Configure Host URL
        configuration.host = host_url

        # Configure API key authorization: bearerAuth
        configuration.api_key['Authorization'] = jwt_token
        # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
        configuration.api_key_prefix['Authorization'] = 'Bearer'

        # create an instance of the API class
        api_instance = snowflake_sql_api_client.Apiv2statementsApi(snowflake_sql_api_client.ApiClient(configuration))
        
        return api_instance