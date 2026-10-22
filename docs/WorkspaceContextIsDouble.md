# WorkspaceContextIsDouble

Latest double-entry flags of one account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_is_double_income** | **bool** |  | 
**latest_is_double_expenses** | **bool** |  | 
**latest_is_double_transfer** | **bool** | Absent only when the account&#39;s latest transaction (highest ID) is an intermediary (chained) leg whose sender or receiver account is outside the workspace&#39;s accounts; present in every other case, including accounts without transactions. | [optional] 

## Example

```python
from orbuculum_client.models.workspace_context_is_double import WorkspaceContextIsDouble

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextIsDouble from a JSON string
workspace_context_is_double_instance = WorkspaceContextIsDouble.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextIsDouble.to_json())

# convert the object into a dict
workspace_context_is_double_dict = workspace_context_is_double_instance.to_dict()
# create an instance of WorkspaceContextIsDouble from a dict
workspace_context_is_double_from_dict = WorkspaceContextIsDouble.from_dict(workspace_context_is_double_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


