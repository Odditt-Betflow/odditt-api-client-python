# V1EventsUpcomingEventsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_date** | **date** | Filter by event date (YYYY-MM-DD). Defaults to today (UTC). | [optional] 
**league_id** | **int** |  | [optional] 
**league_key** | **str** | League external key (e.g. &#39;nba&#39;, &#39;united-states.nba&#39;). Alternative to league_id. If both are provided, league_id takes precedence. | [optional] 
**page** | **int** | Page number for pagination | [optional] [default to 1]
**page_size** | **int** | Number of events per page | [optional] [default to 100]
**sport_id** | **int** |  | [optional] 
**sport_key** | **str** | Sport external key (e.g. &#39;american-football&#39;). Alternative to sport_id. If both are provided, sport_id takes precedence. | [optional] 
**timezone** | **str** | IANA timezone for date interpretation (e.g. &#39;UTC&#39;, &#39;America/New_York&#39;, &#39;Europe/London&#39;) | [optional] [default to 'UTC']

## Example

```python
from odditt_api_client.models.v1_events_upcoming_events_post_request import V1EventsUpcomingEventsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1EventsUpcomingEventsPostRequest from a JSON string
v1_events_upcoming_events_post_request_instance = V1EventsUpcomingEventsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1EventsUpcomingEventsPostRequest.to_json())

# convert the object into a dict
v1_events_upcoming_events_post_request_dict = v1_events_upcoming_events_post_request_instance.to_dict()
# create an instance of V1EventsUpcomingEventsPostRequest from a dict
v1_events_upcoming_events_post_request_from_dict = V1EventsUpcomingEventsPostRequest.from_dict(v1_events_upcoming_events_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


