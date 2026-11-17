# ChangeSetItem

One create, update or delete of a row, with the full row before and after it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Ascending in write order | 
**model_type** | **str** |  | 
**model_id** | **int** |  | 
**action** | **str** |  | 
**before** | **Dict[str, object]** | full database row (column → value) before this write; null on create. For a transaction row, sender_balance_after / receiver_balance_after are null for a leg whose account balance the requesting role may not see (BE-369). | 
**after** | **Dict[str, object]** | full database row (column → value) after this write; null on delete. For a transaction row, sender_balance_after / receiver_balance_after are null for a leg whose account balance the requesting role may not see (BE-369). | 

## Example

```python
from orbuculum_client.models.change_set_item import ChangeSetItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeSetItem from a JSON string
change_set_item_instance = ChangeSetItem.from_json(json)
# print the JSON string representation of the object
print(ChangeSetItem.to_json())

# convert the object into a dict
change_set_item_dict = change_set_item_instance.to_dict()
# create an instance of ChangeSetItem from a dict
change_set_item_from_dict = ChangeSetItem.from_dict(change_set_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


