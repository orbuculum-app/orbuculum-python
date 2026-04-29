# IntermediaryTransactionCreatedResponse

Response after successfully creating an intermediary transaction (two linked legs). `data` carries the legacy leg/commission ids, the shared parent-transaction metadata, and full per-leg Transaction shapes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code. | 
**data** | [**IntermediaryTransactionCreatedData**](IntermediaryTransactionCreatedData.md) |  | 

## Example

```python
from orbuculum_client.models.intermediary_transaction_created_response import IntermediaryTransactionCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediaryTransactionCreatedResponse from a JSON string
intermediary_transaction_created_response_instance = IntermediaryTransactionCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(IntermediaryTransactionCreatedResponse.to_json())

# convert the object into a dict
intermediary_transaction_created_response_dict = intermediary_transaction_created_response_instance.to_dict()
# create an instance of IntermediaryTransactionCreatedResponse from a dict
intermediary_transaction_created_response_from_dict = IntermediaryTransactionCreatedResponse.from_dict(intermediary_transaction_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


