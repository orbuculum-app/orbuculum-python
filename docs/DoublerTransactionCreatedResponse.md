# DoublerTransactionCreatedResponse

Response after successfully creating a doubler transaction (two linked legs)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**DoublerTransactionCreatedData**](DoublerTransactionCreatedData.md) |  | 

## Example

```python
from orbuculum_client.models.doubler_transaction_created_response import DoublerTransactionCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DoublerTransactionCreatedResponse from a JSON string
doubler_transaction_created_response_instance = DoublerTransactionCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(DoublerTransactionCreatedResponse.to_json())

# convert the object into a dict
doubler_transaction_created_response_dict = doubler_transaction_created_response_instance.to_dict()
# create an instance of DoublerTransactionCreatedResponse from a dict
doubler_transaction_created_response_from_dict = DoublerTransactionCreatedResponse.from_dict(doubler_transaction_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


