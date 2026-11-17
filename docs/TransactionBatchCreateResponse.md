# TransactionBatchCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for POST /api/transaction/create-batch (HTTP 200, BE-340).  - results: one item per request row, in request order: &#x60;created&#x60; with the new id, &#x60;already_existed&#x60; with the original&#39;s id (first leg for an intermediary row), or &#x60;duplicate_candidate&#x60; (BE-403) with the original&#39;s id and a &#x60;duplicate_candidate&#x60; object; nothing written. - created_count / already_existed_count: the counts of results with status created / already_existed. | 
**data** | [**TransactionBatchCreateResponseData**](TransactionBatchCreateResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_batch_create_response import TransactionBatchCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBatchCreateResponse from a JSON string
transaction_batch_create_response_instance = TransactionBatchCreateResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionBatchCreateResponse.to_json())

# convert the object into a dict
transaction_batch_create_response_dict = transaction_batch_create_response_instance.to_dict()
# create an instance of TransactionBatchCreateResponse from a dict
transaction_batch_create_response_from_dict = TransactionBatchCreateResponse.from_dict(transaction_batch_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


