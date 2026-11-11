# ChangeSet

A server-side group of writes of transactions, accounts, counterparties and labels. `kind` explicit: opened with POST /api/change-set/open; implicit: header-less writes of one user and attested client within a 300 s window; request: one web-UI request; system: one console run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | BE-337: a change set — a server-side group of writes with full before/after row snapshots | 
**workspace_id** | **int** |  | 
**author_id** | **int** |  | [optional] 
**client_connection_id** | **int** |  | [optional] 
**client** | **str** | Attested MCP client of the writes, when one was sent | [optional] 
**source_ref** | **str** | Free reference given at open, e.g. a message id or a file id | [optional] 
**kind** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**committed_at** | **datetime** |  | [optional] 
**items** | [**List[ChangeSetItem]**](ChangeSetItem.md) | The recorded writes in write order | 

## Example

```python
from orbuculum_client.models.change_set import ChangeSet

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeSet from a JSON string
change_set_instance = ChangeSet.from_json(json)
# print the JSON string representation of the object
print(ChangeSet.to_json())

# convert the object into a dict
change_set_dict = change_set_instance.to_dict()
# create an instance of ChangeSet from a dict
change_set_from_dict = ChangeSet.from_dict(change_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


