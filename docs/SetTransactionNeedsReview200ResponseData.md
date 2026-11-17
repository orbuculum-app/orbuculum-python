# SetTransactionNeedsReview200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **int** |  | [optional] 
**needs_review** | **bool** |  | [optional] 
**needs_review_manual** | **bool** | True when a person set the mark by hand; such a mark survives closing the transaction&#39;s questions | [optional] 
**needs_review_set_by** | **int** | User id of whoever set the current mark; null when not marked | [optional] 
**needs_review_set_at** | **datetime** | When the current mark was set (UTC); null when not marked | [optional] 

## Example

```python
from orbuculum_client.models.set_transaction_needs_review200_response_data import SetTransactionNeedsReview200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SetTransactionNeedsReview200ResponseData from a JSON string
set_transaction_needs_review200_response_data_instance = SetTransactionNeedsReview200ResponseData.from_json(json)
# print the JSON string representation of the object
print(SetTransactionNeedsReview200ResponseData.to_json())

# convert the object into a dict
set_transaction_needs_review200_response_data_dict = set_transaction_needs_review200_response_data_instance.to_dict()
# create an instance of SetTransactionNeedsReview200ResponseData from a dict
set_transaction_needs_review200_response_data_from_dict = SetTransactionNeedsReview200ResponseData.from_dict(set_transaction_needs_review200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


