# ActivityJournalCursorListResponseDataPaginationNextCursor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **str** | OMM-2124: offset-ISO in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Pass back verbatim as the cursor_dt query param. Cursor mode only. | 
**id** | **int** |  | 

## Example

```python
from orbuculum_client.models.activity_journal_cursor_list_response_data_pagination_next_cursor import ActivityJournalCursorListResponseDataPaginationNextCursor

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalCursorListResponseDataPaginationNextCursor from a JSON string
activity_journal_cursor_list_response_data_pagination_next_cursor_instance = ActivityJournalCursorListResponseDataPaginationNextCursor.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalCursorListResponseDataPaginationNextCursor.to_json())

# convert the object into a dict
activity_journal_cursor_list_response_data_pagination_next_cursor_dict = activity_journal_cursor_list_response_data_pagination_next_cursor_instance.to_dict()
# create an instance of ActivityJournalCursorListResponseDataPaginationNextCursor from a dict
activity_journal_cursor_list_response_data_pagination_next_cursor_from_dict = ActivityJournalCursorListResponseDataPaginationNextCursor.from_dict(activity_journal_cursor_list_response_data_pagination_next_cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


