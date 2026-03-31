# ActivityJournalAuthorsResponseDataAuthorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**user_name** | **str** | User display name | [optional] 
**user_email** | **str** | User email address | [optional] 

## Example

```python
from orbuculum_client.models.activity_journal_authors_response_data_authors_inner import ActivityJournalAuthorsResponseDataAuthorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalAuthorsResponseDataAuthorsInner from a JSON string
activity_journal_authors_response_data_authors_inner_instance = ActivityJournalAuthorsResponseDataAuthorsInner.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalAuthorsResponseDataAuthorsInner.to_json())

# convert the object into a dict
activity_journal_authors_response_data_authors_inner_dict = activity_journal_authors_response_data_authors_inner_instance.to_dict()
# create an instance of ActivityJournalAuthorsResponseDataAuthorsInner from a dict
activity_journal_authors_response_data_authors_inner_from_dict = ActivityJournalAuthorsResponseDataAuthorsInner.from_dict(activity_journal_authors_response_data_authors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


