# GetAccountResponseData

Account data - array when getting all accounts, object when getting by ID

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
from orbuculum_client.models.get_account_response_data import GetAccountResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountResponseData from a JSON string
get_account_response_data_instance = GetAccountResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAccountResponseData.to_json())

# convert the object into a dict
get_account_response_data_dict = get_account_response_data_instance.to_dict()
# create an instance of GetAccountResponseData from a dict
get_account_response_data_from_dict = GetAccountResponseData.from_dict(get_account_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


