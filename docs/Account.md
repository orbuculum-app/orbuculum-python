# Account

Account object with all details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account ID | [optional] 
**name** | **str** | Account name | [optional] 
**entity_id** | **int** | Entity ID | [optional] 
**entity_name** | **str** | Entity name | [optional] 
**entity_type** | **int** | Entity type | [optional] 
**currency_id** | **int** | Currency ID (null for some legacy accounts) | [optional] 
**type** | **int** | Account subtype | [optional] 
**hidden** | **int** | Whether the account is hidden (0 or 1) | [optional] 
**balance** | **str** | Account balance (null if hidden) | [optional] 
**hide_balances** | **int** | Whether balances are hidden (0 or 1) | [optional] 
**api_id** | **str** | External API identifier | [optional] 
**commission_enabled** | **int** | Commission enabled flag (0&#x3D;disabled, 1&#x3D;enabled) | [optional] 
**commission_account_id** | **int** | Commission account ID (null when commission disabled) | [optional] 
**commission_appliance** | **int** | Commission appliance (0 or 1) | [optional] 
**custom_commission_sender_id** | **int** | Custom commission sender ID (null when not set) | [optional] 
**has_transactions** | **bool** | Whether account has any transactions (single mode only) | [optional] 
**initial_balance** | **str** | Initial balance amount (single mode only) | [optional] 
**limited** | **bool** | Account limitation flag | [optional] 
**tags** | **List[int]** | Array of account_group_id values | [optional] 

## Example

```python
from orbuculum_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


