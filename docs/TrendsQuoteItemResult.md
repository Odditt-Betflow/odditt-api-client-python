# TrendsQuoteItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **object** | Operator response passthrough on 200, error envelope otherwise. | 
**flow_id** | **int** |  | 
**flow_type** | **str** |  | 
**status** | **int** | HTTP-style status code for this single item. 200 &#x3D; success, 404 &#x3D; flow not resolvable, 502 &#x3D; upstream returned non-2xx or non-JSON, 504 &#x3D; upstream timed out. | 

## Example

```python
from odditt_api_client.models.trends_quote_item_result import TrendsQuoteItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsQuoteItemResult from a JSON string
trends_quote_item_result_instance = TrendsQuoteItemResult.from_json(json)
# print the JSON string representation of the object
print(TrendsQuoteItemResult.to_json())

# convert the object into a dict
trends_quote_item_result_dict = trends_quote_item_result_instance.to_dict()
# create an instance of TrendsQuoteItemResult from a dict
trends_quote_item_result_from_dict = TrendsQuoteItemResult.from_dict(trends_quote_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


