# AccountTransactionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dt** | **str** |  | 
**sender_account_id** | **int** |  | 
**receiver_account_id** | **int** |  | 
**sender_amount** | **str** |  | 
**receiver_amount** | **str** |  | 
**comment** | **str** |  | [optional] 
**label_id** | **int** |  | [optional] 
**done** | **bool** |  | 
**is_future** | **bool** |  | 
**balance_after** | **str** |  | [optional] 
**counterparty** | [**AccountTransactionItemCounterparty**](AccountTransactionItemCounterparty.md) |  | [optional] 
**chained_id** | **int** |  | [optional] 
**chained_commission_id** | **int** |  | [optional] 
**future_id** | **int** |  | [optional] 
**editable** | **bool** |  | 

## Example

```python
from orbuculum_client.models.account_transaction_item import AccountTransactionItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionItem from a JSON string
account_transaction_item_instance = AccountTransactionItem.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionItem.to_json())

# convert the object into a dict
account_transaction_item_dict = account_transaction_item_instance.to_dict()
# create an instance of AccountTransactionItem from a dict
account_transaction_item_from_dict = AccountTransactionItem.from_dict(account_transaction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


