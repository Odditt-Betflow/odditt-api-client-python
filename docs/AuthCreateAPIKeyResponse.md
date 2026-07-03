# AuthCreateAPIKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Plaintext API key (returned only once) | [optional] 
**key_code** | **UUID** |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from odditt_api_client.models.auth_create_api_key_response import AuthCreateAPIKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthCreateAPIKeyResponse from a JSON string
auth_create_api_key_response_instance = AuthCreateAPIKeyResponse.from_json(json)
# print the JSON string representation of the object
print(AuthCreateAPIKeyResponse.to_json())

# convert the object into a dict
auth_create_api_key_response_dict = auth_create_api_key_response_instance.to_dict()
# create an instance of AuthCreateAPIKeyResponse from a dict
auth_create_api_key_response_from_dict = AuthCreateAPIKeyResponse.from_dict(auth_create_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


