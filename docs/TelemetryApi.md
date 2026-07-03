# odditt_api_client.TelemetryApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_affiliates_events_post**](TelemetryApi.md#v1_affiliates_events_post) | **POST** /v1/affiliates/events | Log an impression or click


# **v1_affiliates_events_post**
> v1_affiliates_events_post(v1_affiliates_events_post_request)

Log an impression or click

Fire-and-forget telemetry. Records one impression (card render) or click (deeplink tap). Returns 202 on accept; never blocks the widget's click-out.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_events_post_request import V1AffiliatesEventsPostRequest
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
    api_instance = odditt_api_client.TelemetryApi(api_client)
    v1_affiliates_events_post_request = odditt_api_client.V1AffiliatesEventsPostRequest() # V1AffiliatesEventsPostRequest | 

    try:
        # Log an impression or click
        api_instance.v1_affiliates_events_post(v1_affiliates_events_post_request)
    except Exception as e:
        print("Exception when calling TelemetryApi->v1_affiliates_events_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_events_post_request** | [**V1AffiliatesEventsPostRequest**](V1AffiliatesEventsPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**403** | Authenticated but not permitted to access this resource. |  -  |
**422** | One or more fields failed validation; the message names each offending field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

