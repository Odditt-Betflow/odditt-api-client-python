# AuthCheckEndpointResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple** | **bool** |  | [optional] 
**auth_header_name** | **str** |  | [optional] 
**auth_scheme** | **str** | May be empty for raw-value header schemes like &#39;X-API-Key&#39;. | [optional] 
**auth_token_preview** | **str** | Masked preview of the stored auth token (e.g. \&quot;…aB3x\&quot;). The full token is never returned. | [optional] 
**created_at** | **datetime** |  | [optional] 
**method** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from odditt_api_client.models.auth_check_endpoint_response_data import AuthCheckEndpointResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthCheckEndpointResponseData from a JSON string
auth_check_endpoint_response_data_instance = AuthCheckEndpointResponseData.from_json(json)
# print the JSON string representation of the object
print(AuthCheckEndpointResponseData.to_json())

# convert the object into a dict
auth_check_endpoint_response_data_dict = auth_check_endpoint_response_data_instance.to_dict()
# create an instance of AuthCheckEndpointResponseData from a dict
auth_check_endpoint_response_data_from_dict = AuthCheckEndpointResponseData.from_dict(auth_check_endpoint_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


