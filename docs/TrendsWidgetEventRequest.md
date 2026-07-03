# TrendsWidgetEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_body** | **Dict[str, object]** | Arbitrary JSON object carrying event-specific fields. May be an empty object. | 
**event_type** | **str** | The kind of client-side widget interaction being reported. | 
**mode** | **str** | Optional widget mode the interaction occurred in. Defaults to &#x60;clean&#x60;. | [optional] 

## Example

```python
from odditt_api_client.models.trends_widget_event_request import TrendsWidgetEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsWidgetEventRequest from a JSON string
trends_widget_event_request_instance = TrendsWidgetEventRequest.from_json(json)
# print the JSON string representation of the object
print(TrendsWidgetEventRequest.to_json())

# convert the object into a dict
trends_widget_event_request_dict = trends_widget_event_request_instance.to_dict()
# create an instance of TrendsWidgetEventRequest from a dict
trends_widget_event_request_from_dict = TrendsWidgetEventRequest.from_dict(trends_widget_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


