# BulkCreateTransactionsRequest

Request body for bulk-creating 1..500 transactions in a single call. Each item in `transactions` follows the CreateTransactionRequest schema and is validated/created independently.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**transactions** | [**List[CreateTransactionRequest]**](CreateTransactionRequest.md) | Array of transaction objects to create (1 to 500). Each item has the same shape as CreateTransactionRequest. | 
**stop_on_error** | **bool** | If true, abort and rollback on first item failure (atomic). If false, continue on per-item errors and return partial-success results. Permission errors (403) always abort regardless of this flag (except in dry_run mode). | [optional] [default to False]
**dry_run** | **bool** | If true, validate every item and compute previews but do NOT write to the database. | [optional] [default to False]

## Example

```python
from orbuculum_client.models.bulk_create_transactions_request import BulkCreateTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateTransactionsRequest from a JSON string
bulk_create_transactions_request_instance = BulkCreateTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCreateTransactionsRequest.to_json())

# convert the object into a dict
bulk_create_transactions_request_dict = bulk_create_transactions_request_instance.to_dict()
# create an instance of BulkCreateTransactionsRequest from a dict
bulk_create_transactions_request_from_dict = BulkCreateTransactionsRequest.from_dict(bulk_create_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


