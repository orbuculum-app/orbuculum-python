# AppContextResponseDataAccountTransactions

Top-level account-transactions entrypoint, or null when user lacks ENTITY_ACCESS_READ.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from orbuculum_client.models.app_context_response_data_account_transactions import AppContextResponseDataAccountTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of AppContextResponseDataAccountTransactions from a JSON string
app_context_response_data_account_transactions_instance = AppContextResponseDataAccountTransactions.from_json(json)
# print the JSON string representation of the object
print(AppContextResponseDataAccountTransactions.to_json())

# convert the object into a dict
app_context_response_data_account_transactions_dict = app_context_response_data_account_transactions_instance.to_dict()
# create an instance of AppContextResponseDataAccountTransactions from a dict
app_context_response_data_account_transactions_from_dict = AppContextResponseDataAccountTransactions.from_dict(app_context_response_data_account_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


