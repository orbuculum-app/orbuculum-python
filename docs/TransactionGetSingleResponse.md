# TransactionGetSingleResponse

Response from /api/transaction/get when invoked in single mode (id or apikey supplied). `data` is the full Transaction shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code. | 
**data** | [**Transaction**](Transaction.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_get_single_response import TransactionGetSingleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionGetSingleResponse from a JSON string
transaction_get_single_response_instance = TransactionGetSingleResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionGetSingleResponse.to_json())

# convert the object into a dict
transaction_get_single_response_dict = transaction_get_single_response_instance.to_dict()
# create an instance of TransactionGetSingleResponse from a dict
transaction_get_single_response_from_dict = TransactionGetSingleResponse.from_dict(transaction_get_single_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


