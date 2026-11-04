# ScheduledTransactionEditedOccurrencesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of hand-edited occurrences in the scope; 0 means the overwrite question need not be asked | 
**transaction_ids** | **List[int]** | One id per hand-edited occurrence (its main row), in date order | 

## Example

```python
from orbuculum_client.models.scheduled_transaction_edited_occurrences_response_data import ScheduledTransactionEditedOccurrencesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionEditedOccurrencesResponseData from a JSON string
scheduled_transaction_edited_occurrences_response_data_instance = ScheduledTransactionEditedOccurrencesResponseData.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionEditedOccurrencesResponseData.to_json())

# convert the object into a dict
scheduled_transaction_edited_occurrences_response_data_dict = scheduled_transaction_edited_occurrences_response_data_instance.to_dict()
# create an instance of ScheduledTransactionEditedOccurrencesResponseData from a dict
scheduled_transaction_edited_occurrences_response_data_from_dict = ScheduledTransactionEditedOccurrencesResponseData.from_dict(scheduled_transaction_edited_occurrences_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


