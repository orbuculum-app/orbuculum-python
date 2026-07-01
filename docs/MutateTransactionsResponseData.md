# MutateTransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drops** | **List[int]** | Transaction ids to remove from the loaded window. | 
**upserts** | [**List[TransactionCanonicalRow]**](TransactionCanonicalRow.md) | Canonical transaction rows to insert/replace (each carries isOut). | 
**balance_updates** | [**List[BalanceUpdate]**](BalanceUpdate.md) | In-place cascade balance patches for rows whose identity did not change. | [optional] 

## Example

```python
from orbuculum_client.models.mutate_transactions_response_data import MutateTransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MutateTransactionsResponseData from a JSON string
mutate_transactions_response_data_instance = MutateTransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(MutateTransactionsResponseData.to_json())

# convert the object into a dict
mutate_transactions_response_data_dict = mutate_transactions_response_data_instance.to_dict()
# create an instance of MutateTransactionsResponseData from a dict
mutate_transactions_response_data_from_dict = MutateTransactionsResponseData.from_dict(mutate_transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


