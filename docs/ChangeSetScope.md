# ChangeSetScope

The accounts and/or transactions a change set is meant to touch. Every write held in the set, and its commit, is checked by the ledger verifier's invariant I5 against it. A transaction is in scope when its id is in `transaction_ids`, or when BOTH its sender and its receiver account are in `account_ids`: declare both sides of the transfers and payments the set will write. With only `transaction_ids`, a new transaction is out of scope. The gate checks transactions that still exist and whose last item in the set is not a delete. Deleting a transaction, moving a transaction off an account (only the row after the write is checked), and writes to accounts, counterparties and labels are not checked against the scope. At least one key; each list non-empty, of positive integers that exist in the workspace; any other key is a 400. In a ChangeSet the lists are de-duplicated and sorted ascending.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **List[int]** | BE-413: the scope a change set declares at open; the verifier gate checks it as invariant I5 | [optional] 
**transaction_ids** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.change_set_scope import ChangeSetScope

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeSetScope from a JSON string
change_set_scope_instance = ChangeSetScope.from_json(json)
# print the JSON string representation of the object
print(ChangeSetScope.to_json())

# convert the object into a dict
change_set_scope_dict = change_set_scope_instance.to_dict()
# create an instance of ChangeSetScope from a dict
change_set_scope_from_dict = ChangeSetScope.from_dict(change_set_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


