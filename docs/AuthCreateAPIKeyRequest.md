# AuthCreateAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from odditt_api_client.models.auth_create_api_key_request import AuthCreateAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthCreateAPIKeyRequest from a JSON string
auth_create_api_key_request_instance = AuthCreateAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(AuthCreateAPIKeyRequest.to_json())

# convert the object into a dict
auth_create_api_key_request_dict = auth_create_api_key_request_instance.to_dict()
# create an instance of AuthCreateAPIKeyRequest from a dict
auth_create_api_key_request_from_dict = AuthCreateAPIKeyRequest.from_dict(auth_create_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


