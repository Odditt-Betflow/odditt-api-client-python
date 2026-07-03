# AuthCreateSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | Plaintext secret (returned only once, prefixed with betflow_b2b_) | [optional] 

## Example

```python
from odditt_api_client.models.auth_create_secret_response import AuthCreateSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthCreateSecretResponse from a JSON string
auth_create_secret_response_instance = AuthCreateSecretResponse.from_json(json)
# print the JSON string representation of the object
print(AuthCreateSecretResponse.to_json())

# convert the object into a dict
auth_create_secret_response_dict = auth_create_secret_response_instance.to_dict()
# create an instance of AuthCreateSecretResponse from a dict
auth_create_secret_response_from_dict = AuthCreateSecretResponse.from_dict(auth_create_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


