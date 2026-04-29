# IntermediaryTransactionCreatedDataSchedule

Schedule object (same shape as Transaction.schedule).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**future_date** | **str** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_interval** | **int** |  | [optional] 
**schedule_interval_type** | **str** |  | [optional] 
**schedule_interval_specific** | **str** |  | [optional] 
**schedule_end_type** | **str** |  | [optional] 
**schedule_end_specific** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**recalculation_base** | **str** |  | [optional] 
**next_date** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.intermediary_transaction_created_data_schedule import IntermediaryTransactionCreatedDataSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediaryTransactionCreatedDataSchedule from a JSON string
intermediary_transaction_created_data_schedule_instance = IntermediaryTransactionCreatedDataSchedule.from_json(json)
# print the JSON string representation of the object
print(IntermediaryTransactionCreatedDataSchedule.to_json())

# convert the object into a dict
intermediary_transaction_created_data_schedule_dict = intermediary_transaction_created_data_schedule_instance.to_dict()
# create an instance of IntermediaryTransactionCreatedDataSchedule from a dict
intermediary_transaction_created_data_schedule_from_dict = IntermediaryTransactionCreatedDataSchedule.from_dict(intermediary_transaction_created_data_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


