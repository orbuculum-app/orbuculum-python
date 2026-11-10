# WorkspaceContextModalDefaultsTabs

BE-227. Per tab with double support, the context account's newest record in that tab under rule 1 (the newest typed pair of the tab, or a newer double whose outer pair is typed in it); a hidden or inaccessible counterparty is skipped. History facts: no limitation or label applies. null without account_id; an entry is null when the tab has no such record; Custom has no entry. The opening tab's entry agrees with this block unless the block nulled or demoted something, or the context account is a debt or hidden account (rule 1's exception).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expenses** | [**WorkspaceContextModalDefaultsTabsExpenses**](WorkspaceContextModalDefaultsTabsExpenses.md) |  | 
**income** | [**WorkspaceContextModalDefaultsTabsExpenses**](WorkspaceContextModalDefaultsTabsExpenses.md) |  | 
**transfer** | [**WorkspaceContextModalDefaultsTabsExpenses**](WorkspaceContextModalDefaultsTabsExpenses.md) |  | 

## Example

```python
from orbuculum_client.models.workspace_context_modal_defaults_tabs import WorkspaceContextModalDefaultsTabs

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextModalDefaultsTabs from a JSON string
workspace_context_modal_defaults_tabs_instance = WorkspaceContextModalDefaultsTabs.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextModalDefaultsTabs.to_json())

# convert the object into a dict
workspace_context_modal_defaults_tabs_dict = workspace_context_modal_defaults_tabs_instance.to_dict()
# create an instance of WorkspaceContextModalDefaultsTabs from a dict
workspace_context_modal_defaults_tabs_from_dict = WorkspaceContextModalDefaultsTabs.from_dict(workspace_context_modal_defaults_tabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


