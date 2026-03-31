# ActivityJournalAuthorsResponse

List of workspace users who can be activity authors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | [optional] 
**data** | [**ActivityJournalAuthorsResponseData**](ActivityJournalAuthorsResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.activity_journal_authors_response import ActivityJournalAuthorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalAuthorsResponse from a JSON string
activity_journal_authors_response_instance = ActivityJournalAuthorsResponse.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalAuthorsResponse.to_json())

# convert the object into a dict
activity_journal_authors_response_dict = activity_journal_authors_response_instance.to_dict()
# create an instance of ActivityJournalAuthorsResponse from a dict
activity_journal_authors_response_from_dict = ActivityJournalAuthorsResponse.from_dict(activity_journal_authors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


