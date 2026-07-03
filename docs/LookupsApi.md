# odditt_api_client.LookupsApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_affiliates_lookups_affiliate_networks_get**](LookupsApi.md#v1_affiliates_lookups_affiliate_networks_get) | **GET** /v1/affiliates/lookups/affiliate-networks | Affiliate networks
[**v1_affiliates_lookups_offer_categories_get**](LookupsApi.md#v1_affiliates_lookups_offer_categories_get) | **GET** /v1/affiliates/lookups/offer-categories | Offer categories
[**v1_affiliates_lookups_operator_jurisdictions_get**](LookupsApi.md#v1_affiliates_lookups_operator_jurisdictions_get) | **GET** /v1/affiliates/lookups/operator-jurisdictions | Operator jurisdictions
[**v1_affiliates_lookups_operators_get**](LookupsApi.md#v1_affiliates_lookups_operators_get) | **GET** /v1/affiliates/lookups/operators | Operators


# **v1_affiliates_lookups_affiliate_networks_get**
> object v1_affiliates_lookups_affiliate_networks_get()

Affiliate networks

### Example

* Api Key Authentication (ApiKeyAuth):
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.LookupsApi(api_client)

    try:
        # Affiliate networks
        api_response = api_instance.v1_affiliates_lookups_affiliate_networks_get()
        print("The response of LookupsApi->v1_affiliates_lookups_affiliate_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->v1_affiliates_lookups_affiliate_networks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_lookups_offer_categories_get**
> object v1_affiliates_lookups_offer_categories_get()

Offer categories

### Example

* Api Key Authentication (ApiKeyAuth):
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.LookupsApi(api_client)

    try:
        # Offer categories
        api_response = api_instance.v1_affiliates_lookups_offer_categories_get()
        print("The response of LookupsApi->v1_affiliates_lookups_offer_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->v1_affiliates_lookups_offer_categories_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_lookups_operator_jurisdictions_get**
> object v1_affiliates_lookups_operator_jurisdictions_get(operator_id=operator_id, country_code=country_code)

Operator jurisdictions

Where we believe an operator is live. Informational only — not an upload gate.

### Example

* Api Key Authentication (ApiKeyAuth):
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.LookupsApi(api_client)
    operator_id = 56 # int |  (optional)
    country_code = 'country_code_example' # str |  (optional)

    try:
        # Operator jurisdictions
        api_response = api_instance.v1_affiliates_lookups_operator_jurisdictions_get(operator_id=operator_id, country_code=country_code)
        print("The response of LookupsApi->v1_affiliates_lookups_operator_jurisdictions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->v1_affiliates_lookups_operator_jurisdictions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **int**|  | [optional] 
 **country_code** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_lookups_operators_get**
> object v1_affiliates_lookups_operators_get(search=search, page=page, page_size=page_size)

Operators

Paginated list of operators, optionally filtered by a free-text search term.

### Example

* Api Key Authentication (ApiKeyAuth):
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = odditt_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.LookupsApi(api_client)
    search = 'search_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Operators
        api_response = api_instance.v1_affiliates_lookups_operators_get(search=search, page=page, page_size=page_size)
        print("The response of LookupsApi->v1_affiliates_lookups_operators_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupsApi->v1_affiliates_lookups_operators_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

