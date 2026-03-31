# BulkAssignPermissionsRequestPermissionsEntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** |  | [optional] 
**can_manage** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions_request_permissions_entities_inner import BulkAssignPermissionsRequestPermissionsEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissionsRequestPermissionsEntitiesInner from a JSON string
bulk_assign_permissions_request_permissions_entities_inner_instance = BulkAssignPermissionsRequestPermissionsEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissionsRequestPermissionsEntitiesInner.to_json())

# convert the object into a dict
bulk_assign_permissions_request_permissions_entities_inner_dict = bulk_assign_permissions_request_permissions_entities_inner_instance.to_dict()
# create an instance of BulkAssignPermissionsRequestPermissionsEntitiesInner from a dict
bulk_assign_permissions_request_permissions_entities_inner_from_dict = BulkAssignPermissionsRequestPermissionsEntitiesInner.from_dict(bulk_assign_permissions_request_permissions_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


