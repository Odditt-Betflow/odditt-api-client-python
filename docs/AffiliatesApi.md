# odditt_api_client.AffiliatesApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_affiliates_event_position_post**](AffiliatesApi.md#v1_affiliates_event_position_post) | **POST** /v1/affiliates/event-position | Single-bet cart for affiliate mode
[**v1_affiliates_parlay_post**](AffiliatesApi.md#v1_affiliates_parlay_post) | **POST** /v1/affiliates/parlay | Parlay cart for affiliate mode


# **v1_affiliates_event_position_post**
> object v1_affiliates_event_position_post(v1_affiliates_event_position_post_request)

Single-bet cart for affiliate mode

Returns live odds across operators for a single event betting market position, overlaid with the calling client's best affiliate offer per operator. Powers the widget's "Bet Now" cart for a single selection. Results are scoped to the authenticated client; operators can be gated with operator_ids / operator_keys.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_event_position_post_request import V1AffiliatesEventPositionPostRequest
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
    api_instance = odditt_api_client.AffiliatesApi(api_client)
    v1_affiliates_event_position_post_request = {"country_code":"US","event_betting_market_position_id":351558937,"operator_ids":[1,2],"subnational_region_code":"NJ"} # V1AffiliatesEventPositionPostRequest | 

    try:
        # Single-bet cart for affiliate mode
        api_response = api_instance.v1_affiliates_event_position_post(v1_affiliates_event_position_post_request)
        print("The response of AffiliatesApi->v1_affiliates_event_position_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliatesApi->v1_affiliates_event_position_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_event_position_post_request** | [**V1AffiliatesEventPositionPostRequest**](V1AffiliatesEventPositionPostRequest.md)|  | 

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

# **v1_affiliates_parlay_post**
> object v1_affiliates_parlay_post(v1_affiliates_parlay_post_request)

Parlay cart for affiliate mode

Returns combined parlay odds per operator, the per-leg single bets, and the calling client's best affiliate offer per operator, with combo deeplinks generated per operator. Powers the widget's "Bet Now" cart for a multi-leg bet. Results are scoped to the authenticated client; operators can be gated with operator_ids / operator_keys.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_parlay_post_request import V1AffiliatesParlayPostRequest
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
    api_instance = odditt_api_client.AffiliatesApi(api_client)
    v1_affiliates_parlay_post_request = {"country_code":"US","event_betting_market_position_ids":[351558937,351558940],"operator_ids":[1,2],"subnational_region_code":"NJ"} # V1AffiliatesParlayPostRequest | 

    try:
        # Parlay cart for affiliate mode
        api_response = api_instance.v1_affiliates_parlay_post(v1_affiliates_parlay_post_request)
        print("The response of AffiliatesApi->v1_affiliates_parlay_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliatesApi->v1_affiliates_parlay_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_parlay_post_request** | [**V1AffiliatesParlayPostRequest**](V1AffiliatesParlayPostRequest.md)|  | 

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

