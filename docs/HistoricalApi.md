# odditt_api_client.HistoricalApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_historical_events_get**](HistoricalApi.md#v1_historical_events_get) | **GET** /v1/historical/events | List historical odds events (paginated)
[**v1_historical_odds_event_id_ext_get**](HistoricalApi.md#v1_historical_odds_event_id_ext_get) | **GET** /v1/historical/odds/{event_id}.{ext} | Download a per-event historical odds file


# **v1_historical_events_get**
> object v1_historical_events_get(schema_version=schema_version, sport_id=sport_id, league_id=league_id, team_id=team_id, start_date=start_date, end_date=end_date, page=page, page_size=page_size)

List historical odds events (paginated)

Returns a paginated catalog of per-event historical odds files the authenticated client has access to. Each result entry carries pre-baked download URLs for the JSON and CSV payloads; clients GET those URLs directly. Results are scoped to the authenticated client; callers without a client association receive `403 Forbidden`.


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
    api_instance = odditt_api_client.HistoricalApi(api_client)
    schema_version = 'v1' # str | Payload schema version. Defaults to `v1` when omitted. Unknown versions are rejected. (optional) (default to 'v1')
    sport_id = 56 # int |  (optional)
    league_id = 56 # int |  (optional)
    team_id = 56 # int | Filter to events involving this team as either home or away. (optional)
    start_date = 'start_date_example' # str | Inclusive lower bound on the event/affiliation date, ISO format YYYY-MM-DD. (optional)
    end_date = 'end_date_example' # str | Inclusive upper bound on the event/affiliation date, ISO format YYYY-MM-DD. (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # List historical odds events (paginated)
        api_response = api_instance.v1_historical_events_get(schema_version=schema_version, sport_id=sport_id, league_id=league_id, team_id=team_id, start_date=start_date, end_date=end_date, page=page, page_size=page_size)
        print("The response of HistoricalApi->v1_historical_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoricalApi->v1_historical_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_version** | **str**| Payload schema version. Defaults to &#x60;v1&#x60; when omitted. Unknown versions are rejected. | [optional] [default to &#39;v1&#39;]
 **sport_id** | **int**|  | [optional] 
 **league_id** | **int**|  | [optional] 
 **team_id** | **int**| Filter to events involving this team as either home or away. | [optional] 
 **start_date** | **str**| Inclusive lower bound on the event/affiliation date, ISO format YYYY-MM-DD. | [optional] 
 **end_date** | **str**| Inclusive upper bound on the event/affiliation date, ISO format YYYY-MM-DD. | [optional] 
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
**401** | Missing or invalid credentials. |  -  |
**403** | Authenticated but not permitted to access this resource. |  -  |
**422** | The request body was syntactically valid JSON but one or more fields failed validation; the message names each offending field. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_historical_odds_event_id_ext_get**
> object v1_historical_odds_event_id_ext_get(event_id, ext, schema_version=schema_version)

Download a per-event historical odds file

Resolves the requested per-event file for the authenticated client and streams the JSON or CSV payload back. The response body is the raw file content (not the manifest envelope); the API takes care of fetching the bytes from the underlying CDN so callers see a single HTTP call per file.

The `sha256` of the bytes-at-rest is exposed as a strong `ETag`. Clients can short-circuit with `If-None-Match` to receive `304 Not Modified`. `Range` requests are forwarded upstream and `206 Partial Content` responses are relayed unchanged — useful for resuming multi-MB CSV downloads.


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
    api_instance = odditt_api_client.HistoricalApi(api_client)
    event_id = 56 # int | Canonical event identifier.
    ext = 'ext_example' # str | File format. `json` returns `application/json`; `csv` returns `text/csv`.
    schema_version = 'v1' # str | Payload schema version. Defaults to `v1` when omitted. (optional) (default to 'v1')

    try:
        # Download a per-event historical odds file
        api_response = api_instance.v1_historical_odds_event_id_ext_get(event_id, ext, schema_version=schema_version)
        print("The response of HistoricalApi->v1_historical_odds_event_id_ext_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoricalApi->v1_historical_odds_event_id_ext_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Canonical event identifier. | 
 **ext** | **str**| File format. &#x60;json&#x60; returns &#x60;application/json&#x60;; &#x60;csv&#x60; returns &#x60;text/csv&#x60;. | 
 **schema_version** | **str**| Payload schema version. Defaults to &#x60;v1&#x60; when omitted. | [optional] [default to &#39;v1&#39;]

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File payload streamed back to the client. |  * Content-Disposition - Always &#x60;attachment; filename&#x3D;\&quot;event_&lt;event_id&gt;.&lt;ext&gt;\&quot;&#x60;. <br>  * ETag - Strong validator based on the SHA-256 of the file bytes-at-rest. <br>  |
**206** | Partial content when the client provided a &#x60;Range&#x60; header. |  -  |
**304** | Not modified — the client supplied a matching &#x60;If-None-Match&#x60;. |  -  |
**400** | The request was malformed (invalid path/query parameter or JSON type mismatch in the body). |  -  |
**401** | Missing or invalid credentials. |  -  |
**403** | Authenticated but not permitted to access this resource. |  -  |
**404** | The requested resource does not exist. |  -  |
**422** | The request body was syntactically valid JSON but one or more fields failed validation; the message names each offending field. |  -  |
**500** | Unexpected server error. |  -  |
**502** | Upstream content delivery unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

