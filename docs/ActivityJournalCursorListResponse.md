# ActivityJournalCursorListResponse

Cursor-paginated activity journal entries (chunk envelope for Frontend 2.0 infinite scroll).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Activity Journal cursor-mode (chunk envelope) list response schema | 
**data** | [**ActivityJournalCursorListResponseData**](ActivityJournalCursorListResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.activity_journal_cursor_list_response import ActivityJournalCursorListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalCursorListResponse from a JSON string
activity_journal_cursor_list_response_instance = ActivityJournalCursorListResponse.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalCursorListResponse.to_json())

# convert the object into a dict
activity_journal_cursor_list_response_dict = activity_journal_cursor_list_response_instance.to_dict()
# create an instance of ActivityJournalCursorListResponse from a dict
activity_journal_cursor_list_response_from_dict = ActivityJournalCursorListResponse.from_dict(activity_journal_cursor_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


