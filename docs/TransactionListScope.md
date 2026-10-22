# TransactionListScope

The client's loaded transaction list. Sent as optional `list_scope` with POST /api/transaction/create|update|delete to receive `list_diff`; same scope fields as POST /api/transaction/mutate. Absent or null: no `list_diff`, response unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account the loaded list is scoped to. Positive integer. | 
**filter** | **object** | Filter of the loaded list — the &#x60;filter&#x60; object of POST /api/transaction/mutate. Scopes isOut, the more-rows-beyond-the-edge check and the summary. Absent or null: no filter. | [optional] 
**window** | **object** | Loaded-window descriptor, as in POST /api/transaction/mutate: { pastOldest:{dt,id}|null, futureNewest:{dt,id}|null }. Absent or null: both cursors null. | [optional] 

## Example

```python
from orbuculum_client.models.transaction_list_scope import TransactionListScope

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionListScope from a JSON string
transaction_list_scope_instance = TransactionListScope.from_json(json)
# print the JSON string representation of the object
print(TransactionListScope.to_json())

# convert the object into a dict
transaction_list_scope_dict = transaction_list_scope_instance.to_dict()
# create an instance of TransactionListScope from a dict
transaction_list_scope_from_dict = TransactionListScope.from_dict(transaction_list_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


