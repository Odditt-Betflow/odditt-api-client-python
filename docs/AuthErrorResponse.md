# AuthErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AffiliateErrorResponseError**](AffiliateErrorResponseError.md) |  | 

## Example

```python
from odditt_api_client.models.auth_error_response import AuthErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthErrorResponse from a JSON string
auth_error_response_instance = AuthErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AuthErrorResponse.to_json())

# convert the object into a dict
auth_error_response_dict = auth_error_response_instance.to_dict()
# create an instance of AuthErrorResponse from a dict
auth_error_response_from_dict = AuthErrorResponse.from_dict(auth_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


