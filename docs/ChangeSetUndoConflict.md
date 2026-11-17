# ChangeSetUndoConflict

Undo refused. For a proposed or already-undone set, or a restored row that conflicts with the current book, details is empty or carries only a message; for a conflict report each element names a row and the later change sets that touched it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**error** | **str** | Why the undo was refused | 
**details** | [**List[ChangeSetUndoConflictDetailsInner]**](ChangeSetUndoConflictDetailsInner.md) |  | 

## Example

```python
from orbuculum_client.models.change_set_undo_conflict import ChangeSetUndoConflict

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeSetUndoConflict from a JSON string
change_set_undo_conflict_instance = ChangeSetUndoConflict.from_json(json)
# print the JSON string representation of the object
print(ChangeSetUndoConflict.to_json())

# convert the object into a dict
change_set_undo_conflict_dict = change_set_undo_conflict_instance.to_dict()
# create an instance of ChangeSetUndoConflict from a dict
change_set_undo_conflict_from_dict = ChangeSetUndoConflict.from_dict(change_set_undo_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


