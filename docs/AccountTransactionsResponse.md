# AccountTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**AccountTransactionsResponseData**](AccountTransactionsResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.account_transactions_response import AccountTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsResponse from a JSON string
account_transactions_response_instance = AccountTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsResponse.to_json())

# convert the object into a dict
account_transactions_response_dict = account_transactions_response_instance.to_dict()
# create an instance of AccountTransactionsResponse from a dict
account_transactions_response_from_dict = AccountTransactionsResponse.from_dict(account_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


