# TransactionBatchCreateResponseDataResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_index** | **int** |  | 
**status** | **str** | duplicate_candidate: nothing written; id is the original transaction (BE-403) | 
**id** | **int** | New transaction id (created) or the original&#39;s id (already_existed, duplicate_candidate); first leg for an intermediary row | 
**duplicate_candidate** | [**DuplicateCandidate**](DuplicateCandidate.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.transaction_batch_create_response_data_results_inner import TransactionBatchCreateResponseDataResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBatchCreateResponseDataResultsInner from a JSON string
transaction_batch_create_response_data_results_inner_instance = TransactionBatchCreateResponseDataResultsInner.from_json(json)
# print the JSON string representation of the object
print(TransactionBatchCreateResponseDataResultsInner.to_json())

# convert the object into a dict
transaction_batch_create_response_data_results_inner_dict = transaction_batch_create_response_data_results_inner_instance.to_dict()
# create an instance of TransactionBatchCreateResponseDataResultsInner from a dict
transaction_batch_create_response_data_results_inner_from_dict = TransactionBatchCreateResponseDataResultsInner.from_dict(transaction_batch_create_response_data_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


