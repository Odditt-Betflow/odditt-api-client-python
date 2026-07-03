# AuthTokenPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**expires_at** | **datetime** |  | 
**expires_in** | **int** |  | 
**refresh_token** | **str** |  | 
**token_type** | **str** |  | 

## Example

```python
from odditt_api_client.models.auth_token_pair import AuthTokenPair

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenPair from a JSON string
auth_token_pair_instance = AuthTokenPair.from_json(json)
# print the JSON string representation of the object
print(AuthTokenPair.to_json())

# convert the object into a dict
auth_token_pair_dict = auth_token_pair_instance.to_dict()
# create an instance of AuthTokenPair from a dict
auth_token_pair_from_dict = AuthTokenPair.from_dict(auth_token_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


