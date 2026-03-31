# ActivityJournalListResponseData

Response data with items and pagination metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ActivityJournalListResponseDataItemsInner]**](ActivityJournalListResponseDataItemsInner.md) | Array of activity journal entries | 
**total_count** | **int** | Total number of entries matching filters | 
**page** | **int** | Current page number | 
**per_page** | **int** | Items per page | 
**total_pages** | **int** | Total number of pages | 

## Example

```python
from orbuculum_client.models.activity_journal_list_response_data import ActivityJournalListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalListResponseData from a JSON string
activity_journal_list_response_data_instance = ActivityJournalListResponseData.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalListResponseData.to_json())

# convert the object into a dict
activity_journal_list_response_data_dict = activity_journal_list_response_data_instance.to_dict()
# create an instance of ActivityJournalListResponseData from a dict
activity_journal_list_response_data_from_dict = ActivityJournalListResponseData.from_dict(activity_journal_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


