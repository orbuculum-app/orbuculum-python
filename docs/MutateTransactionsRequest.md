# MutateTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**account_id** | **int** | Active account ID the list is scoped to. Optional for id-based delete/duplicate (account-less bulk mode); required+positive otherwise. | [optional] 
**action** | **str** | Mutation action | 
**filter** | **object** | Filter scope mirroring the chunk-endpoint filter set; consumed only when selection &#x3D;&#x3D; &#39;all&#39;. | [optional] 
**window** | **object** | Loaded-window descriptor for response shaping: { pastOldest:{dt,id}|null, futureNewest:{dt,id}|null }. | [optional] 
**selection** | **object** | Either an array of transaction ids or the literal &#39;all&#39;. Required for every action except create. | [optional] 
**unselected** | **List[int]** | BE-22: transaction ids to EXCLUDE. Honored ONLY when selection &#x3D;&#x3D; &#39;all&#39; (select-all-minus-N). Ignored for an explicit id-array selection. | [optional] 
**payload** | **object** | Action-specific payload (e.g. transaction fields for create/update, newAccountId for replace_account, dt for set_date). | [optional] 

## Example

```python
from orbuculum_client.models.mutate_transactions_request import MutateTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateTransactionsRequest from a JSON string
mutate_transactions_request_instance = MutateTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(MutateTransactionsRequest.to_json())

# convert the object into a dict
mutate_transactions_request_dict = mutate_transactions_request_instance.to_dict()
# create an instance of MutateTransactionsRequest from a dict
mutate_transactions_request_from_dict = MutateTransactionsRequest.from_dict(mutate_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


