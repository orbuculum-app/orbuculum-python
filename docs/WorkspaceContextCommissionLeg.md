# WorkspaceContextCommissionLeg

A transaction linked to the edited one

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**sender_account_id** | **int** |  | 
**receiver_account_id** | **int** |  | 
**sender_amount** | **str** |  | 
**receiver_amount** | **str** |  | 
**dt** | **str** | \&quot;Y-m-d H:i:s\&quot;, no timezone | 
**comment** | **str** |  | 

## Example

```python
from orbuculum_client.models.workspace_context_commission_leg import WorkspaceContextCommissionLeg

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextCommissionLeg from a JSON string
workspace_context_commission_leg_instance = WorkspaceContextCommissionLeg.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextCommissionLeg.to_json())

# convert the object into a dict
workspace_context_commission_leg_dict = workspace_context_commission_leg_instance.to_dict()
# create an instance of WorkspaceContextCommissionLeg from a dict
workspace_context_commission_leg_from_dict = WorkspaceContextCommissionLeg.from_dict(workspace_context_commission_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


