# TrendsErrorResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Machine-readable error code. Possible values:   * &#x60;BAD_REQUEST&#x60; — malformed request, invalid path/query parameter, or JSON type mismatch in the body. Returned with HTTP 400.   * &#x60;VALIDATION_ERROR&#x60; — one or more request fields failed validation rules; the message names each offending field. Returned with HTTP 422 (Unprocessable Entity).   * &#x60;AMBIGUOUS_LOOKUP&#x60; — a slug identifier matched more than one record; qualify it (e.g. &#x60;country/league&#x60;) and retry.   * &#x60;UNAUTHORIZED&#x60; — missing or invalid credentials.   * &#x60;FORBIDDEN&#x60; — authenticated but not permitted to access this resource.   * &#x60;NOT_FOUND&#x60; — resource does not exist.   * &#x60;RATE_LIMIT_EXCEEDED&#x60; — too many requests.   * &#x60;INTERNAL_ERROR&#x60; — unexpected server error.  | 
**message** | **str** | Human-readable explanation of the error. For &#x60;VALIDATION_ERROR&#x60; responses, names the offending field(s) and the rule that failed. | 

## Example

```python
from odditt_api_client.models.trends_error_response_error import TrendsErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsErrorResponseError from a JSON string
trends_error_response_error_instance = TrendsErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(TrendsErrorResponseError.to_json())

# convert the object into a dict
trends_error_response_error_dict = trends_error_response_error_instance.to_dict()
# create an instance of TrendsErrorResponseError from a dict
trends_error_response_error_from_dict = TrendsErrorResponseError.from_dict(trends_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


