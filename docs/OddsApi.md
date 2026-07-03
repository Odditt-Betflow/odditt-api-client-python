# odditt_api_client.OddsApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_odds_upcoming_odds_by_event_post**](OddsApi.md#v1_odds_upcoming_odds_by_event_post) | **POST** /v1/odds/upcoming-odds-by-event | Get upcoming odds by event


# **v1_odds_upcoming_odds_by_event_post**
> object v1_odds_upcoming_odds_by_event_post(v1_odds_upcoming_odds_by_event_post_request)

Get upcoming odds by event

Returns paginated betting market positions for a specific upcoming event, optionally filtered by operator.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_odds_upcoming_odds_by_event_post_request import V1OddsUpcomingOddsByEventPostRequest
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
    api_instance = odditt_api_client.OddsApi(api_client)
    v1_odds_upcoming_odds_by_event_post_request = {"event_id":123456,"operator_ids":[1,2,3],"page":1,"page_size":20} # V1OddsUpcomingOddsByEventPostRequest | 

    try:
        # Get upcoming odds by event
        api_response = api_instance.v1_odds_upcoming_odds_by_event_post(v1_odds_upcoming_odds_by_event_post_request)
        print("The response of OddsApi->v1_odds_upcoming_odds_by_event_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OddsApi->v1_odds_upcoming_odds_by_event_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_odds_upcoming_odds_by_event_post_request** | [**V1OddsUpcomingOddsByEventPostRequest**](V1OddsUpcomingOddsByEventPostRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

