# UpdateLabelTabRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**label_id** | **int** | Label ID to configure | 
**accounts** | **Dict[str, int]** | Map account_id → access_level (1&#x3D;none, 2&#x3D;read, 3&#x3D;manage) | 

## Example

```python
from orbuculum_client.models.update_label_tab_request import UpdateLabelTabRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLabelTabRequest from a JSON string
update_label_tab_request_instance = UpdateLabelTabRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateLabelTabRequest.to_json())

# convert the object into a dict
update_label_tab_request_dict = update_label_tab_request_instance.to_dict()
# create an instance of UpdateLabelTabRequest from a dict
update_label_tab_request_from_dict = UpdateLabelTabRequest.from_dict(update_label_tab_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


