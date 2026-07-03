# V1AffiliatesDealsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] [default to 'US']
**excluded_operator_ids** | **List[int]** |  | [optional] 
**hide_offers_links** | **bool** |  | [optional] 
**mode** | **str** |  | [optional] [default to 'carousel']
**offer_campaign** | **str** |  | [optional] 
**offer_type** | **str** |  | [optional] [default to 'sports']
**operator_ids** | **List[int]** |  | [optional] 
**operator_keys** | **List[str]** |  | [optional] 
**operator_type_ids** | **List[int]** |  | [optional] 
**page_number** | **int** |  | [optional] [default to 1]
**page_size** | **int** |  | [optional] [default to 20]
**subnational_region_code** | **str** |  | [optional] 
**with_reviews** | **bool** | When true | [optional] 

## Example

```python
from odditt_api_client.models.v1_affiliates_deals_post_request import V1AffiliatesDealsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AffiliatesDealsPostRequest from a JSON string
v1_affiliates_deals_post_request_instance = V1AffiliatesDealsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AffiliatesDealsPostRequest.to_json())

# convert the object into a dict
v1_affiliates_deals_post_request_dict = v1_affiliates_deals_post_request_instance.to_dict()
# create an instance of V1AffiliatesDealsPostRequest from a dict
v1_affiliates_deals_post_request_from_dict = V1AffiliatesDealsPostRequest.from_dict(v1_affiliates_deals_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


