# ToggleFullAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**value** | **bool** | true &#x3D; grant full access, false &#x3D; revoke | 

## Example

```python
from orbuculum_client.models.toggle_full_access_request import ToggleFullAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleFullAccessRequest from a JSON string
toggle_full_access_request_instance = ToggleFullAccessRequest.from_json(json)
# print the JSON string representation of the object
print(ToggleFullAccessRequest.to_json())

# convert the object into a dict
toggle_full_access_request_dict = toggle_full_access_request_instance.to_dict()
# create an instance of ToggleFullAccessRequest from a dict
toggle_full_access_request_from_dict = ToggleFullAccessRequest.from_dict(toggle_full_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


