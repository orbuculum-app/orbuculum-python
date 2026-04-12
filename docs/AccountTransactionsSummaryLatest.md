# AccountTransactionsSummaryLatest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **str** |  | 
**received** | **str** |  | 
**balance** | **str** |  | 

## Example

```python
from orbuculum_client.models.account_transactions_summary_latest import AccountTransactionsSummaryLatest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsSummaryLatest from a JSON string
account_transactions_summary_latest_instance = AccountTransactionsSummaryLatest.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsSummaryLatest.to_json())

# convert the object into a dict
account_transactions_summary_latest_dict = account_transactions_summary_latest_instance.to_dict()
# create an instance of AccountTransactionsSummaryLatest from a dict
account_transactions_summary_latest_from_dict = AccountTransactionsSummaryLatest.from_dict(account_transactions_summary_latest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


