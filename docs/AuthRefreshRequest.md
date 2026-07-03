# AuthRefreshRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | 

## Example

```python
from odditt_api_client.models.auth_refresh_request import AuthRefreshRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRefreshRequest from a JSON string
auth_refresh_request_instance = AuthRefreshRequest.from_json(json)
# print the JSON string representation of the object
print(AuthRefreshRequest.to_json())

# convert the object into a dict
auth_refresh_request_dict = auth_refresh_request_instance.to_dict()
# create an instance of AuthRefreshRequest from a dict
auth_refresh_request_from_dict = AuthRefreshRequest.from_dict(auth_refresh_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


