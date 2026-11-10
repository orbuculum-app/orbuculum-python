# ActivityJournalForeignEditCreator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**client** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.activity_journal_foreign_edit_creator import ActivityJournalForeignEditCreator

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalForeignEditCreator from a JSON string
activity_journal_foreign_edit_creator_instance = ActivityJournalForeignEditCreator.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalForeignEditCreator.to_json())

# convert the object into a dict
activity_journal_foreign_edit_creator_dict = activity_journal_foreign_edit_creator_instance.to_dict()
# create an instance of ActivityJournalForeignEditCreator from a dict
activity_journal_foreign_edit_creator_from_dict = ActivityJournalForeignEditCreator.from_dict(activity_journal_foreign_edit_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


