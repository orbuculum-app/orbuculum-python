# AccountTransactionItemCounterparty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**account_name** | **str** |  | 
**entity_name** | **str** |  | 
**currency_code** | **str** |  | 

## Example

```python
from orbuculum_client.models.account_transaction_item_counterparty import AccountTransactionItemCounterparty

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionItemCounterparty from a JSON string
account_transaction_item_counterparty_instance = AccountTransactionItemCounterparty.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionItemCounterparty.to_json())

# convert the object into a dict
account_transaction_item_counterparty_dict = account_transaction_item_counterparty_instance.to_dict()
# create an instance of AccountTransactionItemCounterparty from a dict
account_transaction_item_counterparty_from_dict = AccountTransactionItemCounterparty.from_dict(account_transaction_item_counterparty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


