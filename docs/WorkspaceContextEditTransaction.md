# WorkspaceContextEditTransaction

The edited transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**sender_account_id** | **int** |  | 
**receiver_account_id** | **int** |  | 
**sender_amount** | **str** |  | 
**receiver_amount** | **str** |  | 
**dt** | **str** | \&quot;Y-m-d H:i:s\&quot;, no timezone | 
**comment** | **str** |  | 
**done** | **bool** |  | 
**chained_id** | **int** |  | 
**chained_commission_id** | **int** |  | 
**chained_receiver_commission** | **int** |  | 
**label_id** | **int** |  | 
**future_id** | **int** |  | 
**forex** | **str** |  | 
**commission_applied** | **bool** |  | 

## Example

```python
from orbuculum_client.models.workspace_context_edit_transaction import WorkspaceContextEditTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextEditTransaction from a JSON string
workspace_context_edit_transaction_instance = WorkspaceContextEditTransaction.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextEditTransaction.to_json())

# convert the object into a dict
workspace_context_edit_transaction_dict = workspace_context_edit_transaction_instance.to_dict()
# create an instance of WorkspaceContextEditTransaction from a dict
workspace_context_edit_transaction_from_dict = WorkspaceContextEditTransaction.from_dict(workspace_context_edit_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


