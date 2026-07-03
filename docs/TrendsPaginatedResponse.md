# TrendsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**records** | **List[object]** |  | [optional] 
**total_count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from odditt_api_client.models.trends_paginated_response import TrendsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsPaginatedResponse from a JSON string
trends_paginated_response_instance = TrendsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(TrendsPaginatedResponse.to_json())

# convert the object into a dict
trends_paginated_response_dict = trends_paginated_response_instance.to_dict()
# create an instance of TrendsPaginatedResponse from a dict
trends_paginated_response_from_dict = TrendsPaginatedResponse.from_dict(trends_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


