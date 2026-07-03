# odditt_api_client.OffersApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_affiliates_deals_post**](OffersApi.md#v1_affiliates_deals_post) | **POST** /v1/affiliates/deals | Paginated client deals
[**v1_affiliates_offers_post**](OffersApi.md#v1_affiliates_offers_post) | **POST** /v1/affiliates/offers | Client offer cards for a geography


# **v1_affiliates_deals_post**
> object v1_affiliates_deals_post(v1_affiliates_deals_post_request=v1_affiliates_deals_post_request)

Paginated client deals

Paginated client deals (carousel/featured/list), optionally enriched with operator reviews. Scoped to the authenticated client.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_deals_post_request import V1AffiliatesDealsPostRequest
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
    api_instance = odditt_api_client.OffersApi(api_client)
    v1_affiliates_deals_post_request = odditt_api_client.V1AffiliatesDealsPostRequest() # V1AffiliatesDealsPostRequest |  (optional)

    try:
        # Paginated client deals
        api_response = api_instance.v1_affiliates_deals_post(v1_affiliates_deals_post_request=v1_affiliates_deals_post_request)
        print("The response of OffersApi->v1_affiliates_deals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->v1_affiliates_deals_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_deals_post_request** | [**V1AffiliatesDealsPostRequest**](V1AffiliatesDealsPostRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authenticated but not permitted to access this resource. |  -  |
**422** | One or more fields failed validation; the message names each offending field. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_offers_post**
> object v1_affiliates_offers_post(v1_affiliates_offers_post_request=v1_affiliates_offers_post_request)

Client offer cards for a geography

Returns the calling client's best operator offer card per operator for a geography. The core offers read the widget cart renders.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_offers_post_request import V1AffiliatesOffersPostRequest
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
    api_instance = odditt_api_client.OffersApi(api_client)
    v1_affiliates_offers_post_request = odditt_api_client.V1AffiliatesOffersPostRequest() # V1AffiliatesOffersPostRequest |  (optional)

    try:
        # Client offer cards for a geography
        api_response = api_instance.v1_affiliates_offers_post(v1_affiliates_offers_post_request=v1_affiliates_offers_post_request)
        print("The response of OffersApi->v1_affiliates_offers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->v1_affiliates_offers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_offers_post_request** | [**V1AffiliatesOffersPostRequest**](V1AffiliatesOffersPostRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authenticated but not permitted to access this resource. |  -  |
**422** | One or more fields failed validation; the message names each offending field. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

