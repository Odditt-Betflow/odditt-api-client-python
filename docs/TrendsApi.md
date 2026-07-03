# odditt_api_client.TrendsApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_trends_by_betting_market_position_post**](TrendsApi.md#v1_trends_by_betting_market_position_post) | **POST** /v1/trends/by-betting-market-position | Get flows by betting market position IDs
[**v1_trends_flow_graph_data_fact_flow_id_get**](TrendsApi.md#v1_trends_flow_graph_data_fact_flow_id_get) | **GET** /v1/trends/flow-graph-data/{fact_flow_id} | Get fact flow graph data
[**v1_trends_flow_tooltip_flow_type_flow_id_get**](TrendsApi.md#v1_trends_flow_tooltip_flow_type_flow_id_get) | **GET** /v1/trends/flow-tooltip/{flow_type}/{flow_id} | Get flow tooltip payload
[**v1_trends_flows_by_id_post**](TrendsApi.md#v1_trends_flows_by_id_post) | **POST** /v1/trends/flows-by-id | Get flows by ids
[**v1_trends_flows_post**](TrendsApi.md#v1_trends_flows_post) | **POST** /v1/trends/flows | Get flows (paginated)
[**v1_trends_flows_quote_post**](TrendsApi.md#v1_trends_flows_quote_post) | **POST** /v1/trends/flows/quote | Quote a batch of flows against the caller&#39;s configured check endpoint
[**v1_trends_flows_quote_sandbox_post**](TrendsApi.md#v1_trends_flows_quote_sandbox_post) | **POST** /v1/trends/flows/quote-sandbox | Mock operator pricing endpoint — for sandbox / development use
[**v1_trends_leagues_with_available_flows_get**](TrendsApi.md#v1_trends_leagues_with_available_flows_get) | **GET** /v1/trends/leagues-with-available-flows | Get leagues with available flows
[**v1_trends_mixed_flows_post**](TrendsApi.md#v1_trends_mixed_flows_post) | **POST** /v1/trends/mixed-flows | Get mixed flows (paginated)
[**v1_trends_widget_event_post**](TrendsApi.md#v1_trends_widget_event_post) | **POST** /v1/trends/widget/event | Submit a widget telemetry event


# **v1_trends_by_betting_market_position_post**
> object v1_trends_by_betting_market_position_post(v1_trends_by_betting_market_position_post_request)

Get flows by betting market position IDs

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_trends_by_betting_market_position_post_request import V1TrendsByBettingMarketPositionPostRequest
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
    api_instance = odditt_api_client.TrendsApi(api_client)
    v1_trends_by_betting_market_position_post_request = {"event_betting_market_position_ids":[1,2,3]} # V1TrendsByBettingMarketPositionPostRequest | 

    try:
        # Get flows by betting market position IDs
        api_response = api_instance.v1_trends_by_betting_market_position_post(v1_trends_by_betting_market_position_post_request)
        print("The response of TrendsApi->v1_trends_by_betting_market_position_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_by_betting_market_position_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_trends_by_betting_market_position_post_request** | [**V1TrendsByBettingMarketPositionPostRequest**](V1TrendsByBettingMarketPositionPostRequest.md)|  | 

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
**200** | OK. Each record carries &#x60;flow_type&#x3D;fact_flow&#x60; and &#x60;fact_flow_type&#x3D;multi&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_flow_graph_data_fact_flow_id_get**
> object v1_trends_flow_graph_data_fact_flow_id_get(fact_flow_id)

Get fact flow graph data

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
    api_instance = odditt_api_client.TrendsApi(api_client)
    fact_flow_id = 56 # int | The fact flow ID to get graph data for

    try:
        # Get fact flow graph data
        api_response = api_instance.v1_trends_flow_graph_data_fact_flow_id_get(fact_flow_id)
        print("The response of TrendsApi->v1_trends_flow_graph_data_fact_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_flow_graph_data_fact_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fact_flow_id** | **int**| The fact flow ID to get graph data for | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_flow_tooltip_flow_type_flow_id_get**
> object v1_trends_flow_tooltip_flow_type_flow_id_get(flow_type, flow_id)

Get flow tooltip payload

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
    api_instance = odditt_api_client.TrendsApi(api_client)
    flow_type = 'flow_type_example' # str | Type of flow (fact or fun)
    flow_id = 56 # int | The flow ID to get tooltip data for

    try:
        # Get flow tooltip payload
        api_response = api_instance.v1_trends_flow_tooltip_flow_type_flow_id_get(flow_type, flow_id)
        print("The response of TrendsApi->v1_trends_flow_tooltip_flow_type_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_flow_tooltip_flow_type_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_type** | **str**| Type of flow (fact or fun) | 
 **flow_id** | **int**| The flow ID to get tooltip data for | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_flows_by_id_post**
> object v1_trends_flows_by_id_post(v1_trends_flows_by_id_post_request)

Get flows by ids

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_trends_flows_by_id_post_request import V1TrendsFlowsByIdPostRequest
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
    api_instance = odditt_api_client.TrendsApi(api_client)
    v1_trends_flows_by_id_post_request = odditt_api_client.V1TrendsFlowsByIdPostRequest() # V1TrendsFlowsByIdPostRequest | 

    try:
        # Get flows by ids
        api_response = api_instance.v1_trends_flows_by_id_post(v1_trends_flows_by_id_post_request)
        print("The response of TrendsApi->v1_trends_flows_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_flows_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_trends_flows_by_id_post_request** | [**V1TrendsFlowsByIdPostRequest**](V1TrendsFlowsByIdPostRequest.md)|  | 

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
**200** | OK. Every record carries a &#x60;flow_type&#x60; string with one of: &#x60;fact_flow&#x60;, &#x60;fun_flow&#x60;, &#x60;fact_flow_parlay&#x60;, &#x60;fun_flow_parlay&#x60;, &#x60;plain_flow_parlay&#x60;. Parlay records also include the same field on each entry of their nested &#x60;flows&#x60; array. Records with &#x60;flow_type&#x3D;fact_flow&#x60; additionally carry a &#x60;fact_flow_type&#x60; string with one of: &#x60;base&#x60;, &#x60;expanded&#x60;, &#x60;multi&#x60;. Inside parlay records, fact_flow entries in the nested &#x60;flows&#x60; array are always &#x60;base&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_flows_post**
> object v1_trends_flows_post(v1_trends_flows_post_request)

Get flows (paginated)

Same parameters as mixed-flows but returns non-mixed (single-type) flows. Uses the same underlying request model.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_trends_flows_post_request import V1TrendsFlowsPostRequest
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
    api_instance = odditt_api_client.TrendsApi(api_client)
    v1_trends_flows_post_request = {"bet_type":"singles","fact_flow_type":"base","flow_type":"fact","league_id":7,"page":1,"page_size":20,"sport_id":1,"starting_soon":true} # V1TrendsFlowsPostRequest | 

    try:
        # Get flows (paginated)
        api_response = api_instance.v1_trends_flows_post(v1_trends_flows_post_request)
        print("The response of TrendsApi->v1_trends_flows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_flows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_trends_flows_post_request** | [**V1TrendsFlowsPostRequest**](V1TrendsFlowsPostRequest.md)|  | 

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
**200** | OK. Every record carries a &#x60;flow_type&#x60; string with one of: &#x60;fact_flow&#x60;, &#x60;fun_flow&#x60;, &#x60;fact_flow_parlay&#x60;, &#x60;fun_flow_parlay&#x60;, &#x60;plain_flow_parlay&#x60;. Parlay records also include the same field on each entry of their nested &#x60;flows&#x60; array. Records with &#x60;flow_type&#x3D;fact_flow&#x60; additionally carry a &#x60;fact_flow_type&#x60; string with one of: &#x60;base&#x60;, &#x60;expanded&#x60;, &#x60;multi&#x60;. Inside parlay records, fact_flow entries in the nested &#x60;flows&#x60; array are always &#x60;base&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_flows_quote_post**
> List[TrendsQuoteItemResult] v1_trends_flows_quote_post(trends_quote_flow_item)

Quote a batch of flows against the caller's configured check endpoint

Accepts a JSON array of 1..50 flow specifications and, for each one, forwards a hydrated payload to the URL the caller has registered under `/v1/account/check-endpoint`. Outbound calls run in parallel; the response is a JSON array with one entry per input item, in input order. Per-item failures are encoded in each entry's `status` (and `body`) so one bad operator response does not poison the others. Batch-level failures map to HTTP 4xx without an array body — 412 when the caller has not configured a check endpoint, 422 on validation failure.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_quote_flow_item import TrendsQuoteFlowItem
from odditt_api_client.models.trends_quote_item_result import TrendsQuoteItemResult
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
    api_instance = odditt_api_client.TrendsApi(api_client)
    trends_quote_flow_item = [odditt_api_client.TrendsQuoteFlowItem()] # List[TrendsQuoteFlowItem] | 

    try:
        # Quote a batch of flows against the caller's configured check endpoint
        api_response = api_instance.v1_trends_flows_quote_post(trends_quote_flow_item)
        print("The response of TrendsApi->v1_trends_flows_quote_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_flows_quote_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trends_quote_flow_item** | [**List[TrendsQuoteFlowItem]**](TrendsQuoteFlowItem.md)|  | 

### Return type

[**List[TrendsQuoteItemResult]**](TrendsQuoteItemResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of per-item results in input order. |  -  |
**400** | Malformed request body. |  -  |
**412** | Caller has not configured a check endpoint. |  -  |
**422** | Validation failed (empty batch, batch too large, or any item failed field validation). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_flows_quote_sandbox_post**
> TrendsQuoteSandboxResponse v1_trends_flows_quote_sandbox_post(trends_quote_sandbox_request)

Mock operator pricing endpoint — for sandbox / development use

Drop-in stand-in for a real operator's pricing endpoint. Accepts ONE hydrated pricing payload (the exact shape that /v1/trends/flows/quote POSTs to a configured check endpoint) and returns synthetic pricing- response data with deterministic `button_payload` values and randomly- injected failure modes (~15% rate). Integrators wire this URL into /v1/account/check-endpoint as `url` to round-trip the widget call entirely on platform infrastructure without a real operator. Not for production traffic.

### Example


```python
import odditt_api_client
from odditt_api_client.models.trends_quote_sandbox_request import TrendsQuoteSandboxRequest
from odditt_api_client.models.trends_quote_sandbox_response import TrendsQuoteSandboxResponse
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
    api_instance = odditt_api_client.TrendsApi(api_client)
    trends_quote_sandbox_request = odditt_api_client.TrendsQuoteSandboxRequest() # TrendsQuoteSandboxRequest | 

    try:
        # Mock operator pricing endpoint — for sandbox / development use
        api_response = api_instance.v1_trends_flows_quote_sandbox_post(trends_quote_sandbox_request)
        print("The response of TrendsApi->v1_trends_flows_quote_sandbox_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_flows_quote_sandbox_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trends_quote_sandbox_request** | [**TrendsQuoteSandboxRequest**](TrendsQuoteSandboxRequest.md)|  | 

### Return type

[**TrendsQuoteSandboxResponse**](TrendsQuoteSandboxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mock pricing response, shape depends on single vs parlay. |  -  |
**400** | Malformed request body. |  -  |
**422** | Validation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_leagues_with_available_flows_get**
> object v1_trends_leagues_with_available_flows_get(sport_id=sport_id, sport_key=sport_key)

Get leagues with available flows

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
    api_instance = odditt_api_client.TrendsApi(api_client)
    sport_id = 56 # int |  (optional)
    sport_key = 'sport_key_example' # str | Sport external key (e.g. 'american-football'). Format: {sport_key}. Alternative to sport_id. If both are provided, sport_id takes precedence. (optional)

    try:
        # Get leagues with available flows
        api_response = api_instance.v1_trends_leagues_with_available_flows_get(sport_id=sport_id, sport_key=sport_key)
        print("The response of TrendsApi->v1_trends_leagues_with_available_flows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_leagues_with_available_flows_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**|  | [optional] 
 **sport_key** | **str**| Sport external key (e.g. &#39;american-football&#39;). Format: {sport_key}. Alternative to sport_id. If both are provided, sport_id takes precedence. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_mixed_flows_post**
> object v1_trends_mixed_flows_post(v1_trends_flows_post_request)

Get mixed flows (paginated)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_trends_flows_post_request import V1TrendsFlowsPostRequest
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
    api_instance = odditt_api_client.TrendsApi(api_client)
    v1_trends_flows_post_request = {"bet_type":"singles","fact_flow_type":"base","flow_type":"fact","league_id":7,"page":1,"page_size":20,"sport_id":1,"starting_soon":true} # V1TrendsFlowsPostRequest | 

    try:
        # Get mixed flows (paginated)
        api_response = api_instance.v1_trends_mixed_flows_post(v1_trends_flows_post_request)
        print("The response of TrendsApi->v1_trends_mixed_flows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_mixed_flows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_trends_flows_post_request** | [**V1TrendsFlowsPostRequest**](V1TrendsFlowsPostRequest.md)|  | 

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
**200** | OK. Every record carries a &#x60;flow_type&#x60; string with one of: &#x60;fact_flow&#x60;, &#x60;fun_flow&#x60;, &#x60;fact_flow_parlay&#x60;, &#x60;fun_flow_parlay&#x60;, &#x60;plain_flow_parlay&#x60;. Parlay records also include the same field on each entry of their nested &#x60;flows&#x60; array. Records with &#x60;flow_type&#x3D;fact_flow&#x60; additionally carry a &#x60;fact_flow_type&#x60; string with one of: &#x60;base&#x60;, &#x60;expanded&#x60;, &#x60;multi&#x60;. Inside parlay records, fact_flow entries in the nested &#x60;flows&#x60; array are always &#x60;base&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trends_widget_event_post**
> TrendsWidgetEventResponse v1_trends_widget_event_post(trends_widget_event_request)

Submit a widget telemetry event

Records a single client-side widget interaction (impression, click, dwell, or cart action) for analytics. Accepts a typed envelope `{event_type, mode, event_body}`: `event_type` is a closed enum naming the interaction, optional `mode` describes the widget mode, and `event_body` is an arbitrary JSON object whose shape depends on the event. Available only to widget API keys. Fire-and-forget: returns `202 Accepted` once the event is queued; the response does not guarantee durable storage.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_widget_event_request import TrendsWidgetEventRequest
from odditt_api_client.models.trends_widget_event_response import TrendsWidgetEventResponse
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

# Enter a context with an instance of the API client
with odditt_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odditt_api_client.TrendsApi(api_client)
    trends_widget_event_request = odditt_api_client.TrendsWidgetEventRequest() # TrendsWidgetEventRequest | 

    try:
        # Submit a widget telemetry event
        api_response = api_instance.v1_trends_widget_event_post(trends_widget_event_request)
        print("The response of TrendsApi->v1_trends_widget_event_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->v1_trends_widget_event_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trends_widget_event_request** | [**TrendsWidgetEventRequest**](TrendsWidgetEventRequest.md)|  | 

### Return type

[**TrendsWidgetEventResponse**](TrendsWidgetEventResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Event accepted for asynchronous processing. |  -  |
**400** | Malformed request body. |  -  |
**403** | The API key is not a widget key. |  -  |
**422** | Validation failed (unknown event_type, invalid mode, missing event_body, or event_body is not a JSON object). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

