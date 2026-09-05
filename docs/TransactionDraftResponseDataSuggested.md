# TransactionDraftResponseDataSuggested

The counterparty the modal offers for the side left free, and whether it is pre-filled. Null when there is no suggestion, and always null in edit mode. Wire consequence of the caller-drives-slots rule: non-null only when the request leaves sub-tab and all slots empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** |  | 
**account_id** | **int** |  | 
**auto_fill** | **bool** |  | 

## Example

```python
from orbuculum_client.models.transaction_draft_response_data_suggested import TransactionDraftResponseDataSuggested

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftResponseDataSuggested from a JSON string
transaction_draft_response_data_suggested_instance = TransactionDraftResponseDataSuggested.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftResponseDataSuggested.to_json())

# convert the object into a dict
transaction_draft_response_data_suggested_dict = transaction_draft_response_data_suggested_instance.to_dict()
# create an instance of TransactionDraftResponseDataSuggested from a dict
transaction_draft_response_data_suggested_from_dict = TransactionDraftResponseDataSuggested.from_dict(transaction_draft_response_data_suggested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


