# AccountContextResponseDataCommissionReceiverAccount

Commission receiver account (null if not set or commission disabled)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account ID | 
**name** | **str** | Account name | 
**entity_name** | **str** | Entity name | 
**currency_code** | **str** | Currency code | 

## Example

```python
from orbuculum_client.models.account_context_response_data_commission_receiver_account import AccountContextResponseDataCommissionReceiverAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContextResponseDataCommissionReceiverAccount from a JSON string
account_context_response_data_commission_receiver_account_instance = AccountContextResponseDataCommissionReceiverAccount.from_json(json)
# print the JSON string representation of the object
print(AccountContextResponseDataCommissionReceiverAccount.to_json())

# convert the object into a dict
account_context_response_data_commission_receiver_account_dict = account_context_response_data_commission_receiver_account_instance.to_dict()
# create an instance of AccountContextResponseDataCommissionReceiverAccount from a dict
account_context_response_data_commission_receiver_account_from_dict = AccountContextResponseDataCommissionReceiverAccount.from_dict(account_context_response_data_commission_receiver_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


