# SetBalanceInvalidRequestAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account ID | 
**var_date** | **str** | Recalculate from this date (ISO timestamp, null for all) | [optional] 

## Example

```python
from orbuculum_client.models.set_balance_invalid_request_accounts_inner import SetBalanceInvalidRequestAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SetBalanceInvalidRequestAccountsInner from a JSON string
set_balance_invalid_request_accounts_inner_instance = SetBalanceInvalidRequestAccountsInner.from_json(json)
# print the JSON string representation of the object
print(SetBalanceInvalidRequestAccountsInner.to_json())

# convert the object into a dict
set_balance_invalid_request_accounts_inner_dict = set_balance_invalid_request_accounts_inner_instance.to_dict()
# create an instance of SetBalanceInvalidRequestAccountsInner from a dict
set_balance_invalid_request_accounts_inner_from_dict = SetBalanceInvalidRequestAccountsInner.from_dict(set_balance_invalid_request_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


