# TransactionReceiverCommission

Receiver-side commission row (a Transaction whose chained_commission_id points back to this row). Null when no receiver commission is attached.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**amount** | **str** | Commission amount. Decimal value as string to preserve precision. | [optional] 
**account_id** | **int** |  | [optional] 
**account_name** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.transaction_receiver_commission import TransactionReceiverCommission

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReceiverCommission from a JSON string
transaction_receiver_commission_instance = TransactionReceiverCommission.from_json(json)
# print the JSON string representation of the object
print(TransactionReceiverCommission.to_json())

# convert the object into a dict
transaction_receiver_commission_dict = transaction_receiver_commission_instance.to_dict()
# create an instance of TransactionReceiverCommission from a dict
transaction_receiver_commission_from_dict = TransactionReceiverCommission.from_dict(transaction_receiver_commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


