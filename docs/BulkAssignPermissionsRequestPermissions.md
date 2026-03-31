# BulkAssignPermissionsRequestPermissions

Permissions to assign, grouped by type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | **List[str]** | General permission names (max 10) | [optional] 
**entities** | [**List[BulkAssignPermissionsRequestPermissionsEntitiesInner]**](BulkAssignPermissionsRequestPermissionsEntitiesInner.md) | Entity permissions (max 20) | [optional] 
**account_groups** | [**List[BulkAssignPermissionsRequestPermissionsAccountGroupsInner]**](BulkAssignPermissionsRequestPermissionsAccountGroupsInner.md) | Account group permissions (max 20) | [optional] 
**labels** | [**List[BulkAssignPermissionsRequestPermissionsLabelsInner]**](BulkAssignPermissionsRequestPermissionsLabelsInner.md) | Label permissions (max 20) | [optional] 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions_request_permissions import BulkAssignPermissionsRequestPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissionsRequestPermissions from a JSON string
bulk_assign_permissions_request_permissions_instance = BulkAssignPermissionsRequestPermissions.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissionsRequestPermissions.to_json())

# convert the object into a dict
bulk_assign_permissions_request_permissions_dict = bulk_assign_permissions_request_permissions_instance.to_dict()
# create an instance of BulkAssignPermissionsRequestPermissions from a dict
bulk_assign_permissions_request_permissions_from_dict = BulkAssignPermissionsRequestPermissions.from_dict(bulk_assign_permissions_request_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


