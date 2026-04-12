# AccountTransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[AccountTransactionItem]**](AccountTransactionItem.md) |  | 
**has_more** | **bool** |  | 
**summary** | [**AccountTransactionsSummary**](AccountTransactionsSummary.md) |  | 

## Example

```python
from orbuculum_client.models.account_transactions_response_data import AccountTransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsResponseData from a JSON string
account_transactions_response_data_instance = AccountTransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsResponseData.to_json())

# convert the object into a dict
account_transactions_response_data_dict = account_transactions_response_data_instance.to_dict()
# create an instance of AccountTransactionsResponseData from a dict
account_transactions_response_data_from_dict = AccountTransactionsResponseData.from_dict(account_transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


