# AffiliateErrorResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from odditt_api_client.models.affiliate_error_response_error import AffiliateErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateErrorResponseError from a JSON string
affiliate_error_response_error_instance = AffiliateErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(AffiliateErrorResponseError.to_json())

# convert the object into a dict
affiliate_error_response_error_dict = affiliate_error_response_error_instance.to_dict()
# create an instance of AffiliateErrorResponseError from a dict
affiliate_error_response_error_from_dict = AffiliateErrorResponseError.from_dict(affiliate_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


