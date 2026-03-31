# ActivityJournalListResponse

Paginated list of activity journal entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**ActivityJournalListResponseData**](ActivityJournalListResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.activity_journal_list_response import ActivityJournalListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalListResponse from a JSON string
activity_journal_list_response_instance = ActivityJournalListResponse.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalListResponse.to_json())

# convert the object into a dict
activity_journal_list_response_dict = activity_journal_list_response_instance.to_dict()
# create an instance of ActivityJournalListResponse from a dict
activity_journal_list_response_from_dict = ActivityJournalListResponse.from_dict(activity_journal_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


