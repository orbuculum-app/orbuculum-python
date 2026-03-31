# BulkAssignPermissionsRequestPermissionsAccountGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group_id** | **int** |  | [optional] 
**can_manage** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions_request_permissions_account_groups_inner import BulkAssignPermissionsRequestPermissionsAccountGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissionsRequestPermissionsAccountGroupsInner from a JSON string
bulk_assign_permissions_request_permissions_account_groups_inner_instance = BulkAssignPermissionsRequestPermissionsAccountGroupsInner.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissionsRequestPermissionsAccountGroupsInner.to_json())

# convert the object into a dict
bulk_assign_permissions_request_permissions_account_groups_inner_dict = bulk_assign_permissions_request_permissions_account_groups_inner_instance.to_dict()
# create an instance of BulkAssignPermissionsRequestPermissionsAccountGroupsInner from a dict
bulk_assign_permissions_request_permissions_account_groups_inner_from_dict = BulkAssignPermissionsRequestPermissionsAccountGroupsInner.from_dict(bulk_assign_permissions_request_permissions_account_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


