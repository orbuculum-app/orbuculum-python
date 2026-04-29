# IntermediaryTransactionUpdatedResponse

Response after successfully updating an intermediary transaction pair (atomic two-leg update via POST /api/transaction/update). HTTP 200. The `data` payload uses the same hybrid shape as IntermediaryTransactionCreatedResponse: Group A (legacy keys + leg ids + commission ids) + Group B (14 shared metadata fields lifted from leg1) + Group C (full per-leg formatTransactionResponse shape).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code. | 
**data** | [**IntermediaryTransactionUpdatedData**](IntermediaryTransactionUpdatedData.md) |  | 

## Example

```python
from orbuculum_client.models.intermediary_transaction_updated_response import IntermediaryTransactionUpdatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediaryTransactionUpdatedResponse from a JSON string
intermediary_transaction_updated_response_instance = IntermediaryTransactionUpdatedResponse.from_json(json)
# print the JSON string representation of the object
print(IntermediaryTransactionUpdatedResponse.to_json())

# convert the object into a dict
intermediary_transaction_updated_response_dict = intermediary_transaction_updated_response_instance.to_dict()
# create an instance of IntermediaryTransactionUpdatedResponse from a dict
intermediary_transaction_updated_response_from_dict = IntermediaryTransactionUpdatedResponse.from_dict(intermediary_transaction_updated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


