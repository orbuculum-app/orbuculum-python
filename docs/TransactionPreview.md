# TransactionPreview

Dry-run preview response for non-intermediary transaction create. No DB writes performed. `data` carries the full Transaction shape with `preview: true`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code (always 200 for preview). | 
**data** | [**TransactionPreviewData**](TransactionPreviewData.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_preview import TransactionPreview

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPreview from a JSON string
transaction_preview_instance = TransactionPreview.from_json(json)
# print the JSON string representation of the object
print(TransactionPreview.to_json())

# convert the object into a dict
transaction_preview_dict = transaction_preview_instance.to_dict()
# create an instance of TransactionPreview from a dict
transaction_preview_from_dict = TransactionPreview.from_dict(transaction_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


