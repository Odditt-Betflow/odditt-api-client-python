# AuthOAuthLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from odditt_api_client.models.auth_o_auth_login_request import AuthOAuthLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthOAuthLoginRequest from a JSON string
auth_o_auth_login_request_instance = AuthOAuthLoginRequest.from_json(json)
# print the JSON string representation of the object
print(AuthOAuthLoginRequest.to_json())

# convert the object into a dict
auth_o_auth_login_request_dict = auth_o_auth_login_request_instance.to_dict()
# create an instance of AuthOAuthLoginRequest from a dict
auth_o_auth_login_request_from_dict = AuthOAuthLoginRequest.from_dict(auth_o_auth_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


