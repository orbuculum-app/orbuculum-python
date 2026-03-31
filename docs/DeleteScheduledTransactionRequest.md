# DeleteScheduledTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Scheduled transaction ID | 
**delete_type** | **int** | Delete type: 1&#x3D;ENTIRE, 2&#x3D;SINGLE, 3&#x3D;THIS_AND_FUTURE | 
**trx_id** | **int** | Transaction ID (required for delete_type 2 and 3) | [optional] 

## Example

```python
from orbuculum_client.models.delete_scheduled_transaction_request import DeleteScheduledTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteScheduledTransactionRequest from a JSON string
delete_scheduled_transaction_request_instance = DeleteScheduledTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteScheduledTransactionRequest.to_json())

# convert the object into a dict
delete_scheduled_transaction_request_dict = delete_scheduled_transaction_request_instance.to_dict()
# create an instance of DeleteScheduledTransactionRequest from a dict
delete_scheduled_transaction_request_from_dict = DeleteScheduledTransactionRequest.from_dict(delete_scheduled_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


