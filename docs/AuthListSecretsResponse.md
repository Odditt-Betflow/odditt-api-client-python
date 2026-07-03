# AuthListSecretsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[AuthListSecretsResponseSecretsInner]**](AuthListSecretsResponseSecretsInner.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from odditt_api_client.models.auth_list_secrets_response import AuthListSecretsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthListSecretsResponse from a JSON string
auth_list_secrets_response_instance = AuthListSecretsResponse.from_json(json)
# print the JSON string representation of the object
print(AuthListSecretsResponse.to_json())

# convert the object into a dict
auth_list_secrets_response_dict = auth_list_secrets_response_instance.to_dict()
# create an instance of AuthListSecretsResponse from a dict
auth_list_secrets_response_from_dict = AuthListSecretsResponse.from_dict(auth_list_secrets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


