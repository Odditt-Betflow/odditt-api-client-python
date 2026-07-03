# odditt_api_client.LinksApi

All URIs are relative to *https://api.odditt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_affiliates_links_bulk_deactivate_post**](LinksApi.md#v1_affiliates_links_bulk_deactivate_post) | **POST** /v1/affiliates/links/bulk-deactivate | Bulk deactivate links by filter
[**v1_affiliates_links_bulk_patch**](LinksApi.md#v1_affiliates_links_bulk_patch) | **PATCH** /v1/affiliates/links/bulk | Bulk patch links by filter
[**v1_affiliates_links_bulk_post**](LinksApi.md#v1_affiliates_links_bulk_post) | **POST** /v1/affiliates/links/bulk | Bulk create/upsert links (JSON or CSV)
[**v1_affiliates_links_jobs_get**](LinksApi.md#v1_affiliates_links_jobs_get) | **GET** /v1/affiliates/links/jobs | List async bulk jobs
[**v1_affiliates_links_jobs_job_id_get**](LinksApi.md#v1_affiliates_links_jobs_job_id_get) | **GET** /v1/affiliates/links/jobs/{job_id} | Poll an async bulk job
[**v1_affiliates_links_post**](LinksApi.md#v1_affiliates_links_post) | **POST** /v1/affiliates/links | Create or upsert a single link


# **v1_affiliates_links_bulk_deactivate_post**
> object v1_affiliates_links_bulk_deactivate_post(v1_affiliates_links_bulk_deactivate_post_request)

Bulk deactivate links by filter

Soft-deletes all links matching a filter (e.g. a state goes offline).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_links_bulk_deactivate_post_request import V1AffiliatesLinksBulkDeactivatePostRequest
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
    api_instance = odditt_api_client.LinksApi(api_client)
    v1_affiliates_links_bulk_deactivate_post_request = odditt_api_client.V1AffiliatesLinksBulkDeactivatePostRequest() # V1AffiliatesLinksBulkDeactivatePostRequest | 

    try:
        # Bulk deactivate links by filter
        api_response = api_instance.v1_affiliates_links_bulk_deactivate_post(v1_affiliates_links_bulk_deactivate_post_request)
        print("The response of LinksApi->v1_affiliates_links_bulk_deactivate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->v1_affiliates_links_bulk_deactivate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_links_bulk_deactivate_post_request** | [**V1AffiliatesLinksBulkDeactivatePostRequest**](V1AffiliatesLinksBulkDeactivatePostRequest.md)|  | 

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

# **v1_affiliates_links_bulk_patch**
> object v1_affiliates_links_bulk_patch(v1_affiliates_links_bulk_patch_request)

Bulk patch links by filter

Applies a patch to all links matching a filter (e.g. rewrite all FanDuel-NJ URLs on a domain change).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_links_bulk_patch_request import V1AffiliatesLinksBulkPatchRequest
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
    api_instance = odditt_api_client.LinksApi(api_client)
    v1_affiliates_links_bulk_patch_request = odditt_api_client.V1AffiliatesLinksBulkPatchRequest() # V1AffiliatesLinksBulkPatchRequest | 

    try:
        # Bulk patch links by filter
        api_response = api_instance.v1_affiliates_links_bulk_patch(v1_affiliates_links_bulk_patch_request)
        print("The response of LinksApi->v1_affiliates_links_bulk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->v1_affiliates_links_bulk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_links_bulk_patch_request** | [**V1AffiliatesLinksBulkPatchRequest**](V1AffiliatesLinksBulkPatchRequest.md)|  | 

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

# **v1_affiliates_links_bulk_post**
> object v1_affiliates_links_bulk_post(request_body, dry_run=dry_run, var_async=var_async)

Bulk create/upsert links (JSON or CSV)

Upserts many links idempotently on the natural key. Accepts a JSON array of row objects or a text/csv body (header row). Per-row errors never fail the batch. Use ?dry_run=true to validate without persisting.

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
    api_instance = odditt_api_client.LinksApi(api_client)
    request_body = None # List[object] | 
    dry_run = True # bool | When true, validates the whole batch and returns the per-row report without persisting. Always synchronous. (optional)
    var_async = True # bool | Force background processing. Batches of 500+ rows are queued automatically regardless of this flag. Queued batches return 202 with a job_id to poll at /v1/affiliates/links/jobs/{job_id}. (optional)

    try:
        # Bulk create/upsert links (JSON or CSV)
        api_response = api_instance.v1_affiliates_links_bulk_post(request_body, dry_run=dry_run, var_async=var_async)
        print("The response of LinksApi->v1_affiliates_links_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->v1_affiliates_links_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[object]**](object.md)|  | 
 **dry_run** | **bool**| When true, validates the whole batch and returns the per-row report without persisting. Always synchronous. | [optional] 
 **var_async** | **bool**| Force background processing. Batches of 500+ rows are queued automatically regardless of this flag. Queued batches return 202 with a job_id to poll at /v1/affiliates/links/jobs/{job_id}. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/csv
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Processed synchronously |  -  |
**202** | Accepted for background processing. |  -  |
**400** | The request was malformed. |  -  |
**403** | Authenticated but not permitted to access this resource. |  -  |
**422** | One or more fields failed validation; the message names each offending field. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_links_jobs_get**
> object v1_affiliates_links_jobs_get()

List async bulk jobs

Recent async bulk jobs for the authenticated client.

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
    api_instance = odditt_api_client.LinksApi(api_client)

    try:
        # List async bulk jobs
        api_response = api_instance.v1_affiliates_links_jobs_get()
        print("The response of LinksApi->v1_affiliates_links_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->v1_affiliates_links_jobs_get: %s\n" % e)
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
**403** | Authenticated but not permitted to access this resource. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_links_jobs_job_id_get**
> object v1_affiliates_links_jobs_job_id_get(job_id)

Poll an async bulk job

Status, counts, and per-row errors for one async bulk job. Poll until status is "completed" or "failed". Scoped to the authenticated client.

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
    api_instance = odditt_api_client.LinksApi(api_client)
    job_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Poll an async bulk job
        api_response = api_instance.v1_affiliates_links_jobs_job_id_get(job_id)
        print("The response of LinksApi->v1_affiliates_links_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->v1_affiliates_links_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **UUID**|  | 

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
**400** | The request was malformed. |  -  |
**403** | Authenticated but not permitted to access this resource. |  -  |
**404** | The requested resource does not exist. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_affiliates_links_post**
> object v1_affiliates_links_post(v1_affiliates_links_post_request)

Create or upsert a single link

Creates a link, or updates the existing one on the natural key (operator + geography + category + campaign + label). Resolves operator, country, and region at write time; unresolvable codes return 422.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import odditt_api_client
from odditt_api_client.models.v1_affiliates_links_post_request import V1AffiliatesLinksPostRequest
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
    api_instance = odditt_api_client.LinksApi(api_client)
    v1_affiliates_links_post_request = odditt_api_client.V1AffiliatesLinksPostRequest() # V1AffiliatesLinksPostRequest | 

    try:
        # Create or upsert a single link
        api_response = api_instance.v1_affiliates_links_post(v1_affiliates_links_post_request)
        print("The response of LinksApi->v1_affiliates_links_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->v1_affiliates_links_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_affiliates_links_post_request** | [**V1AffiliatesLinksPostRequest**](V1AffiliatesLinksPostRequest.md)|  | 

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

