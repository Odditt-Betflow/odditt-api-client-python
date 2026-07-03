# V1AffiliatesLinksBulkPost202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **UUID** |  | [optional] 
**mode** | **str** |  | [optional] 
**poll_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**submitted_rows** | **int** |  | [optional] 

## Example

```python
from odditt_api_client.models.v1_affiliates_links_bulk_post202_response import V1AffiliatesLinksBulkPost202Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AffiliatesLinksBulkPost202Response from a JSON string
v1_affiliates_links_bulk_post202_response_instance = V1AffiliatesLinksBulkPost202Response.from_json(json)
# print the JSON string representation of the object
print(V1AffiliatesLinksBulkPost202Response.to_json())

# convert the object into a dict
v1_affiliates_links_bulk_post202_response_dict = v1_affiliates_links_bulk_post202_response_instance.to_dict()
# create an instance of V1AffiliatesLinksBulkPost202Response from a dict
v1_affiliates_links_bulk_post202_response_from_dict = V1AffiliatesLinksBulkPost202Response.from_dict(v1_affiliates_links_bulk_post202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


