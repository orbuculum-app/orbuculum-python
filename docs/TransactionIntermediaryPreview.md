# TransactionIntermediaryPreview

Dry-run preview response for intermediary transaction create. Both legs computed; no DB writes performed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code (always 200 for preview). | 
**data** | [**TransactionIntermediaryPreviewData**](TransactionIntermediaryPreviewData.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_intermediary_preview import TransactionIntermediaryPreview

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionIntermediaryPreview from a JSON string
transaction_intermediary_preview_instance = TransactionIntermediaryPreview.from_json(json)
# print the JSON string representation of the object
print(TransactionIntermediaryPreview.to_json())

# convert the object into a dict
transaction_intermediary_preview_dict = transaction_intermediary_preview_instance.to_dict()
# create an instance of TransactionIntermediaryPreview from a dict
transaction_intermediary_preview_from_dict = TransactionIntermediaryPreview.from_dict(transaction_intermediary_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


