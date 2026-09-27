# ScheduledTransactionCreatedResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**transaction_ids** | **List[int]** |  | 
**sender_account_id** | **int** |  | 
**receiver_account_id** | **int** |  | 
**dt** | **str** | OMM-2124: schedule date/time emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC …Z when absent/invalid). The schedule&#39;s stored wall-clock is interpreted in its own &#x60;timezone&#x60; field. | 

## Example

```python
from orbuculum_client.models.scheduled_transaction_created_response_data import ScheduledTransactionCreatedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionCreatedResponseData from a JSON string
scheduled_transaction_created_response_data_instance = ScheduledTransactionCreatedResponseData.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionCreatedResponseData.to_json())

# convert the object into a dict
scheduled_transaction_created_response_data_dict = scheduled_transaction_created_response_data_instance.to_dict()
# create an instance of ScheduledTransactionCreatedResponseData from a dict
scheduled_transaction_created_response_data_from_dict = ScheduledTransactionCreatedResponseData.from_dict(scheduled_transaction_created_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


