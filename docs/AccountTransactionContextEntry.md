# AccountTransactionContextEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** |  | 
**entity_name** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.account_transaction_context_entry import AccountTransactionContextEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionContextEntry from a JSON string
account_transaction_context_entry_instance = AccountTransactionContextEntry.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionContextEntry.to_json())

# convert the object into a dict
account_transaction_context_entry_dict = account_transaction_context_entry_instance.to_dict()
# create an instance of AccountTransactionContextEntry from a dict
account_transaction_context_entry_from_dict = AccountTransactionContextEntry.from_dict(account_transaction_context_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


