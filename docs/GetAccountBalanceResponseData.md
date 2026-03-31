# GetAccountBalanceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **str** | Account balance at the specified date. Null if balance is hidden for this role. | [optional] 
**currency** | **str** | Currency name | [optional] 
**currency_id** | **int** | Currency ID | [optional] 
**precision** | **int** | Currency decimal precision | [optional] 

## Example

```python
from orbuculum_client.models.get_account_balance_response_data import GetAccountBalanceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountBalanceResponseData from a JSON string
get_account_balance_response_data_instance = GetAccountBalanceResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAccountBalanceResponseData.to_json())

# convert the object into a dict
get_account_balance_response_data_dict = get_account_balance_response_data_instance.to_dict()
# create an instance of GetAccountBalanceResponseData from a dict
get_account_balance_response_data_from_dict = GetAccountBalanceResponseData.from_dict(get_account_balance_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


