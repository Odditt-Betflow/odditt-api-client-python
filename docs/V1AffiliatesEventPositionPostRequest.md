# V1AffiliatesEventPositionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | ISO 3166-1 alpha-2 country code. | [optional] [default to 'US']
**event_betting_market_position_id** | **int** | The event betting market position to build the cart for. | 
**hide_offers_links** | **bool** | When true, offer metadata is returned without the deep-link URLs. | [optional] 
**odds_format** | **str** | Odds display format. Defaults per product_mode (dfs→multiplier, prediction_market→percent, else american). | [optional] 
**offer_campaign** | **str** | Optional campaign filter. Renders only offers tagged with this campaign. | [optional] 
**operator_ids** | **List[int]** | Optional list of operator IDs to gate which operators appear in the cart. | [optional] 
**operator_keys** | **List[str]** | Optional operator external keys (e.g. &#39;draftkings&#39;). Resolved IDs are merged with operator_ids. | [optional] 
**product_mode** | **str** | Display mode. dfs rewrites leg stat lines to MORE/LESS. | [optional] 
**subnational_region_code** | **str** | ISO 3166-2 subnational region code (used for offer/deeplink resolution). | [optional] 
**use_cartoon_images** | **bool** | When true, swaps default operator/jersey imagery for cartoon variants. | [optional] 

## Example

```python
from odditt_api_client.models.v1_affiliates_event_position_post_request import V1AffiliatesEventPositionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AffiliatesEventPositionPostRequest from a JSON string
v1_affiliates_event_position_post_request_instance = V1AffiliatesEventPositionPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AffiliatesEventPositionPostRequest.to_json())

# convert the object into a dict
v1_affiliates_event_position_post_request_dict = v1_affiliates_event_position_post_request_instance.to_dict()
# create an instance of V1AffiliatesEventPositionPostRequest from a dict
v1_affiliates_event_position_post_request_from_dict = V1AffiliatesEventPositionPostRequest.from_dict(v1_affiliates_event_position_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


