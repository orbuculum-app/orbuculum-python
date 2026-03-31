# BulkAssignPermissionsRequestPermissionsLabelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**can_manage** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions_request_permissions_labels_inner import BulkAssignPermissionsRequestPermissionsLabelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissionsRequestPermissionsLabelsInner from a JSON string
bulk_assign_permissions_request_permissions_labels_inner_instance = BulkAssignPermissionsRequestPermissionsLabelsInner.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissionsRequestPermissionsLabelsInner.to_json())

# convert the object into a dict
bulk_assign_permissions_request_permissions_labels_inner_dict = bulk_assign_permissions_request_permissions_labels_inner_instance.to_dict()
# create an instance of BulkAssignPermissionsRequestPermissionsLabelsInner from a dict
bulk_assign_permissions_request_permissions_labels_inner_from_dict = BulkAssignPermissionsRequestPermissionsLabelsInner.from_dict(bulk_assign_permissions_request_permissions_labels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


