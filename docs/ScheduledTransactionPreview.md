# ScheduledTransactionPreview

BE-102: dry-run preview for POST /api/scheduled-transaction/create (dry_run=true). Every check of a real create ran; nothing was written.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code (always 200 for a preview). | 
**data** | [**ScheduledTransactionPreviewData**](ScheduledTransactionPreviewData.md) |  | 

## Example

```python
from orbuculum_client.models.scheduled_transaction_preview import ScheduledTransactionPreview

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionPreview from a JSON string
scheduled_transaction_preview_instance = ScheduledTransactionPreview.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionPreview.to_json())

# convert the object into a dict
scheduled_transaction_preview_dict = scheduled_transaction_preview_instance.to_dict()
# create an instance of ScheduledTransactionPreview from a dict
scheduled_transaction_preview_from_dict = ScheduledTransactionPreview.from_dict(scheduled_transaction_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


