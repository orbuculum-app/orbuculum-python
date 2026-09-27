# ScheduledTransactionCreatedResponse

Response after creating a scheduled transaction via POST /api/scheduled-transaction/create (dry_run false or omitted).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response after creating a scheduled transaction via POST /api/scheduled-transaction/create (HTTP 200, dry_run false or omitted).  BE-102: the former inline 200 shape of that endpoint, relocated so the 200 response can be a oneOf with ScheduledTransactionPreview. The &#x60;data&#x60; &#x60;required&#x60; list keeps the two branches disjoint. | 
**data** | [**ScheduledTransactionCreatedResponseData**](ScheduledTransactionCreatedResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.scheduled_transaction_created_response import ScheduledTransactionCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionCreatedResponse from a JSON string
scheduled_transaction_created_response_instance = ScheduledTransactionCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionCreatedResponse.to_json())

# convert the object into a dict
scheduled_transaction_created_response_dict = scheduled_transaction_created_response_instance.to_dict()
# create an instance of ScheduledTransactionCreatedResponse from a dict
scheduled_transaction_created_response_from_dict = ScheduledTransactionCreatedResponse.from_dict(scheduled_transaction_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


