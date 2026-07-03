# TrendsQuoteFlowItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | ISO 3166-1 alpha-2 country code (e.g. &#39;US&#39;, &#39;IT&#39;). Uppercased server-side. | 
**event_betting_market_position_ids** | **List[int]** | Leg identifiers that make up this flow. Length 1 &#x3D; single, length 2+ &#x3D; parlay. | 
**flow_id** | **int** |  | 
**flow_type** | **str** |  | 
**region** | **str** | Sub-national region code (e.g. &#39;NJ&#39;, &#39;WA&#39;). Uppercased server-side. | [optional] 

## Example

```python
from odditt_api_client.models.trends_quote_flow_item import TrendsQuoteFlowItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsQuoteFlowItem from a JSON string
trends_quote_flow_item_instance = TrendsQuoteFlowItem.from_json(json)
# print the JSON string representation of the object
print(TrendsQuoteFlowItem.to_json())

# convert the object into a dict
trends_quote_flow_item_dict = trends_quote_flow_item_instance.to_dict()
# create an instance of TrendsQuoteFlowItem from a dict
trends_quote_flow_item_from_dict = TrendsQuoteFlowItem.from_dict(trends_quote_flow_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


