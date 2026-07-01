# ActivityJournalCursorListResponseDataChunkInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dt** | **str** | OMM-2124: entry timestamp emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Cursor mode only. | 
**type** | **str** |  | 
**data** | [**ActivityJournalCursorListResponseDataChunkInnerData**](ActivityJournalCursorListResponseDataChunkInnerData.md) |  | 

## Example

```python
from orbuculum_client.models.activity_journal_cursor_list_response_data_chunk_inner import ActivityJournalCursorListResponseDataChunkInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalCursorListResponseDataChunkInner from a JSON string
activity_journal_cursor_list_response_data_chunk_inner_instance = ActivityJournalCursorListResponseDataChunkInner.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalCursorListResponseDataChunkInner.to_json())

# convert the object into a dict
activity_journal_cursor_list_response_data_chunk_inner_dict = activity_journal_cursor_list_response_data_chunk_inner_instance.to_dict()
# create an instance of ActivityJournalCursorListResponseDataChunkInner from a dict
activity_journal_cursor_list_response_data_chunk_inner_from_dict = ActivityJournalCursorListResponseDataChunkInner.from_dict(activity_journal_cursor_list_response_data_chunk_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


