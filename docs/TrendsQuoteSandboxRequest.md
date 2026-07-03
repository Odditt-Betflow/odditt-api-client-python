# TrendsQuoteSandboxRequest

Single hydrated pricing payload — the exact shape /v1/trends/flows/quote sends in each outbound call. Wire this endpoint into /v1/account/check-endpoint to round-trip the widget call entirely on platform infrastructure (no real operator needed).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**event_betting_market_position_maps** | **List[object]** | Hydrated leg array, identical to what the quote endpoint POSTs to a real operator. Pass it through unchanged. | 
**flow_id** | **int** |  | 
**flow_type** | **str** |  | 
**region** | **str** |  | [optional] 

## Example

```python
from odditt_api_client.models.trends_quote_sandbox_request import TrendsQuoteSandboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsQuoteSandboxRequest from a JSON string
trends_quote_sandbox_request_instance = TrendsQuoteSandboxRequest.from_json(json)
# print the JSON string representation of the object
print(TrendsQuoteSandboxRequest.to_json())

# convert the object into a dict
trends_quote_sandbox_request_dict = trends_quote_sandbox_request_instance.to_dict()
# create an instance of TrendsQuoteSandboxRequest from a dict
trends_quote_sandbox_request_from_dict = TrendsQuoteSandboxRequest.from_dict(trends_quote_sandbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


