# GetRecalculatedBalancesResponseDataAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**is_calculating** | **bool** |  | 

## Example

```python
from orbuculum_client.models.get_recalculated_balances_response_data_accounts_inner import GetRecalculatedBalancesResponseDataAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecalculatedBalancesResponseDataAccountsInner from a JSON string
get_recalculated_balances_response_data_accounts_inner_instance = GetRecalculatedBalancesResponseDataAccountsInner.from_json(json)
# print the JSON string representation of the object
print(GetRecalculatedBalancesResponseDataAccountsInner.to_json())

# convert the object into a dict
get_recalculated_balances_response_data_accounts_inner_dict = get_recalculated_balances_response_data_accounts_inner_instance.to_dict()
# create an instance of GetRecalculatedBalancesResponseDataAccountsInner from a dict
get_recalculated_balances_response_data_accounts_inner_from_dict = GetRecalculatedBalancesResponseDataAccountsInner.from_dict(get_recalculated_balances_response_data_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


