# SetTransactionNeedsReview200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**SetTransactionNeedsReview200ResponseData**](SetTransactionNeedsReview200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.set_transaction_needs_review200_response import SetTransactionNeedsReview200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetTransactionNeedsReview200Response from a JSON string
set_transaction_needs_review200_response_instance = SetTransactionNeedsReview200Response.from_json(json)
# print the JSON string representation of the object
print(SetTransactionNeedsReview200Response.to_json())

# convert the object into a dict
set_transaction_needs_review200_response_dict = set_transaction_needs_review200_response_instance.to_dict()
# create an instance of SetTransactionNeedsReview200Response from a dict
set_transaction_needs_review200_response_from_dict = SetTransactionNeedsReview200Response.from_dict(set_transaction_needs_review200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


