# WorkspaceContextPairOrder

Account ordering for the Add modal. In receiver_order the outer keys are sender account IDs and the lists hold receiver account IDs; in sender_order the outer keys are receiver account IDs and the lists hold sender account IDs. Most recent first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**Dict[str, WorkspaceContextPairOrderAccountsValue]**](WorkspaceContextPairOrderAccountsValue.md) | Keyed by account ID. An empty map is serialized as {}. | 
**entities** | **Dict[str, List[int]]** | Entity IDs keyed by account ID. An empty map is serialized as {}. | 

## Example

```python
from orbuculum_client.models.workspace_context_pair_order import WorkspaceContextPairOrder

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextPairOrder from a JSON string
workspace_context_pair_order_instance = WorkspaceContextPairOrder.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextPairOrder.to_json())

# convert the object into a dict
workspace_context_pair_order_dict = workspace_context_pair_order_instance.to_dict()
# create an instance of WorkspaceContextPairOrder from a dict
workspace_context_pair_order_from_dict = WorkspaceContextPairOrder.from_dict(workspace_context_pair_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


