# CreateTransactionBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Request schema for POST /api/transaction/create-batch (BE-340).  Documentation schema only: each row is validated at runtime through CreateTransactionRequest. | 
**rows** | [**List[CreateTransactionRequest]**](CreateTransactionRequest.md) | Rows to create in one all-or-nothing call. A row without apikey gets a content key (date, accounts, sender_amount) and must carry dt and sender_amount (receiver_amount alone is refused with 422); workspace_id and dry_run inside a row are ignored. | 

## Example

```python
from orbuculum_client.models.create_transaction_batch_request import CreateTransactionBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransactionBatchRequest from a JSON string
create_transaction_batch_request_instance = CreateTransactionBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransactionBatchRequest.to_json())

# convert the object into a dict
create_transaction_batch_request_dict = create_transaction_batch_request_instance.to_dict()
# create an instance of CreateTransactionBatchRequest from a dict
create_transaction_batch_request_from_dict = CreateTransactionBatchRequest.from_dict(create_transaction_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


