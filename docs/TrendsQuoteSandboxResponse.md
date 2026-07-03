# TrendsQuoteSandboxResponse

Mock pricing response. Shape differs between single (1-leg) and parlay (2+ legs); parlay responses additionally carry top-level combined odds and is_combinable / parlay_failure_reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**american_odds_value** | **str** | Parlay only. Null when uncombinable. | [optional] 
**button_payload** | **str** | Synthetic bet-slip identifier (prefix &#39;FD-MOCK-&#39;). Null when the result is invalid or the parlay is uncombinable. | [optional] 
**decimal_odds_value** | **float** |  | [optional] 
**event_betting_market_position_maps** | **List[object]** |  | 
**flow_id** | **int** |  | 
**flow_type** | **str** |  | 
**fractional_odds_value** | **str** |  | [optional] 
**is_combinable** | **bool** | Parlay only. False if any leg failed or the parlay-level uncombinable roll fired. | [optional] 
**odds_implied_probability** | **float** |  | [optional] 
**parlay_failure_reason** | **str** |  | [optional] 
**payout_multiplier** | **float** |  | [optional] 

## Example

```python
from odditt_api_client.models.trends_quote_sandbox_response import TrendsQuoteSandboxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsQuoteSandboxResponse from a JSON string
trends_quote_sandbox_response_instance = TrendsQuoteSandboxResponse.from_json(json)
# print the JSON string representation of the object
print(TrendsQuoteSandboxResponse.to_json())

# convert the object into a dict
trends_quote_sandbox_response_dict = trends_quote_sandbox_response_instance.to_dict()
# create an instance of TrendsQuoteSandboxResponse from a dict
trends_quote_sandbox_response_from_dict = TrendsQuoteSandboxResponse.from_dict(trends_quote_sandbox_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


