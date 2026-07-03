# odditt_api_client.AccountApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_api_keys_get**](AccountApi.md#v1_account_api_keys_get) | **GET** /v1/account/api-keys | List own API keys
[**v1_account_api_keys_key_code_delete**](AccountApi.md#v1_account_api_keys_key_code_delete) | **DELETE** /v1/account/api-keys/{key_code} | Deactivate an API key
[**v1_account_api_keys_post**](AccountApi.md#v1_account_api_keys_post) | **POST** /v1/account/api-keys | Create a new API key
[**v1_account_check_endpoint_delete**](AccountApi.md#v1_account_check_endpoint_delete) | **DELETE** /v1/account/check-endpoint | Delete the check endpoint
[**v1_account_check_endpoint_get**](AccountApi.md#v1_account_check_endpoint_get) | **GET** /v1/account/check-endpoint | Get the configured check endpoint
[**v1_account_check_endpoint_post**](AccountApi.md#v1_account_check_endpoint_post) | **POST** /v1/account/check-endpoint | Set the check endpoint (upsert)
[**v1_account_config_get**](AccountApi.md#v1_account_config_get) | **GET** /v1/account/config | Get own client configuration
[**v1_account_secret_post**](AccountApi.md#v1_account_secret_post) | **POST** /v1/account/secret | Create a new client secret
[**v1_account_secrets_get**](AccountApi.md#v1_account_secrets_get) | **GET** /v1/account/secrets | List own client secrets
[**v1_account_secrets_secret_code_delete**](AccountApi.md#v1_account_secrets_secret_code_delete) | **DELETE** /v1/account/secrets/{secret_code} | Delete a client secret
[**v1_account_usage_get**](AccountApi.md#v1_account_usage_get) | **GET** /v1/account/usage | Get own usage stats


# **v1_account_api_keys_get**
> AuthListAPIKeysResponse v1_account_api_keys_get()

List own API keys

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.auth_list_api_keys_response import AuthListAPIKeysResponse
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)

    try:
        # List own API keys
        api_response = api_instance.v1_account_api_keys_get()
        print("The response of AccountApi->v1_account_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_api_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthListAPIKeysResponse**](AuthListAPIKeysResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of API keys |  -  |
**401** | Missing or invalid credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_api_keys_key_code_delete**
> v1_account_api_keys_key_code_delete(key_code)

Deactivate an API key

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)
    key_code = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Deactivate an API key
        api_instance.v1_account_api_keys_key_code_delete(key_code)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_api_keys_key_code_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_code** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key deactivated |  -  |
**401** | Missing or invalid credentials. |  -  |
**409** | The request conflicts with the current resource state. Uses the account-envelope shape &#x60;{ \&quot;success\&quot;: false, \&quot;error\&quot;: \&quot;...\&quot; }&#x60; rather than the standard error envelope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_api_keys_post**
> AuthCreateAPIKeyResponse v1_account_api_keys_post(auth_create_api_key_request)

Create a new API key

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.auth_create_api_key_request import AuthCreateAPIKeyRequest
from odditt_api_client.models.auth_create_api_key_response import AuthCreateAPIKeyResponse
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)
    auth_create_api_key_request = odditt_api_client.AuthCreateAPIKeyRequest() # AuthCreateAPIKeyRequest | 

    try:
        # Create a new API key
        api_response = api_instance.v1_account_api_keys_post(auth_create_api_key_request)
        print("The response of AccountApi->v1_account_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_create_api_key_request** | [**AuthCreateAPIKeyRequest**](AuthCreateAPIKeyRequest.md)|  | 

### Return type

[**AuthCreateAPIKeyResponse**](AuthCreateAPIKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | API key created (plaintext returned once) |  -  |
**400** | The request was malformed (invalid path/query parameter or JSON type mismatch in the body). |  -  |
**401** | Missing or invalid credentials. |  -  |
**422** | The request body was syntactically valid JSON but one or more fields failed validation; the message names each offending field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_check_endpoint_delete**
> v1_account_check_endpoint_delete()

Delete the check endpoint

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)

    try:
        # Delete the check endpoint
        api_instance.v1_account_check_endpoint_delete()
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_check_endpoint_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Check endpoint deleted |  -  |
**401** | Missing or invalid credentials. |  -  |
**409** | The request conflicts with the current resource state. Uses the account-envelope shape &#x60;{ \&quot;success\&quot;: false, \&quot;error\&quot;: \&quot;...\&quot; }&#x60; rather than the standard error envelope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_check_endpoint_get**
> AuthCheckEndpointResponse v1_account_check_endpoint_get()

Get the configured check endpoint

Returns the URL, method and bearer token preview for the check endpoint used by flow quoting. The full bearer token is never returned.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.auth_check_endpoint_response import AuthCheckEndpointResponse
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)

    try:
        # Get the configured check endpoint
        api_response = api_instance.v1_account_check_endpoint_get()
        print("The response of AccountApi->v1_account_check_endpoint_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_check_endpoint_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthCheckEndpointResponse**](AuthCheckEndpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Check endpoint configuration (or null data if not configured) |  -  |
**401** | Missing or invalid credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_check_endpoint_post**
> AuthCheckEndpointResponse v1_account_check_endpoint_post(auth_set_check_endpoint_request)

Set the check endpoint (upsert)

Stores or updates the URL, method and bearer token used to quote flows against the client's own service. A single configuration exists per client.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.auth_check_endpoint_response import AuthCheckEndpointResponse
from odditt_api_client.models.auth_set_check_endpoint_request import AuthSetCheckEndpointRequest
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)
    auth_set_check_endpoint_request = odditt_api_client.AuthSetCheckEndpointRequest() # AuthSetCheckEndpointRequest | 

    try:
        # Set the check endpoint (upsert)
        api_response = api_instance.v1_account_check_endpoint_post(auth_set_check_endpoint_request)
        print("The response of AccountApi->v1_account_check_endpoint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_check_endpoint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_set_check_endpoint_request** | [**AuthSetCheckEndpointRequest**](AuthSetCheckEndpointRequest.md)|  | 

### Return type

[**AuthCheckEndpointResponse**](AuthCheckEndpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Check endpoint stored |  -  |
**400** | The request was malformed (invalid path/query parameter or JSON type mismatch in the body). |  -  |
**401** | Missing or invalid credentials. |  -  |
**422** | The request body was syntactically valid JSON but one or more fields failed validation; the message names each offending field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_config_get**
> v1_account_config_get()

Get own client configuration

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)

    try:
        # Get own client configuration
        api_instance.v1_account_config_get()
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client configuration |  -  |
**401** | Missing or invalid credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_secret_post**
> AuthCreateSecretResponse v1_account_secret_post()

Create a new client secret

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.auth_create_secret_response import AuthCreateSecretResponse
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)

    try:
        # Create a new client secret
        api_response = api_instance.v1_account_secret_post()
        print("The response of AccountApi->v1_account_secret_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_secret_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthCreateSecretResponse**](AuthCreateSecretResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Secret created (plaintext returned once) |  -  |
**401** | Missing or invalid credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_secrets_get**
> AuthListSecretsResponse v1_account_secrets_get()

List own client secrets

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.auth_list_secrets_response import AuthListSecretsResponse
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)

    try:
        # List own client secrets
        api_response = api_instance.v1_account_secrets_get()
        print("The response of AccountApi->v1_account_secrets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_secrets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthListSecretsResponse**](AuthListSecretsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of secrets |  -  |
**401** | Missing or invalid credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_secrets_secret_code_delete**
> v1_account_secrets_secret_code_delete(secret_code)

Delete a client secret

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)
    secret_code = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a client secret
        api_instance.v1_account_secrets_secret_code_delete(secret_code)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_secrets_secret_code_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_code** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret deleted |  -  |
**401** | Missing or invalid credentials. |  -  |
**409** | The request conflicts with the current resource state. Uses the account-envelope shape &#x60;{ \&quot;success\&quot;: false, \&quot;error\&quot;: \&quot;...\&quot; }&#x60; rather than the standard error envelope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_usage_get**
> v1_account_usage_get(start_date=start_date, end_date=end_date)

Get own usage stats

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AccountApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get own usage stats
        api_instance.v1_account_usage_get(start_date=start_date, end_date=end_date)
    except Exception as e:
        print("Exception when calling AccountApi->v1_account_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage data |  -  |
**401** | Missing or invalid credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

