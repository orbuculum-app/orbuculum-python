# ActivityJournalCursorListResponseDataPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_date** | **str** | OMM-2124: offset-ISO in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Cursor mode only. | 
**last_date** | **str** | OMM-2124: offset-ISO in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Cursor mode only. | 
**total_count** | **int** |  | 
**next_cursor** | [**ActivityJournalCursorListResponseDataPaginationNextCursor**](ActivityJournalCursorListResponseDataPaginationNextCursor.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from orbuculum_client.models.activity_journal_cursor_list_response_data_pagination import ActivityJournalCursorListResponseDataPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalCursorListResponseDataPagination from a JSON string
activity_journal_cursor_list_response_data_pagination_instance = ActivityJournalCursorListResponseDataPagination.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalCursorListResponseDataPagination.to_json())

# convert the object into a dict
activity_journal_cursor_list_response_data_pagination_dict = activity_journal_cursor_list_response_data_pagination_instance.to_dict()
# create an instance of ActivityJournalCursorListResponseDataPagination from a dict
activity_journal_cursor_list_response_data_pagination_from_dict = ActivityJournalCursorListResponseDataPagination.from_dict(activity_journal_cursor_list_response_data_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


