# TransactionSchedule

Recurring schedule (Future) that generated this transaction, when applicable. Null when the transaction is not tied to a schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**future_date** | **str** | Anchor date of the schedule (Y-m-d H:i:s). | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_interval** | **int** |  | [optional] 
**schedule_interval_type** | **str** |  | [optional] 
**schedule_interval_specific** | **str** |  | [optional] 
**schedule_end_type** | **str** |  | [optional] 
**schedule_end_specific** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**recalculation_base** | **str** |  | [optional] 
**next_date** | **str** | Next scheduled occurrence (Y-m-d). | [optional] 

## Example

```python
from orbuculum_client.models.transaction_schedule import TransactionSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchedule from a JSON string
transaction_schedule_instance = TransactionSchedule.from_json(json)
# print the JSON string representation of the object
print(TransactionSchedule.to_json())

# convert the object into a dict
transaction_schedule_dict = transaction_schedule_instance.to_dict()
# create an instance of TransactionSchedule from a dict
transaction_schedule_from_dict = TransactionSchedule.from_dict(transaction_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


