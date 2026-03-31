# UpdateAccountTabRequestAccountsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_access** | **bool** |  | [optional] 
**full_access** | **bool** |  | [optional] 
**show_balance** | **bool** |  | [optional] 
**hide_transactions** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.update_account_tab_request_accounts_value import UpdateAccountTabRequestAccountsValue

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountTabRequestAccountsValue from a JSON string
update_account_tab_request_accounts_value_instance = UpdateAccountTabRequestAccountsValue.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountTabRequestAccountsValue.to_json())

# convert the object into a dict
update_account_tab_request_accounts_value_dict = update_account_tab_request_accounts_value_instance.to_dict()
# create an instance of UpdateAccountTabRequestAccountsValue from a dict
update_account_tab_request_accounts_value_from_dict = UpdateAccountTabRequestAccountsValue.from_dict(update_account_tab_request_accounts_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


