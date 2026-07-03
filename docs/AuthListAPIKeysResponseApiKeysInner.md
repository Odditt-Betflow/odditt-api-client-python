# AuthListAPIKeysResponseApiKeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**key_code** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**widget** | **bool** |  | [optional] 

## Example

```python
from odditt_api_client.models.auth_list_api_keys_response_api_keys_inner import AuthListAPIKeysResponseApiKeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of AuthListAPIKeysResponseApiKeysInner from a JSON string
auth_list_api_keys_response_api_keys_inner_instance = AuthListAPIKeysResponseApiKeysInner.from_json(json)
# print the JSON string representation of the object
print(AuthListAPIKeysResponseApiKeysInner.to_json())

# convert the object into a dict
auth_list_api_keys_response_api_keys_inner_dict = auth_list_api_keys_response_api_keys_inner_instance.to_dict()
# create an instance of AuthListAPIKeysResponseApiKeysInner from a dict
auth_list_api_keys_response_api_keys_inner_from_dict = AuthListAPIKeysResponseApiKeysInner.from_dict(auth_list_api_keys_response_api_keys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


