# WorkspaceContextModalDefaults

The Add-modal's opening state, computed server-side

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtab** | **str** |  | 
**double** | **bool** |  | 
**double_available** | **bool** |  | 
**sender_id** | **int** |  | 
**receiver_id** | **int** |  | 
**intermediary_id** | **int** |  | 
**suggestion** | [**WorkspaceContextModalDefaultsSuggestion**](WorkspaceContextModalDefaultsSuggestion.md) |  | 
**label_id** | **int** |  | 
**visible_subtabs** | **List[str]** |  | 

## Example

```python
from orbuculum_client.models.workspace_context_modal_defaults import WorkspaceContextModalDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextModalDefaults from a JSON string
workspace_context_modal_defaults_instance = WorkspaceContextModalDefaults.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextModalDefaults.to_json())

# convert the object into a dict
workspace_context_modal_defaults_dict = workspace_context_modal_defaults_instance.to_dict()
# create an instance of WorkspaceContextModalDefaults from a dict
workspace_context_modal_defaults_from_dict = WorkspaceContextModalDefaults.from_dict(workspace_context_modal_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


