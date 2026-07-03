# odditt_api_client.AuthenticationApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_login_post**](AuthenticationApi.md#v1_auth_login_post) | **POST** /v1/auth/login | Login with API key
[**v1_auth_refresh_post**](AuthenticationApi.md#v1_auth_refresh_post) | **POST** /v1/auth/refresh | Refresh tokens
[**v1_oauth_login_post**](AuthenticationApi.md#v1_oauth_login_post) | **POST** /v1/oauth/login | OAuth login (client credentials)
[**v1_oauth_refresh_post**](AuthenticationApi.md#v1_oauth_refresh_post) | **POST** /v1/oauth/refresh | OAuth refresh


# **v1_auth_login_post**
> AuthTokenPair v1_auth_login_post(x_api_key)

Login with API key

### Example


```python
import odditt_api_client
from odditt_api_client.models.auth_token_pair import AuthTokenPair
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)


# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AuthenticationApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Login with API key
        api_response = api_instance.v1_auth_login_post(x_api_key)
        print("The response of AuthenticationApi->v1_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->v1_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**AuthTokenPair**](AuthTokenPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token pair |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_refresh_post**
> AuthTokenPair v1_auth_refresh_post(auth_refresh_request)

Refresh tokens

### Example


```python
import odditt_api_client
from odditt_api_client.models.auth_refresh_request import AuthRefreshRequest
from odditt_api_client.models.auth_token_pair import AuthTokenPair
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)


# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AuthenticationApi(api_client)
    auth_refresh_request = odditt_api_client.AuthRefreshRequest() # AuthRefreshRequest | 

    try:
        # Refresh tokens
        api_response = api_instance.v1_auth_refresh_post(auth_refresh_request)
        print("The response of AuthenticationApi->v1_auth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->v1_auth_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_refresh_request** | [**AuthRefreshRequest**](AuthRefreshRequest.md)|  | 

### Return type

[**AuthTokenPair**](AuthTokenPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token pair |  -  |
**400** | The request was malformed (invalid path/query parameter or JSON type mismatch in the body). |  -  |
**422** | The request body was syntactically valid JSON but one or more fields failed validation; the message names each offending field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_oauth_login_post**
> AuthTokenPair v1_oauth_login_post(auth_o_auth_login_request)

OAuth login (client credentials)

### Example


```python
import odditt_api_client
from odditt_api_client.models.auth_o_auth_login_request import AuthOAuthLoginRequest
from odditt_api_client.models.auth_token_pair import AuthTokenPair
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)


# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AuthenticationApi(api_client)
    auth_o_auth_login_request = odditt_api_client.AuthOAuthLoginRequest() # AuthOAuthLoginRequest | 

    try:
        # OAuth login (client credentials)
        api_response = api_instance.v1_oauth_login_post(auth_o_auth_login_request)
        print("The response of AuthenticationApi->v1_oauth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->v1_oauth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_o_auth_login_request** | [**AuthOAuthLoginRequest**](AuthOAuthLoginRequest.md)|  | 

### Return type

[**AuthTokenPair**](AuthTokenPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token pair |  -  |
**400** | The request was malformed (invalid path/query parameter or JSON type mismatch in the body). |  -  |
**401** | Missing or invalid credentials. |  -  |
**422** | The request body was syntactically valid JSON but one or more fields failed validation; the message names each offending field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_oauth_refresh_post**
> AuthTokenPair v1_oauth_refresh_post(auth_refresh_request)

OAuth refresh

### Example


```python
import odditt_api_client
from odditt_api_client.models.auth_refresh_request import AuthRefreshRequest
from odditt_api_client.models.auth_token_pair import AuthTokenPair
from odditt_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.odditt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = odditt_api_client.Configuration(
    host = "https://api.odditt.com"
)


# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.AuthenticationApi(api_client)
    auth_refresh_request = odditt_api_client.AuthRefreshRequest() # AuthRefreshRequest | 

    try:
        # OAuth refresh
        api_response = api_instance.v1_oauth_refresh_post(auth_refresh_request)
        print("The response of AuthenticationApi->v1_oauth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->v1_oauth_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_refresh_request** | [**AuthRefreshRequest**](AuthRefreshRequest.md)|  | 

### Return type

[**AuthTokenPair**](AuthTokenPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token pair |  -  |
**400** | The request was malformed (invalid path/query parameter or JSON type mismatch in the body). |  -  |
**422** | The request body was syntactically valid JSON but one or more fields failed validation; the message names each offending field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

