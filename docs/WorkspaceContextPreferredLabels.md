# WorkspaceContextPreferredLabels

Label IDs grouped by Add-modal tab, most recently used first; empty groups are omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expenses** | **List[int]** |  | [optional] 
**income** | **List[int]** |  | [optional] 
**transfer** | **List[int]** |  | [optional] 
**any** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_context_preferred_labels import WorkspaceContextPreferredLabels

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextPreferredLabels from a JSON string
workspace_context_preferred_labels_instance = WorkspaceContextPreferredLabels.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextPreferredLabels.to_json())

# convert the object into a dict
workspace_context_preferred_labels_dict = workspace_context_preferred_labels_instance.to_dict()
# create an instance of WorkspaceContextPreferredLabels from a dict
workspace_context_preferred_labels_from_dict = WorkspaceContextPreferredLabels.from_dict(workspace_context_preferred_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


