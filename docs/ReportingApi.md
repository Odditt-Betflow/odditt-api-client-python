# odditt_api_client.ReportingApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_affiliates_links_clicks_get**](ReportingApi.md#v1_affiliates_links_clicks_get) | **GET** /v1/affiliates/links/clicks | Impression/click rollups
[**v1_affiliates_links_inventory_summary_get**](ReportingApi.md#v1_affiliates_links_inventory_summary_get) | **GET** /v1/affiliates/links/inventory-summary | Inventory counts


# **v1_affiliates_links_clicks_get**
> object v1_affiliates_links_clicks_get(start_date, end_date, operator_id=operator_id, country_code=country_code, subnational_region_code=subnational_region_code, offer_campaign=offer_campaign, offer_label=offer_label)

Impression/click rollups

Per-link, per-day impression and click counts for the authenticated client.

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
    api_instance = odditt_api_client.ReportingApi(api_client)
    start_date = '2013-10-20' # date | 
    end_date = '2013-10-20' # date | 
    operator_id = 56 # int |  (optional)
    country_code = 'country_code_example' # str |  (optional)
    subnational_region_code = 'subnational_region_code_example' # str |  (optional)
    offer_campaign = 'offer_campaign_example' # str |  (optional)
    offer_label = 'offer_label_example' # str |  (optional)

    try:
        # Impression/click rollups
        api_response = api_instance.v1_affiliates_links_clicks_get(start_date, end_date, operator_id=operator_id, country_code=country_code, subnational_region_code=subnational_region_code, offer_campaign=offer_campaign, offer_label=offer_label)
        print("The response of ReportingApi->v1_affiliates_links_clicks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->v1_affiliates_links_clicks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | 
 **end_date** | **date**|  | 
 **operator_id** | **int**|  | [optional] 
 **country_code** | **str**|  | [optional] 
 **subnational_region_code** | **str**|  | [optional] 
 **offer_campaign** | **str**|  | [optional] 
 **offer_label** | **str**|  | [optional] 

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
**403** | Authenticated but not permitted to access this resource. |  -  |
**422** | One or more fields failed validation; the message names each offending field. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_links_inventory_summary_get**
> object v1_affiliates_links_inventory_summary_get(group_by=group_by)

Inventory counts

Active/inactive link counts grouped by the requested dimension.

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
    api_instance = odditt_api_client.ReportingApi(api_client)
    group_by = operator # str |  (optional) (default to operator)

    try:
        # Inventory counts
        api_response = api_instance.v1_affiliates_links_inventory_summary_get(group_by=group_by)
        print("The response of ReportingApi->v1_affiliates_links_inventory_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->v1_affiliates_links_inventory_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**|  | [optional] [default to operator]

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
**403** | Authenticated but not permitted to access this resource. |  -  |
**422** | One or more fields failed validation; the message names each offending field. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

