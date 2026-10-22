# WorkspaceContextModalDefaultsSuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** |  | 
**account_id** | **int** |  | 
**auto_fill** | **bool** |  | 

## Example

```python
from orbuculum_client.models.workspace_context_modal_defaults_suggestion import WorkspaceContextModalDefaultsSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextModalDefaultsSuggestion from a JSON string
workspace_context_modal_defaults_suggestion_instance = WorkspaceContextModalDefaultsSuggestion.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextModalDefaultsSuggestion.to_json())

# convert the object into a dict
workspace_context_modal_defaults_suggestion_dict = workspace_context_modal_defaults_suggestion_instance.to_dict()
# create an instance of WorkspaceContextModalDefaultsSuggestion from a dict
workspace_context_modal_defaults_suggestion_from_dict = WorkspaceContextModalDefaultsSuggestion.from_dict(workspace_context_modal_defaults_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


