# V1OddsUpcomingOddsByEventPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | The event ID to retrieve odds for | 
**operator_ids** | **List[int]** | Optional list of operator IDs to filter by | [optional] 
**page** | **int** | Page number for pagination | [optional] [default to 1]
**page_size** | **int** | Number of results per page | [optional] [default to 100]

## Example

```python
from odditt_api_client.models.v1_odds_upcoming_odds_by_event_post_request import V1OddsUpcomingOddsByEventPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1OddsUpcomingOddsByEventPostRequest from a JSON string
v1_odds_upcoming_odds_by_event_post_request_instance = V1OddsUpcomingOddsByEventPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1OddsUpcomingOddsByEventPostRequest.to_json())

# convert the object into a dict
v1_odds_upcoming_odds_by_event_post_request_dict = v1_odds_upcoming_odds_by_event_post_request_instance.to_dict()
# create an instance of V1OddsUpcomingOddsByEventPostRequest from a dict
v1_odds_upcoming_odds_by_event_post_request_from_dict = V1OddsUpcomingOddsByEventPostRequest.from_dict(v1_odds_upcoming_odds_by_event_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


