# odditt_api_client.ReferencesApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_references_betting_market_categories_get**](ReferencesApi.md#v1_references_betting_market_categories_get) | **GET** /v1/references/betting-market-categories | Get betting market categories
[**v1_references_betting_market_positions_get**](ReferencesApi.md#v1_references_betting_market_positions_get) | **GET** /v1/references/betting-market-positions | Get all betting market positions
[**v1_references_betting_markets_get**](ReferencesApi.md#v1_references_betting_markets_get) | **GET** /v1/references/betting-markets | Get betting markets (paginated)
[**v1_references_countries_get**](ReferencesApi.md#v1_references_countries_get) | **GET** /v1/references/countries | Get countries (paginated)
[**v1_references_event_periods_get**](ReferencesApi.md#v1_references_event_periods_get) | **GET** /v1/references/event-periods | Get event periods
[**v1_references_leagues_get**](ReferencesApi.md#v1_references_leagues_get) | **GET** /v1/references/leagues | Get leagues (paginated)
[**v1_references_odds_format_get**](ReferencesApi.md#v1_references_odds_format_get) | **GET** /v1/references/odds-format | Get odds formats (paginated)
[**v1_references_operators_get**](ReferencesApi.md#v1_references_operators_get) | **GET** /v1/references/operators | Get operators (paginated)
[**v1_references_players_get**](ReferencesApi.md#v1_references_players_get) | **GET** /v1/references/players | Get players (paginated)
[**v1_references_sports_get**](ReferencesApi.md#v1_references_sports_get) | **GET** /v1/references/sports | Get sports (paginated)
[**v1_references_subnational_regions_get**](ReferencesApi.md#v1_references_subnational_regions_get) | **GET** /v1/references/subnational-regions | Get subnational regions (paginated)
[**v1_references_tag_dimensions_get**](ReferencesApi.md#v1_references_tag_dimensions_get) | **GET** /v1/references/tag-dimensions | Get tag dimensions
[**v1_references_tag_types_search_get**](ReferencesApi.md#v1_references_tag_types_search_get) | **GET** /v1/references/tag-types/search | Search tag types
[**v1_references_tag_types_tag_type_id_children_get**](ReferencesApi.md#v1_references_tag_types_tag_type_id_children_get) | **GET** /v1/references/tag-types/{tag_type_id}/children | Get child tag types
[**v1_references_teams_get**](ReferencesApi.md#v1_references_teams_get) | **GET** /v1/references/teams | Get teams (paginated)


# **v1_references_betting_market_categories_get**
> object v1_references_betting_market_categories_get(sport_id=sport_id, sport_key=sport_key)

Get betting market categories

Returns available betting market categories, optionally filtered by sport.

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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    sport_id = 56 # int |  (optional)
    sport_key = 'sport_key_example' # str | Sport external key (e.g. 'american-football'). Alternative to sport_id. If both are provided, sport_id takes precedence. (optional)

    try:
        # Get betting market categories
        api_response = api_instance.v1_references_betting_market_categories_get(sport_id=sport_id, sport_key=sport_key)
        print("The response of ReferencesApi->v1_references_betting_market_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_betting_market_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**|  | [optional] 
 **sport_key** | **str**| Sport external key (e.g. &#39;american-football&#39;). Alternative to sport_id. If both are provided, sport_id takes precedence. | [optional] 

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

# **v1_references_betting_market_positions_get**
> object v1_references_betting_market_positions_get()

Get all betting market positions

Returns all available betting market positions.

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
    api_instance = odditt_api_client.ReferencesApi(api_client)

    try:
        # Get all betting market positions
        api_response = api_instance.v1_references_betting_market_positions_get()
        print("The response of ReferencesApi->v1_references_betting_market_positions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_betting_market_positions_get: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_references_betting_markets_get**
> object v1_references_betting_markets_get(sport_id=sport_id, sport_key=sport_key, search=search, page=page, page_size=page_size)

Get betting markets (paginated)

Returns a paginated list of betting markets with optional sport filter and text search.

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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    sport_id = 56 # int |  (optional)
    sport_key = 'sport_key_example' # str | Sport external key (e.g. 'american-football'). Alternative to sport_id. If both are provided, sport_id takes precedence. (optional)
    search = 'search_example' # str | Text search filter for betting market names (optional)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    page_size = 100 # int | Number of results per page (optional) (default to 100)

    try:
        # Get betting markets (paginated)
        api_response = api_instance.v1_references_betting_markets_get(sport_id=sport_id, sport_key=sport_key, search=search, page=page, page_size=page_size)
        print("The response of ReferencesApi->v1_references_betting_markets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_betting_markets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**|  | [optional] 
 **sport_key** | **str**| Sport external key (e.g. &#39;american-football&#39;). Alternative to sport_id. If both are provided, sport_id takes precedence. | [optional] 
 **search** | **str**| Text search filter for betting market names | [optional] 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **page_size** | **int**| Number of results per page | [optional] [default to 100]

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

# **v1_references_countries_get**
> TrendsPaginatedResponse v1_references_countries_get(search=search, page=page, page_size=page_size)

Get countries (paginated)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_paginated_response import TrendsPaginatedResponse
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    search = 'search_example' # str | Search by country name (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Get countries (paginated)
        api_response = api_instance.v1_references_countries_get(search=search, page=page, page_size=page_size)
        print("The response of ReferencesApi->v1_references_countries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_countries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search by country name | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**TrendsPaginatedResponse**](TrendsPaginatedResponse.md)

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

# **v1_references_event_periods_get**
> object v1_references_event_periods_get(sport_id=sport_id, sport_key=sport_key)

Get event periods

Returns available event periods, optionally filtered by sport.

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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    sport_id = 56 # int |  (optional)
    sport_key = 'sport_key_example' # str | Sport external key (e.g. 'american-football'). Alternative to sport_id. If both are provided, sport_id takes precedence. (optional)

    try:
        # Get event periods
        api_response = api_instance.v1_references_event_periods_get(sport_id=sport_id, sport_key=sport_key)
        print("The response of ReferencesApi->v1_references_event_periods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_event_periods_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**|  | [optional] 
 **sport_key** | **str**| Sport external key (e.g. &#39;american-football&#39;). Alternative to sport_id. If both are provided, sport_id takes precedence. | [optional] 

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

# **v1_references_leagues_get**
> object v1_references_leagues_get(country_id=country_id, sport_id=sport_id, sport_key=sport_key, search=search, is_popular=is_popular, page=page, page_size=page_size, search_mode=search_mode)

Get leagues (paginated)

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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    country_id = 56 # int |  (optional)
    sport_id = 56 # int |  (optional)
    sport_key = 'sport_key_example' # str | Sport external key (e.g. 'american-football'). Format: {sport_key}. Alternative to sport_id. If both are provided, sport_id takes precedence. (optional)
    search = 'search_example' # str |  (optional)
    is_popular = True # bool |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    search_mode = 'search_mode_example' # str | Search mode (e.g. exact match vs partial). When omitted, uses default search behavior. (optional)

    try:
        # Get leagues (paginated)
        api_response = api_instance.v1_references_leagues_get(country_id=country_id, sport_id=sport_id, sport_key=sport_key, search=search, is_popular=is_popular, page=page, page_size=page_size, search_mode=search_mode)
        print("The response of ReferencesApi->v1_references_leagues_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_leagues_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **int**|  | [optional] 
 **sport_id** | **int**|  | [optional] 
 **sport_key** | **str**| Sport external key (e.g. &#39;american-football&#39;). Format: {sport_key}. Alternative to sport_id. If both are provided, sport_id takes precedence. | [optional] 
 **search** | **str**|  | [optional] 
 **is_popular** | **bool**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **search_mode** | **str**| Search mode (e.g. exact match vs partial). When omitted, uses default search behavior. | [optional] 

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

# **v1_references_odds_format_get**
> TrendsPaginatedResponse v1_references_odds_format_get(search=search, page=page, page_size=page_size)

Get odds formats (paginated)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_paginated_response import TrendsPaginatedResponse
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    search = 'search_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Get odds formats (paginated)
        api_response = api_instance.v1_references_odds_format_get(search=search, page=page, page_size=page_size)
        print("The response of ReferencesApi->v1_references_odds_format_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_odds_format_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**TrendsPaginatedResponse**](TrendsPaginatedResponse.md)

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

# **v1_references_operators_get**
> TrendsPaginatedResponse v1_references_operators_get(search=search, page=page, page_size=page_size)

Get operators (paginated)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_paginated_response import TrendsPaginatedResponse
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    search = 'search_example' # str | Search by operator display name (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Get operators (paginated)
        api_response = api_instance.v1_references_operators_get(search=search, page=page, page_size=page_size)
        print("The response of ReferencesApi->v1_references_operators_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_operators_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search by operator display name | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**TrendsPaginatedResponse**](TrendsPaginatedResponse.md)

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

# **v1_references_players_get**
> object v1_references_players_get(team_id=team_id, team_key=team_key, search=search, page=page, page_size=page_size, search_mode=search_mode)

Get players (paginated)

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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    team_id = 56 # int |  (optional)
    team_key = 'team_key_example' # str | Team external key (e.g. 'new-england-patriots', 'nfl.new-england-patriots'). Format: {team_key} or {league_key}.{team_key}. Alternative to team_id. If both are provided, team_id takes precedence. (optional)
    search = 'search_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    search_mode = 'search_mode_example' # str | Search mode (e.g. exact match vs partial). When omitted, uses default search behavior. (optional)

    try:
        # Get players (paginated)
        api_response = api_instance.v1_references_players_get(team_id=team_id, team_key=team_key, search=search, page=page, page_size=page_size, search_mode=search_mode)
        print("The response of ReferencesApi->v1_references_players_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_players_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | [optional] 
 **team_key** | **str**| Team external key (e.g. &#39;new-england-patriots&#39;, &#39;nfl.new-england-patriots&#39;). Format: {team_key} or {league_key}.{team_key}. Alternative to team_id. If both are provided, team_id takes precedence. | [optional] 
 **search** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **search_mode** | **str**| Search mode (e.g. exact match vs partial). When omitted, uses default search behavior. | [optional] 

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

# **v1_references_sports_get**
> TrendsPaginatedResponse v1_references_sports_get(search=search, page=page, page_size=page_size)

Get sports (paginated)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_paginated_response import TrendsPaginatedResponse
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    search = 'search_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Get sports (paginated)
        api_response = api_instance.v1_references_sports_get(search=search, page=page, page_size=page_size)
        print("The response of ReferencesApi->v1_references_sports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_sports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**TrendsPaginatedResponse**](TrendsPaginatedResponse.md)

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

# **v1_references_subnational_regions_get**
> TrendsPaginatedResponse v1_references_subnational_regions_get(country_id, search=search, page=page, page_size=page_size)

Get subnational regions (paginated)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_paginated_response import TrendsPaginatedResponse
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    country_id = 56 # int | Country ID to filter subnational regions
    search = 'search_example' # str | Search by subnational region name (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Get subnational regions (paginated)
        api_response = api_instance.v1_references_subnational_regions_get(country_id, search=search, page=page, page_size=page_size)
        print("The response of ReferencesApi->v1_references_subnational_regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_subnational_regions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **int**| Country ID to filter subnational regions | 
 **search** | **str**| Search by subnational region name | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**TrendsPaginatedResponse**](TrendsPaginatedResponse.md)

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

# **v1_references_tag_dimensions_get**
> V1ReferencesTagDimensionsGet200Response v1_references_tag_dimensions_get(flow_type=flow_type)

Get tag dimensions

Returns the top-level tag dimension categories. Use these as entry points to explore the tag hierarchy. Optionally filter to dimensions relevant to a specific flow type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_references_tag_dimensions_get200_response import V1ReferencesTagDimensionsGet200Response
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    flow_type = 'flow_type_example' # str | Filter by flow type eligibility. (optional)

    try:
        # Get tag dimensions
        api_response = api_instance.v1_references_tag_dimensions_get(flow_type=flow_type)
        print("The response of ReferencesApi->v1_references_tag_dimensions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_tag_dimensions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_type** | **str**| Filter by flow type eligibility. | [optional] 

### Return type

[**V1ReferencesTagDimensionsGet200Response**](V1ReferencesTagDimensionsGet200Response.md)

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

# **v1_references_tag_types_search_get**
> TrendsPaginatedResponse v1_references_tag_types_search_get(search=search, search_mode=search_mode, dimension=dimension, flow_type=flow_type, terminal_only=terminal_only, tag_level=tag_level, page=page, page_size=page_size)

Search tag types

Search across tag types by keyword. Returns paginated results with breadcrumb paths for disambiguation. Use terminal_only combined with flow_type to find only tags that are usable as filters for a specific flow type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.trends_paginated_response import TrendsPaginatedResponse
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    search = 'search_example' # str |  (optional)
    search_mode = 'search_mode_example' # str | How the search term is matched. Defaults to 'starts_with'. (optional)
    dimension = 'dimension_example' # str | Limit results to a specific dimension (e.g. 'event', 'metadata'). (optional)
    flow_type = 'flow_type_example' # str | Filter by flow type eligibility. (optional)
    terminal_only = False # bool | When true, returns only terminal (filterable) tag types. (optional) (default to False)
    tag_level = 56 # int | Restrict results to a specific hierarchy depth. (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Search tag types
        api_response = api_instance.v1_references_tag_types_search_get(search=search, search_mode=search_mode, dimension=dimension, flow_type=flow_type, terminal_only=terminal_only, tag_level=tag_level, page=page, page_size=page_size)
        print("The response of ReferencesApi->v1_references_tag_types_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_tag_types_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **search_mode** | **str**| How the search term is matched. Defaults to &#39;starts_with&#39;. | [optional] 
 **dimension** | **str**| Limit results to a specific dimension (e.g. &#39;event&#39;, &#39;metadata&#39;). | [optional] 
 **flow_type** | **str**| Filter by flow type eligibility. | [optional] 
 **terminal_only** | **bool**| When true, returns only terminal (filterable) tag types. | [optional] [default to False]
 **tag_level** | **int**| Restrict results to a specific hierarchy depth. | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**TrendsPaginatedResponse**](TrendsPaginatedResponse.md)

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

# **v1_references_tag_types_tag_type_id_children_get**
> V1ReferencesTagTypesTagTypeIdChildrenGet200Response v1_references_tag_types_tag_type_id_children_get(tag_type_id, include_values=include_values, flow_type=flow_type)

Get child tag types

Returns the direct children of a given tag type, along with context about the parent (description and known values). Use this to navigate the tag hierarchy from dimensions down to individual filterable tags.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_references_tag_types_tag_type_id_children_get200_response import V1ReferencesTagTypesTagTypeIdChildrenGet200Response
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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    tag_type_id = 56 # int | Parent tag type ID to drill into.
    include_values = False # bool | When true, includes individual value-level leaf tags in the results. When false (default), value-level leaves are omitted — the parent's known_values field already enumerates them. (optional) (default to False)
    flow_type = 'flow_type_example' # str | Filter by flow type eligibility. (optional)

    try:
        # Get child tag types
        api_response = api_instance.v1_references_tag_types_tag_type_id_children_get(tag_type_id, include_values=include_values, flow_type=flow_type)
        print("The response of ReferencesApi->v1_references_tag_types_tag_type_id_children_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_tag_types_tag_type_id_children_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_type_id** | **int**| Parent tag type ID to drill into. | 
 **include_values** | **bool**| When true, includes individual value-level leaf tags in the results. When false (default), value-level leaves are omitted — the parent&#39;s known_values field already enumerates them. | [optional] [default to False]
 **flow_type** | **str**| Filter by flow type eligibility. | [optional] 

### Return type

[**V1ReferencesTagTypesTagTypeIdChildrenGet200Response**](V1ReferencesTagTypesTagTypeIdChildrenGet200Response.md)

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

# **v1_references_teams_get**
> object v1_references_teams_get(league_id=league_id, league_key=league_key, search=search, page=page, page_size=page_size, search_mode=search_mode, start_date=start_date, end_date=end_date)

Get teams (paginated)

Returns a paginated list of teams. When neither `start_date` nor `end_date` is provided, only teams whose affiliation is currently active are returned. When either date is provided, the result is filtered to teams whose affiliation overlapped the requested window — useful for looking up teams that played in a league during a past season.


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
    api_instance = odditt_api_client.ReferencesApi(api_client)
    league_id = 56 # int |  (optional)
    league_key = 'league_key_example' # str | League external key (e.g. 'nba', 'united-states.nba'). Format: {league_key} or {country_key}.{league_key}. Alternative to league_id. If both are provided, league_id takes precedence. (optional)
    search = 'search_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    search_mode = 'search_mode_example' # str | Search mode (e.g. exact match vs partial). When omitted, uses default search behavior. (optional)
    start_date = 'start_date_example' # str | Inclusive lower bound on the event/affiliation date, ISO format YYYY-MM-DD. (optional)
    end_date = 'end_date_example' # str | Inclusive upper bound on the event/affiliation date, ISO format YYYY-MM-DD. (optional)

    try:
        # Get teams (paginated)
        api_response = api_instance.v1_references_teams_get(league_id=league_id, league_key=league_key, search=search, page=page, page_size=page_size, search_mode=search_mode, start_date=start_date, end_date=end_date)
        print("The response of ReferencesApi->v1_references_teams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->v1_references_teams_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**|  | [optional] 
 **league_key** | **str**| League external key (e.g. &#39;nba&#39;, &#39;united-states.nba&#39;). Format: {league_key} or {country_key}.{league_key}. Alternative to league_id. If both are provided, league_id takes precedence. | [optional] 
 **search** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **search_mode** | **str**| Search mode (e.g. exact match vs partial). When omitted, uses default search behavior. | [optional] 
 **start_date** | **str**| Inclusive lower bound on the event/affiliation date, ISO format YYYY-MM-DD. | [optional] 
 **end_date** | **str**| Inclusive upper bound on the event/affiliation date, ISO format YYYY-MM-DD. | [optional] 

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

