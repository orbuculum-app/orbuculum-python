# ScheduledTransactionPreviewData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | **bool** | Always true — identifies a dry-run preview. | 
**dates** | **List[datetime]** | Occurrence instants the real create would generate as transactions, in order, as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Empty for schedule_type&#x3D;1 (once). | 
**count** | **int** | Number of elements in dates. | 

## Example

```python
from orbuculum_client.models.scheduled_transaction_preview_data import ScheduledTransactionPreviewData

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionPreviewData from a JSON string
scheduled_transaction_preview_data_instance = ScheduledTransactionPreviewData.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionPreviewData.to_json())

# convert the object into a dict
scheduled_transaction_preview_data_dict = scheduled_transaction_preview_data_instance.to_dict()
# create an instance of ScheduledTransactionPreviewData from a dict
scheduled_transaction_preview_data_from_dict = ScheduledTransactionPreviewData.from_dict(scheduled_transaction_preview_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


