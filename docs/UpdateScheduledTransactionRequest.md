# UpdateScheduledTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Scheduled transaction ID | 
**edit_type** | **int** | Edit type: 1&#x3D;ALL, 2&#x3D;SINGLE, 3&#x3D;THIS_AND_FUTURE | 
**trx_id** | **int** | Transaction ID (required for edit_type&#x3D;2) | [optional] 
**trx_id_2** | **int** | Second transaction ID for intermediary (edit_type&#x3D;2) | [optional] 
**override** | **bool** | Override edited transactions | [optional] 
**sender_account_id** | **int** | Sender account ID | [optional] 
**receiver_account_id** | **int** | Receiver account ID | [optional] 
**sender_amount** | **str** | Sender amount | [optional] 
**receiver_amount** | **str** | Receiver amount | [optional] 
**dt** | **datetime** | Schedule date/time. Accepted formats: \&quot;YYYY-MM-DD\&quot; (interpreted as midnight in the timezone field), \&quot;YYYY-MM-DD HH:MM:SS\&quot;, \&quot;YYYY-MM-DDTHH:MM:SS\&quot; (ISO 8601), with optional Z/offset suffix. A Z/offset suffix identifies an instant and is stored as the wall-clock of that instant in the &#x60;timezone&#x60; field; a value without a suffix is taken as a wall-clock in &#x60;timezone&#x60; directly. | [optional] 
**time** | **str** | Time | [optional] 
**timezone** | **str** | Timezone | [optional] 
**schedule_type** | **int** | Schedule type (1-8) | [optional] 
**comment** | **str** | Comment | [optional] 
**description** | **str** | Description | [optional] 
**project_id** | **int** | Project ID | [optional] 
**subtab** | **str** | BE-66: the transaction-modal sub-tab. ACCEPTED AND IGNORED on update — slot eligibility rules run on create only, and a submitted sub-tab never exempts an update from the direction floor. Edit-only sub-tabs (editing, edit_double_income, edit_double_expenses, edit_any) are rejected. | [optional] 

## Example

```python
from orbuculum_client.models.update_scheduled_transaction_request import UpdateScheduledTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduledTransactionRequest from a JSON string
update_scheduled_transaction_request_instance = UpdateScheduledTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduledTransactionRequest.to_json())

# convert the object into a dict
update_scheduled_transaction_request_dict = update_scheduled_transaction_request_instance.to_dict()
# create an instance of UpdateScheduledTransactionRequest from a dict
update_scheduled_transaction_request_from_dict = UpdateScheduledTransactionRequest.from_dict(update_scheduled_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


