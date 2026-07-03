# AuthListAPIKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | [**List[AuthListAPIKeysResponseApiKeysInner]**](AuthListAPIKeysResponseApiKeysInner.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from odditt_api_client.models.auth_list_api_keys_response import AuthListAPIKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthListAPIKeysResponse from a JSON string
auth_list_api_keys_response_instance = AuthListAPIKeysResponse.from_json(json)
# print the JSON string representation of the object
print(AuthListAPIKeysResponse.to_json())

# convert the object into a dict
auth_list_api_keys_response_dict = auth_list_api_keys_response_instance.to_dict()
# create an instance of AuthListAPIKeysResponse from a dict
auth_list_api_keys_response_from_dict = AuthListAPIKeysResponse.from_dict(auth_list_api_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


