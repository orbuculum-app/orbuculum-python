# TransactionChainedTransaction

Compact view of the paired transaction in a debt-pair (the row whose `id` equals this row's `chained_id`). Null for standalone transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sender_account_id** | **int** |  | [optional] 
**receiver_account_id** | **int** |  | [optional] 
**sender_amount** | **str** | Decimal value as string to preserve precision. | [optional] 
**receiver_amount** | **str** | Decimal value as string to preserve precision. | [optional] 

## Example

```python
from orbuculum_client.models.transaction_chained_transaction import TransactionChainedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionChainedTransaction from a JSON string
transaction_chained_transaction_instance = TransactionChainedTransaction.from_json(json)
# print the JSON string representation of the object
print(TransactionChainedTransaction.to_json())

# convert the object into a dict
transaction_chained_transaction_dict = transaction_chained_transaction_instance.to_dict()
# create an instance of TransactionChainedTransaction from a dict
transaction_chained_transaction_from_dict = TransactionChainedTransaction.from_dict(transaction_chained_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


