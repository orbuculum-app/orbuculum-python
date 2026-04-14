# CheckChainedTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**transaction_ids** | **List[int]** |  | 
**action** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.check_chained_transactions_request import CheckChainedTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckChainedTransactionsRequest from a JSON string
check_chained_transactions_request_instance = CheckChainedTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(CheckChainedTransactionsRequest.to_json())

# convert the object into a dict
check_chained_transactions_request_dict = check_chained_transactions_request_instance.to_dict()
# create an instance of CheckChainedTransactionsRequest from a dict
check_chained_transactions_request_from_dict = CheckChainedTransactionsRequest.from_dict(check_chained_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


