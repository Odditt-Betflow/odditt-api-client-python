# V1AffiliatesEventsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 
**device_type** | **str** |  | [optional] 
**event_type** | **str** |  | 
**offer_campaign** | **str** |  | [optional] 
**offer_id** | **UUID** |  | 
**offer_label** | **str** |  | [optional] 
**operator_id** | **int** |  | 
**session_token** | **str** |  | [optional] 
**subnational_region_code** | **str** |  | [optional] 

## Example

```python
from odditt_api_client.models.v1_affiliates_events_post_request import V1AffiliatesEventsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AffiliatesEventsPostRequest from a JSON string
v1_affiliates_events_post_request_instance = V1AffiliatesEventsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AffiliatesEventsPostRequest.to_json())

# convert the object into a dict
v1_affiliates_events_post_request_dict = v1_affiliates_events_post_request_instance.to_dict()
# create an instance of V1AffiliatesEventsPostRequest from a dict
v1_affiliates_events_post_request_from_dict = V1AffiliatesEventsPostRequest.from_dict(v1_affiliates_events_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


