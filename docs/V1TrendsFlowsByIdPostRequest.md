# V1TrendsFlowsByIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fact_flow_type** | **str** | Sub-type for fact flows. Defaults to &#39;base&#39; if omitted. | [optional] 
**flow_ids** | **List[int]** | Array of flow IDs to retrieve | 
**flow_type** | **str** |  | 
**use_cartoon_images** | **bool** | When true, the logo fields on each flow, leg, and multi-trend slot (default_logo_url, logo_url_1, logo_url_2) are replaced with cartoon-jersey image URLs derived from the relevant team, player, or league. When false or omitted, the original logo URLs are returned. Defaults to false. | [optional] 

## Example

```python
from odditt_api_client.models.v1_trends_flows_by_id_post_request import V1TrendsFlowsByIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1TrendsFlowsByIdPostRequest from a JSON string
v1_trends_flows_by_id_post_request_instance = V1TrendsFlowsByIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1TrendsFlowsByIdPostRequest.to_json())

# convert the object into a dict
v1_trends_flows_by_id_post_request_dict = v1_trends_flows_by_id_post_request_instance.to_dict()
# create an instance of V1TrendsFlowsByIdPostRequest from a dict
v1_trends_flows_by_id_post_request_from_dict = V1TrendsFlowsByIdPostRequest.from_dict(v1_trends_flows_by_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


