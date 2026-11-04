# ScheduledTransactionEditedOccurrencesResponse

Response of GET /api/scheduled-transaction/edited-occurrences (BE-229).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response of GET /api/scheduled-transaction/edited-occurrences (HTTP 200).  BE-229: the hand-edited occurrences an update of the series with override&#x3D;false keeps, one id per occurrence (its main row). | 
**data** | [**ScheduledTransactionEditedOccurrencesResponseData**](ScheduledTransactionEditedOccurrencesResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.scheduled_transaction_edited_occurrences_response import ScheduledTransactionEditedOccurrencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionEditedOccurrencesResponse from a JSON string
scheduled_transaction_edited_occurrences_response_instance = ScheduledTransactionEditedOccurrencesResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionEditedOccurrencesResponse.to_json())

# convert the object into a dict
scheduled_transaction_edited_occurrences_response_dict = scheduled_transaction_edited_occurrences_response_instance.to_dict()
# create an instance of ScheduledTransactionEditedOccurrencesResponse from a dict
scheduled_transaction_edited_occurrences_response_from_dict = ScheduledTransactionEditedOccurrencesResponse.from_dict(scheduled_transaction_edited_occurrences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


