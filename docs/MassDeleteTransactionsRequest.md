# MassDeleteTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**transaction_ids** | **List[int]** | Array of transaction IDs to delete (max 500) | 

## Example

```python
from orbuculum_client.models.mass_delete_transactions_request import MassDeleteTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassDeleteTransactionsRequest from a JSON string
mass_delete_transactions_request_instance = MassDeleteTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(MassDeleteTransactionsRequest.to_json())

# convert the object into a dict
mass_delete_transactions_request_dict = mass_delete_transactions_request_instance.to_dict()
# create an instance of MassDeleteTransactionsRequest from a dict
mass_delete_transactions_request_from_dict = MassDeleteTransactionsRequest.from_dict(mass_delete_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


