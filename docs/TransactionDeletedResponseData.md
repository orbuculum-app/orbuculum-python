# TransactionDeletedResponseData

Deletion result: {message, deleted_commissions}; when `account_id` is sent, {transactions, removed_ids, summary} instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Success message | [optional] 

## Example

```python
from orbuculum_client.models.transaction_deleted_response_data import TransactionDeletedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDeletedResponseData from a JSON string
transaction_deleted_response_data_instance = TransactionDeletedResponseData.from_json(json)
# print the JSON string representation of the object
print(TransactionDeletedResponseData.to_json())

# convert the object into a dict
transaction_deleted_response_data_dict = transaction_deleted_response_data_instance.to_dict()
# create an instance of TransactionDeletedResponseData from a dict
transaction_deleted_response_data_from_dict = TransactionDeletedResponseData.from_dict(transaction_deleted_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


