# AccountContextResponseDataAccount

Account data (null in create mode)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account ID | 
**name** | **str** | Account name | 
**entity_id** | **int** | Entity ID | 
**currency_id** | **int** | Currency ID | 
**type** | **int** | Account type | 
**hidden** | **bool** | Whether account is hidden | 
**commission_type** | **int** | Commission type | 
**commission_appliance** | **bool** | Whether commission is applied | 
**limited** | **bool** | Whether account has limitations | 
**hide_balances** | **bool** | Whether balances are hidden | 
**api_id** | **str** | External API identifier | 

## Example

```python
from orbuculum_client.models.account_context_response_data_account import AccountContextResponseDataAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContextResponseDataAccount from a JSON string
account_context_response_data_account_instance = AccountContextResponseDataAccount.from_json(json)
# print the JSON string representation of the object
print(AccountContextResponseDataAccount.to_json())

# convert the object into a dict
account_context_response_data_account_dict = account_context_response_data_account_instance.to_dict()
# create an instance of AccountContextResponseDataAccount from a dict
account_context_response_data_account_from_dict = AccountContextResponseDataAccount.from_dict(account_context_response_data_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


