# GetAccountBalanceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **str** | Account balance at the specified date: every transaction dated at or before it counts and &#x60;done&#x60; plays no part. Null if balance is hidden for this role. | [optional] 
**unconfirmed_amount** | **str** | The part of &#x60;balance&#x60;, at the same &#x60;date&#x60; and &#x60;trx_id&#x60;, that comes from unconfirmed rows (done false, recurring or not). Signed: the balance minus this is what confirmed rows add up to. Null when this account&#39;s balance is hidden for the caller&#39;s role. | [optional] 
**currency** | **str** | Stored currency name (may be a sign such as &#39;$&#39;) | [optional] 
**currency_code** | **str** | ISO code of the account currency | [optional] 
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


