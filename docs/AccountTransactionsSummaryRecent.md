# AccountTransactionsSummaryRecent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **str** |  | 
**received** | **str** |  | 
**balance** | **str** |  | 

## Example

```python
from orbuculum_client.models.account_transactions_summary_recent import AccountTransactionsSummaryRecent

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsSummaryRecent from a JSON string
account_transactions_summary_recent_instance = AccountTransactionsSummaryRecent.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsSummaryRecent.to_json())

# convert the object into a dict
account_transactions_summary_recent_dict = account_transactions_summary_recent_instance.to_dict()
# create an instance of AccountTransactionsSummaryRecent from a dict
account_transactions_summary_recent_from_dict = AccountTransactionsSummaryRecent.from_dict(account_transactions_summary_recent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


