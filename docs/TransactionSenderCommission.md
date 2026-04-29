# TransactionSenderCommission

Sender-side commission row (a Transaction whose chained_commission_id points back to this row). Null when no sender commission is attached. In dry-run previews this carries the computed amounts but the `id` is null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**amount** | **str** | Commission amount. Decimal value as string to preserve precision. | [optional] 
**account_id** | **int** |  | [optional] 
**account_name** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.transaction_sender_commission import TransactionSenderCommission

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSenderCommission from a JSON string
transaction_sender_commission_instance = TransactionSenderCommission.from_json(json)
# print the JSON string representation of the object
print(TransactionSenderCommission.to_json())

# convert the object into a dict
transaction_sender_commission_dict = transaction_sender_commission_instance.to_dict()
# create an instance of TransactionSenderCommission from a dict
transaction_sender_commission_from_dict = TransactionSenderCommission.from_dict(transaction_sender_commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


