# WorkspaceContextModalDefaultsTabsExpenses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**double** | **bool** |  | 
**intermediary_id** | **int** | the middle account of a double; null for a single | 
**counterparty_id** | **int** | the record&#39;s other outer end (for a double: the outer end that is not the context account) | 

## Example

```python
from orbuculum_client.models.workspace_context_modal_defaults_tabs_expenses import WorkspaceContextModalDefaultsTabsExpenses

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextModalDefaultsTabsExpenses from a JSON string
workspace_context_modal_defaults_tabs_expenses_instance = WorkspaceContextModalDefaultsTabsExpenses.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextModalDefaultsTabsExpenses.to_json())

# convert the object into a dict
workspace_context_modal_defaults_tabs_expenses_dict = workspace_context_modal_defaults_tabs_expenses_instance.to_dict()
# create an instance of WorkspaceContextModalDefaultsTabsExpenses from a dict
workspace_context_modal_defaults_tabs_expenses_from_dict = WorkspaceContextModalDefaultsTabsExpenses.from_dict(workspace_context_modal_defaults_tabs_expenses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


