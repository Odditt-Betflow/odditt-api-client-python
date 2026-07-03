# AuthSetCheckEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple** | **bool** | If true, the platform sends a single POST with a JSON array of all hydrated payloads. If false (default), one POST per flow is issued in parallel. | [optional] [default to False]
**auth_header_name** | **str** | HTTP header name used to carry the authentication credential. Defaults to &#39;Authorization&#39;. Common alternatives: &#39;X-API-Key&#39;, &#39;X-Auth&#39;. | [optional] 
**auth_scheme** | **str** | Prefix placed before the token in the header value. Defaults to &#39;Bearer&#39; when &#39;auth_header_name&#39; is omitted. Set to an empty string for headers that take the raw value (e.g. &#39;X-API-Key&#39;). | [optional] 
**auth_token** | **str** | Authentication credential. Stored server-side and never returned in any response. Sent as &#x60;&lt;auth_header_name&gt;: &lt;auth_scheme&gt; &lt;auth_token&gt;&#x60; (scheme omitted when empty). | 
**method** | **str** | HTTP method used when calling the endpoint. | 
**url** | **str** | Absolute URL of the check endpoint (https recommended). | 

## Example

```python
from odditt_api_client.models.auth_set_check_endpoint_request import AuthSetCheckEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSetCheckEndpointRequest from a JSON string
auth_set_check_endpoint_request_instance = AuthSetCheckEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(AuthSetCheckEndpointRequest.to_json())

# convert the object into a dict
auth_set_check_endpoint_request_dict = auth_set_check_endpoint_request_instance.to_dict()
# create an instance of AuthSetCheckEndpointRequest from a dict
auth_set_check_endpoint_request_from_dict = AuthSetCheckEndpointRequest.from_dict(auth_set_check_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


