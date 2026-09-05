# GetWorkspaceContext200ResponseDataModalDefaults

BE-58: the Add-modal's opening state, computed server-side. Null in edit mode (when `id` is passed), when no candidate subtab is visible under the returned label, or when the block cannot be computed. Keys: subtab (string, the RESOLVED subtab over the twelve semantic subtabs — a double variant exactly when double is true, custom when Custom; always a member of visible_subtabs), double (bool), double_available (bool), sender_id (int|null), receiver_id (int|null), intermediary_id (int|null), suggestion ({side, account_id, auto_fill}|null — null whenever no counterparty is returned, including a neutral open), label_id (int|null), visible_subtabs (string[], the subset of the twelve candidates with at least one valid pair — or triple, for the double variants — in fixed DOM order; never empty).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtab** | **str** |  | [optional] 
**double** | **bool** |  | [optional] 
**double_available** | **bool** |  | [optional] 
**sender_id** | **int** |  | [optional] 
**receiver_id** | **int** |  | [optional] 
**intermediary_id** | **int** |  | [optional] 
**suggestion** | [**GetWorkspaceContext200ResponseDataModalDefaultsSuggestion**](GetWorkspaceContext200ResponseDataModalDefaultsSuggestion.md) |  | [optional] 
**label_id** | **int** |  | [optional] 
**visible_subtabs** | **List[str]** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_workspace_context200_response_data_modal_defaults import GetWorkspaceContext200ResponseDataModalDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspaceContext200ResponseDataModalDefaults from a JSON string
get_workspace_context200_response_data_modal_defaults_instance = GetWorkspaceContext200ResponseDataModalDefaults.from_json(json)
# print the JSON string representation of the object
print(GetWorkspaceContext200ResponseDataModalDefaults.to_json())

# convert the object into a dict
get_workspace_context200_response_data_modal_defaults_dict = get_workspace_context200_response_data_modal_defaults_instance.to_dict()
# create an instance of GetWorkspaceContext200ResponseDataModalDefaults from a dict
get_workspace_context200_response_data_modal_defaults_from_dict = GetWorkspaceContext200ResponseDataModalDefaults.from_dict(get_workspace_context200_response_data_modal_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


