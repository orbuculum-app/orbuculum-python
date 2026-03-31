# GetAccountBalanceResponse

Response for account balance endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetAccountBalanceResponseData**](GetAccountBalanceResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_account_balance_response import GetAccountBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountBalanceResponse from a JSON string
get_account_balance_response_instance = GetAccountBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountBalanceResponse.to_json())

# convert the object into a dict
get_account_balance_response_dict = get_account_balance_response_instance.to_dict()
# create an instance of GetAccountBalanceResponse from a dict
get_account_balance_response_from_dict = GetAccountBalanceResponse.from_dict(get_account_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


