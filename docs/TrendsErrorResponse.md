# TrendsErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**TrendsErrorResponseError**](TrendsErrorResponseError.md) |  | 

## Example

```python
from odditt_api_client.models.trends_error_response import TrendsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsErrorResponse from a JSON string
trends_error_response_instance = TrendsErrorResponse.from_json(json)
# print the JSON string representation of the object
print(TrendsErrorResponse.to_json())

# convert the object into a dict
trends_error_response_dict = trends_error_response_instance.to_dict()
# create an instance of TrendsErrorResponse from a dict
trends_error_response_from_dict = TrendsErrorResponse.from_dict(trends_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


