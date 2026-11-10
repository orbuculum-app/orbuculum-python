# WorkspaceContextModalDefaults

The Add-modal's opening state, computed server-side. With an account context (account_id) in typed mode three rules hold (BE-220). 1. The tab comes from the context account's newest typed record — an expense, income or transfer pair — and the anchor transaction is that pair's newest transaction or a newer double whose outer pair is an operation of the same tab; the sub-tab follows the anchor. A debt, repayment, debt-transfer, commission or service record, or a double's untyped leg, never becomes the anchor. A debt context account, or a hidden one, is the exception (BE-346): it takes the side it acted on last (sender when its last send is not older than its last receipt, else receiver); its anchor is the newest pair on that side with a visible counterparty among expense, income, transfer, repayment and debt-transfer records; the tab is that record's operation tab, the sub-tab is the tab's first base sub-tab admitting the pair, and no double is promoted from it. With no such pair the first base sub-tab of visible_subtabs, in Expenses, Income, Transfer order, whose sender or receiver class admits the account opens with the account in that slot and no counterparty. 2. The context account keeps its slot of the returned sub-tab: a limitation that fails the pair under the returned label drops the counterparty, never the context account, and does not move label_id. A hidden context account the caller can access keeps its slot like a visible one, takes its anchor by rule 1's exception, and visible_subtabs counts it (BE-346); a hidden counterparty is never returned. 3. A counterparty that survives is returned filled: its side's id is set and suggestion.auto_fill is true. Without an account context in typed mode the anchor is the caller's own last Add-modal save (BE-226): its tab, both outer sides and a double's middle account are returned as saved, whatever its operation date and whoever added newer rows; when that transaction no longer exists, one of its outer sides is hidden or its outer pair is not an expense, income or transfer, the workspace's newest typed pair decides as before. With an account context, no label_id in the request and a placed context account, label_id switches automatically (BE-226) when no visible account of the returned sub-tab's free side is manageable under the cascade's label but all of them and the context account are manageable under a common label: label_id becomes the context account's most recently used label for the sub-tab's tab among those common labels, else the first common label, and the counterparty is resolved under it.

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
**tabs** | [**WorkspaceContextModalDefaultsTabs**](WorkspaceContextModalDefaultsTabs.md) |  | 

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


