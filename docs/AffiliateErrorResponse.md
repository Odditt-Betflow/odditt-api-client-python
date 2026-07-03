# AffiliateErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AffiliateErrorResponseError**](AffiliateErrorResponseError.md) |  | 

## Example

```python
from odditt_api_client.models.affiliate_error_response import AffiliateErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateErrorResponse from a JSON string
affiliate_error_response_instance = AffiliateErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AffiliateErrorResponse.to_json())

# convert the object into a dict
affiliate_error_response_dict = affiliate_error_response_instance.to_dict()
# create an instance of AffiliateErrorResponse from a dict
affiliate_error_response_from_dict = AffiliateErrorResponse.from_dict(affiliate_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


