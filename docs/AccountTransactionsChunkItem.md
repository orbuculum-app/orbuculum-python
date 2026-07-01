# AccountTransactionsChunkItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dt** | **datetime** | OMM-2124: transaction date/time emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC …Z when absent/invalid). | 
**type** | **str** |  | 
**data** | [**TransactionCanonicalRow**](TransactionCanonicalRow.md) |  | 

## Example

```python
from orbuculum_client.models.account_transactions_chunk_item import AccountTransactionsChunkItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsChunkItem from a JSON string
account_transactions_chunk_item_instance = AccountTransactionsChunkItem.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsChunkItem.to_json())

# convert the object into a dict
account_transactions_chunk_item_dict = account_transactions_chunk_item_instance.to_dict()
# create an instance of AccountTransactionsChunkItem from a dict
account_transactions_chunk_item_from_dict = AccountTransactionsChunkItem.from_dict(account_transactions_chunk_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


