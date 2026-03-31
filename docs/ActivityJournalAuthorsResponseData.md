# ActivityJournalAuthorsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authors** | [**List[ActivityJournalAuthorsResponseDataAuthorsInner]**](ActivityJournalAuthorsResponseDataAuthorsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.activity_journal_authors_response_data import ActivityJournalAuthorsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalAuthorsResponseData from a JSON string
activity_journal_authors_response_data_instance = ActivityJournalAuthorsResponseData.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalAuthorsResponseData.to_json())

# convert the object into a dict
activity_journal_authors_response_data_dict = activity_journal_authors_response_data_instance.to_dict()
# create an instance of ActivityJournalAuthorsResponseData from a dict
activity_journal_authors_response_data_from_dict = ActivityJournalAuthorsResponseData.from_dict(activity_journal_authors_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


