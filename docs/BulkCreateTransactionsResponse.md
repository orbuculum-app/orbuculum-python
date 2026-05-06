# BulkCreateTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for POST /api/transaction/bulk-create (HTTP 200).  Container shape: - status: HTTP status (always 200 on success / partial success). - data: - created_count: number of items actually persisted (always 0 in dry_run mode). - failed_count: number of items that failed validation/business rules. - items: per-input-item array. Each entry has: - item_index: 0-based position in the request transactions array. - id (optional): created transaction id (real run, success only). - preview (optional): createTransaction(dryRun&#x3D;true)[&#39;data&#39;] payload (dry_run, success only). - errors (optional): [{field, message}, ...] when this item failed. | 
**data** | [**BulkCreateTransactionsResponseData**](BulkCreateTransactionsResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.bulk_create_transactions_response import BulkCreateTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateTransactionsResponse from a JSON string
bulk_create_transactions_response_instance = BulkCreateTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCreateTransactionsResponse.to_json())

# convert the object into a dict
bulk_create_transactions_response_dict = bulk_create_transactions_response_instance.to_dict()
# create an instance of BulkCreateTransactionsResponse from a dict
bulk_create_transactions_response_from_dict = BulkCreateTransactionsResponse.from_dict(bulk_create_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


