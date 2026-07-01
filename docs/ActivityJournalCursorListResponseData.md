# ActivityJournalCursorListResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk** | [**List[ActivityJournalCursorListResponseDataChunkInner]**](ActivityJournalCursorListResponseDataChunkInner.md) |  | 
**pagination** | [**ActivityJournalCursorListResponseDataPagination**](ActivityJournalCursorListResponseDataPagination.md) |  | 

## Example

```python
from orbuculum_client.models.activity_journal_cursor_list_response_data import ActivityJournalCursorListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalCursorListResponseData from a JSON string
activity_journal_cursor_list_response_data_instance = ActivityJournalCursorListResponseData.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalCursorListResponseData.to_json())

# convert the object into a dict
activity_journal_cursor_list_response_data_dict = activity_journal_cursor_list_response_data_instance.to_dict()
# create an instance of ActivityJournalCursorListResponseData from a dict
activity_journal_cursor_list_response_data_from_dict = ActivityJournalCursorListResponseData.from_dict(activity_journal_cursor_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


