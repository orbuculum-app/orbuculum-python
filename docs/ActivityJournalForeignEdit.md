# ActivityJournalForeignEdit

An edit or delete of a record through another channel or client than the one that created it. Present only on `foreign_edit` rows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | BE-299: the structured payload of a &#x60;foreign_edit&#x60; journal event | 
**creator** | [**ActivityJournalForeignEditCreator**](ActivityJournalForeignEditCreator.md) |  | 
**editor** | [**ActivityJournalForeignEditEditor**](ActivityJournalForeignEditEditor.md) |  | 
**before** | **Dict[str, object]** | The changed fields before the edit. On &#x60;operation: delete&#x60;, every non-null business column of the deleted row. On a note, &#x60;description&#x60; holds its actual balance, so its value is always null here and in &#x60;after&#x60;: the key names the change. | 
**after** | **Dict[str, object]** | The changed fields after the edit. Null on &#x60;operation: delete&#x60;. | [optional] 

## Example

```python
from orbuculum_client.models.activity_journal_foreign_edit import ActivityJournalForeignEdit

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalForeignEdit from a JSON string
activity_journal_foreign_edit_instance = ActivityJournalForeignEdit.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalForeignEdit.to_json())

# convert the object into a dict
activity_journal_foreign_edit_dict = activity_journal_foreign_edit_instance.to_dict()
# create an instance of ActivityJournalForeignEdit from a dict
activity_journal_foreign_edit_from_dict = ActivityJournalForeignEdit.from_dict(activity_journal_foreign_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


