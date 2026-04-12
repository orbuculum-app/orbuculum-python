# AccountTransactionsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**precision** | **int** |  | 
**show_balance** | **bool** |  | 
**recent** | [**AccountTransactionsSummaryRecent**](AccountTransactionsSummaryRecent.md) |  | [optional] 
**latest** | [**AccountTransactionsSummaryLatest**](AccountTransactionsSummaryLatest.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.account_transactions_summary import AccountTransactionsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsSummary from a JSON string
account_transactions_summary_instance = AccountTransactionsSummary.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsSummary.to_json())

# convert the object into a dict
account_transactions_summary_dict = account_transactions_summary_instance.to_dict()
# create an instance of AccountTransactionsSummary from a dict
account_transactions_summary_from_dict = AccountTransactionsSummary.from_dict(account_transactions_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


