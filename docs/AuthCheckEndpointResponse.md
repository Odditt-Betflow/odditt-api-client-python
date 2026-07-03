# AuthCheckEndpointResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuthCheckEndpointResponseData**](AuthCheckEndpointResponseData.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from odditt_api_client.models.auth_check_endpoint_response import AuthCheckEndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthCheckEndpointResponse from a JSON string
auth_check_endpoint_response_instance = AuthCheckEndpointResponse.from_json(json)
# print the JSON string representation of the object
print(AuthCheckEndpointResponse.to_json())

# convert the object into a dict
auth_check_endpoint_response_dict = auth_check_endpoint_response_instance.to_dict()
# create an instance of AuthCheckEndpointResponse from a dict
auth_check_endpoint_response_from_dict = AuthCheckEndpointResponse.from_dict(auth_check_endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


