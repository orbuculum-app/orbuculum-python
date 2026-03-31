# ToggleFlagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**permission** | **str** | Permission identifier | 
**value** | **bool** | true &#x3D; grant, false &#x3D; revoke | 

## Example

```python
from orbuculum_client.models.toggle_flag_request import ToggleFlagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleFlagRequest from a JSON string
toggle_flag_request_instance = ToggleFlagRequest.from_json(json)
# print the JSON string representation of the object
print(ToggleFlagRequest.to_json())

# convert the object into a dict
toggle_flag_request_dict = toggle_flag_request_instance.to_dict()
# create an instance of ToggleFlagRequest from a dict
toggle_flag_request_from_dict = ToggleFlagRequest.from_dict(toggle_flag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


