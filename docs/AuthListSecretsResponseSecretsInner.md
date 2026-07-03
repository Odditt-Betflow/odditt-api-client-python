# AuthListSecretsResponseSecretsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**secret_code** | **UUID** |  | [optional] 
**secret_preview** | **str** | Masked secret preview (e.g. betflow_b2b_...5678901234) | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from odditt_api_client.models.auth_list_secrets_response_secrets_inner import AuthListSecretsResponseSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AuthListSecretsResponseSecretsInner from a JSON string
auth_list_secrets_response_secrets_inner_instance = AuthListSecretsResponseSecretsInner.from_json(json)
# print the JSON string representation of the object
print(AuthListSecretsResponseSecretsInner.to_json())

# convert the object into a dict
auth_list_secrets_response_secrets_inner_dict = auth_list_secrets_response_secrets_inner_instance.to_dict()
# create an instance of AuthListSecretsResponseSecretsInner from a dict
auth_list_secrets_response_secrets_inner_from_dict = AuthListSecretsResponseSecretsInner.from_dict(auth_list_secrets_response_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


