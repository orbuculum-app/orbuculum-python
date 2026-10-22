# TransactionListDiff

Window diff of a single save relative to the client's loaded list (`list_scope`) — the same diff POST /api/transaction/mutate returns in `data` for the same change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drops** | **List[int]** | Transaction ids to remove from the loaded window. | 
**upserts** | [**List[TransactionCanonicalRow]**](TransactionCanonicalRow.md) | Canonical transaction rows to insert/replace (each carries isOut). | 
**balance_updates** | [**List[BalanceUpdate]**](BalanceUpdate.md) | In-place cascade balance patches for rows whose identity did not change. | 
**summary** | [**AccountTransactionsSummary**](AccountTransactionsSummary.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.transaction_list_diff import TransactionListDiff

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionListDiff from a JSON string
transaction_list_diff_instance = TransactionListDiff.from_json(json)
# print the JSON string representation of the object
print(TransactionListDiff.to_json())

# convert the object into a dict
transaction_list_diff_dict = transaction_list_diff_instance.to_dict()
# create an instance of TransactionListDiff from a dict
transaction_list_diff_from_dict = TransactionListDiff.from_dict(transaction_list_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


