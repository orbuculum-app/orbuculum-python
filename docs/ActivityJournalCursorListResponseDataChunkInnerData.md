# ActivityJournalCursorListResponseDataChunkInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dt** | **str** | OMM-2124: entry timestamp emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Cursor mode only. | 
**description** | **str** |  | [optional] 
**type_author** | **str** |  | [optional] 
**author_id** | **int** |  | [optional] 
**author_name** | **str** |  | [optional] 
**device** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**type_action** | **str** |  | [optional] 
**amount_impact** | **str** |  | [optional] 
**type_model** | **str** |  | [optional] 
**model_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.activity_journal_cursor_list_response_data_chunk_inner_data import ActivityJournalCursorListResponseDataChunkInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalCursorListResponseDataChunkInnerData from a JSON string
activity_journal_cursor_list_response_data_chunk_inner_data_instance = ActivityJournalCursorListResponseDataChunkInnerData.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalCursorListResponseDataChunkInnerData.to_json())

# convert the object into a dict
activity_journal_cursor_list_response_data_chunk_inner_data_dict = activity_journal_cursor_list_response_data_chunk_inner_data_instance.to_dict()
# create an instance of ActivityJournalCursorListResponseDataChunkInnerData from a dict
activity_journal_cursor_list_response_data_chunk_inner_data_from_dict = ActivityJournalCursorListResponseDataChunkInnerData.from_dict(activity_journal_cursor_list_response_data_chunk_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


