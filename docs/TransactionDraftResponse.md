# TransactionDraftResponse

The complete render-ready state of the transaction modal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**TransactionDraftResponseData**](TransactionDraftResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_draft_response import TransactionDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftResponse from a JSON string
transaction_draft_response_instance = TransactionDraftResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftResponse.to_json())

# convert the object into a dict
transaction_draft_response_dict = transaction_draft_response_instance.to_dict()
# create an instance of TransactionDraftResponse from a dict
transaction_draft_response_from_dict = TransactionDraftResponse.from_dict(transaction_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


