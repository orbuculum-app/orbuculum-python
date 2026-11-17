# SetTransactionNeedsReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**transaction_id** | **int** |  | 
**needs_review** | **bool** | true: mark by hand; false: clear the mark | 

## Example

```python
from orbuculum_client.models.set_transaction_needs_review_request import SetTransactionNeedsReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTransactionNeedsReviewRequest from a JSON string
set_transaction_needs_review_request_instance = SetTransactionNeedsReviewRequest.from_json(json)
# print the JSON string representation of the object
print(SetTransactionNeedsReviewRequest.to_json())

# convert the object into a dict
set_transaction_needs_review_request_dict = set_transaction_needs_review_request_instance.to_dict()
# create an instance of SetTransactionNeedsReviewRequest from a dict
set_transaction_needs_review_request_from_dict = SetTransactionNeedsReviewRequest.from_dict(set_transaction_needs_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


