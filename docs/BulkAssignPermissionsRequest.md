# BulkAssignPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**role_id** | **int** | Role ID to assign permissions to | 
**permissions** | [**BulkAssignPermissionsRequestPermissions**](BulkAssignPermissionsRequestPermissions.md) |  | 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions_request import BulkAssignPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissionsRequest from a JSON string
bulk_assign_permissions_request_instance = BulkAssignPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissionsRequest.to_json())

# convert the object into a dict
bulk_assign_permissions_request_dict = bulk_assign_permissions_request_instance.to_dict()
# create an instance of BulkAssignPermissionsRequest from a dict
bulk_assign_permissions_request_from_dict = BulkAssignPermissionsRequest.from_dict(bulk_assign_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


