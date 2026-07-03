# V1AffiliatesLinksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_deep_link_url** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] [default to 'US']
**ios_deep_link_url** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**offer_call_to_action** | **str** |  | [optional] 
**offer_campaign** | **str** |  | [optional] 
**offer_category_id** | **int** |  | 
**offer_display_bullets** | **List[str]** |  | [optional] 
**offer_display_small_print** | **str** |  | [optional] 
**offer_ev_usd** | **float** |  | [optional] 
**offer_label** | **str** |  | [optional] 
**offer_priority** | **int** |  | [optional] 
**offer_tagline** | **str** |  | [optional] 
**operator_id** | **int** | One of operator_id or operator_name is required. | [optional] 
**operator_name** | **str** |  | [optional] 
**source_network_affiliate_partner_id** | **int** |  | [optional] 
**subnational_region_code** | **str** | Omit for country-grain inventory. | [optional] 
**web_deep_link_url** | **str** |  | 

## Example

```python
from odditt_api_client.models.v1_affiliates_links_post_request import V1AffiliatesLinksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AffiliatesLinksPostRequest from a JSON string
v1_affiliates_links_post_request_instance = V1AffiliatesLinksPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AffiliatesLinksPostRequest.to_json())

# convert the object into a dict
v1_affiliates_links_post_request_dict = v1_affiliates_links_post_request_instance.to_dict()
# create an instance of V1AffiliatesLinksPostRequest from a dict
v1_affiliates_links_post_request_from_dict = V1AffiliatesLinksPostRequest.from_dict(v1_affiliates_links_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


