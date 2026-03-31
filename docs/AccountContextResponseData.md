# AccountContextResponseData

Account context data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Form mode: &#39;create&#39; or &#39;edit&#39; | 
**account** | [**AccountContextResponseDataAccount**](AccountContextResponseDataAccount.md) |  | 
**entity** | [**AccountContextResponseDataEntity**](AccountContextResponseDataEntity.md) |  | 
**available_currencies** | [**List[AccountContextResponseDataAvailableCurrenciesInner]**](AccountContextResponseDataAvailableCurrenciesInner.md) | Available currencies for this entity type | 
**available_subtypes** | [**List[AccountContextResponseDataAvailableSubtypesInner]**](AccountContextResponseDataAvailableSubtypesInner.md) | Available account subtypes for this entity type | 
**commission_sender_account** | [**AccountContextResponseDataCommissionSenderAccount**](AccountContextResponseDataCommissionSenderAccount.md) |  | 
**commission_receiver_account** | [**AccountContextResponseDataCommissionReceiverAccount**](AccountContextResponseDataCommissionReceiverAccount.md) |  | 
**has_transactions** | **bool** | Whether the account has any transactions (always false in create mode) | 
**initial_balance** | **str** | Initial balance amount as string (empty string in create mode) | 
**can_manage** | **bool** | Whether the current user can manage (edit) the account | 

## Example

```python
from orbuculum_client.models.account_context_response_data import AccountContextResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContextResponseData from a JSON string
account_context_response_data_instance = AccountContextResponseData.from_json(json)
# print the JSON string representation of the object
print(AccountContextResponseData.to_json())

# convert the object into a dict
account_context_response_data_dict = account_context_response_data_instance.to_dict()
# create an instance of AccountContextResponseData from a dict
account_context_response_data_from_dict = AccountContextResponseData.from_dict(account_context_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


