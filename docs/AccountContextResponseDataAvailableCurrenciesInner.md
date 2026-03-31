# AccountContextResponseDataAvailableCurrenciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Currency ID | 
**name** | **str** | Currency name/code | 
**precision** | **int** | Decimal precision | 
**basic** | **bool** | Whether this is the basic currency | 

## Example

```python
from orbuculum_client.models.account_context_response_data_available_currencies_inner import AccountContextResponseDataAvailableCurrenciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContextResponseDataAvailableCurrenciesInner from a JSON string
account_context_response_data_available_currencies_inner_instance = AccountContextResponseDataAvailableCurrenciesInner.from_json(json)
# print the JSON string representation of the object
print(AccountContextResponseDataAvailableCurrenciesInner.to_json())

# convert the object into a dict
account_context_response_data_available_currencies_inner_dict = account_context_response_data_available_currencies_inner_instance.to_dict()
# create an instance of AccountContextResponseDataAvailableCurrenciesInner from a dict
account_context_response_data_available_currencies_inner_from_dict = AccountContextResponseDataAvailableCurrenciesInner.from_dict(account_context_response_data_available_currencies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


