# ActivityJournalList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Activity Journal cursor-mode (chunk envelope) list response schema | 
**data** | [**ActivityJournalCursorListResponseData**](ActivityJournalCursorListResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.activity_journal_list200_response import ActivityJournalList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalList200Response from a JSON string
activity_journal_list200_response_instance = ActivityJournalList200Response.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalList200Response.to_json())

# convert the object into a dict
activity_journal_list200_response_dict = activity_journal_list200_response_instance.to_dict()
# create an instance of ActivityJournalList200Response from a dict
activity_journal_list200_response_from_dict = ActivityJournalList200Response.from_dict(activity_journal_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


