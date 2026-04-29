# UpdateTransactionResponseDataCommissions

Per-slot commission CRUD result (sender + receiver)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | [**UpdateCommissionResult**](UpdateCommissionResult.md) |  | [optional] 
**receiver** | [**UpdateCommissionResult**](UpdateCommissionResult.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.update_transaction_response_data_commissions import UpdateTransactionResponseDataCommissions

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionResponseDataCommissions from a JSON string
update_transaction_response_data_commissions_instance = UpdateTransactionResponseDataCommissions.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionResponseDataCommissions.to_json())

# convert the object into a dict
update_transaction_response_data_commissions_dict = update_transaction_response_data_commissions_instance.to_dict()
# create an instance of UpdateTransactionResponseDataCommissions from a dict
update_transaction_response_data_commissions_from_dict = UpdateTransactionResponseDataCommissions.from_dict(update_transaction_response_data_commissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


