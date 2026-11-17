# TransactionBatchCreateResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TransactionBatchCreateResponseDataResultsInner]**](TransactionBatchCreateResponseDataResultsInner.md) |  | 
**created_count** | **int** |  | 
**already_existed_count** | **int** |  | 

## Example

```python
from orbuculum_client.models.transaction_batch_create_response_data import TransactionBatchCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBatchCreateResponseData from a JSON string
transaction_batch_create_response_data_instance = TransactionBatchCreateResponseData.from_json(json)
# print the JSON string representation of the object
print(TransactionBatchCreateResponseData.to_json())

# convert the object into a dict
transaction_batch_create_response_data_dict = transaction_batch_create_response_data_instance.to_dict()
# create an instance of TransactionBatchCreateResponseData from a dict
transaction_batch_create_response_data_from_dict = TransactionBatchCreateResponseData.from_dict(transaction_batch_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


