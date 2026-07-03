# V1TrendsByBettingMarketPositionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_betting_market_position_ids** | **List[int]** | Array of event betting market position IDs | 
**odds_format** | **str** | Odds display format. Defaults per product_mode (dfs→multiplier, prediction_market→percent, else american). | [optional] 
**product_mode** | **str** | Display mode. dfs rewrites stat lines to MORE/LESS; on the paginated flows endpoints it also auto-filters to over/under player props (entity_type&#x3D;player, positions [4,5]) unless an entity/position filter is set. | [optional] 
**use_cartoon_images** | **bool** | When true, the logo fields on each flow, leg, and multi-trend slot (default_logo_url, logo_url_1, logo_url_2) are replaced with cartoon-jersey image URLs derived from the relevant team, player, or league. When false or omitted, the original logo URLs are returned. Defaults to false. | [optional] 

## Example

```python
from odditt_api_client.models.v1_trends_by_betting_market_position_post_request import V1TrendsByBettingMarketPositionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1TrendsByBettingMarketPositionPostRequest from a JSON string
v1_trends_by_betting_market_position_post_request_instance = V1TrendsByBettingMarketPositionPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1TrendsByBettingMarketPositionPostRequest.to_json())

# convert the object into a dict
v1_trends_by_betting_market_position_post_request_dict = v1_trends_by_betting_market_position_post_request_instance.to_dict()
# create an instance of V1TrendsByBettingMarketPositionPostRequest from a dict
v1_trends_by_betting_market_position_post_request_from_dict = V1TrendsByBettingMarketPositionPostRequest.from_dict(v1_trends_by_betting_market_position_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


