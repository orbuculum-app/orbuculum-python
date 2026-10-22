# TransactionDeletedResponse

Response of POST /api/transaction/delete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**TransactionDeletedResponseData**](TransactionDeletedResponseData.md) |  | 
**list_diff** | [**TransactionListDiff**](TransactionListDiff.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.transaction_deleted_response import TransactionDeletedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDeletedResponse from a JSON string
transaction_deleted_response_instance = TransactionDeletedResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionDeletedResponse.to_json())

# convert the object into a dict
transaction_deleted_response_dict = transaction_deleted_response_instance.to_dict()
# create an instance of TransactionDeletedResponse from a dict
transaction_deleted_response_from_dict = TransactionDeletedResponse.from_dict(transaction_deleted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


