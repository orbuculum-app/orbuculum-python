# TransactionSchedule

Recurring schedule (Future) that generated this transaction, when applicable. Null when the transaction is not tied to a schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**future_date** | **str** | Anchor date of the schedule, emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC rendered with trailing Z when absent/invalid). | [optional] 
**dt** | **str** | BE-62: alias of &#x60;future_date&#x60; under the name POST /api/scheduled-transaction/create accepts, so a schedule object can be spread into that payload without renaming. Always byte-identical to &#x60;future_date&#x60;. | [optional] 
**schedule_type** | **str** |  | [optional] 
**schedule_interval** | **int** |  | [optional] 
**schedule_interval_type** | **str** |  | [optional] 
**schedule_interval_specific** | **str** |  | [optional] 
**schedule_end_type** | **str** |  | [optional] 
**schedule_end_specific** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**recalculation_base** | **int** | Which amount is fixed on materialisation: 1&#x3D;sender&#39;s, 2&#x3D;receiver&#39;s, 3&#x3D;intermediary, 4&#x3D;no recalculation (default). | [optional] 
**recalculate_option** | **int** | BE-62: alias of &#x60;recalculation_base&#x60; under the name POST /api/scheduled-transaction/create accepts. Always identical to &#x60;recalculation_base&#x60;. | [optional] 
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


