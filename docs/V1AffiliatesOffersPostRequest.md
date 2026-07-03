# V1AffiliatesOffersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] [default to 'US']
**excluded_operator_ids** | **List[int]** |  | [optional] 
**hide_offers_links** | **bool** |  | [optional] 
**offer_campaign** | **str** |  | [optional] 
**operator_ids** | **List[int]** |  | [optional] 
**operator_keys** | **List[str]** |  | [optional] 
**operator_type_ids** | **List[int]** |  | [optional] 
**subnational_region_code** | **str** |  | [optional] 

## Example

```python
from odditt_api_client.models.v1_affiliates_offers_post_request import V1AffiliatesOffersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AffiliatesOffersPostRequest from a JSON string
v1_affiliates_offers_post_request_instance = V1AffiliatesOffersPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AffiliatesOffersPostRequest.to_json())

# convert the object into a dict
v1_affiliates_offers_post_request_dict = v1_affiliates_offers_post_request_instance.to_dict()
# create an instance of V1AffiliatesOffersPostRequest from a dict
v1_affiliates_offers_post_request_from_dict = V1AffiliatesOffersPostRequest.from_dict(v1_affiliates_offers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


