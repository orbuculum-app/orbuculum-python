# ChangeSetUndoConflictDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**model_type** | **str** |  | [optional] 
**model_id** | **int** |  | [optional] 
**later_change_set_ids** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.change_set_undo_conflict_details_inner import ChangeSetUndoConflictDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeSetUndoConflictDetailsInner from a JSON string
change_set_undo_conflict_details_inner_instance = ChangeSetUndoConflictDetailsInner.from_json(json)
# print the JSON string representation of the object
print(ChangeSetUndoConflictDetailsInner.to_json())

# convert the object into a dict
change_set_undo_conflict_details_inner_dict = change_set_undo_conflict_details_inner_instance.to_dict()
# create an instance of ChangeSetUndoConflictDetailsInner from a dict
change_set_undo_conflict_details_inner_from_dict = ChangeSetUndoConflictDetailsInner.from_dict(change_set_undo_conflict_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


