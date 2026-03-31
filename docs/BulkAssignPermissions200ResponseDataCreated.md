# BulkAssignPermissions200ResponseDataCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | **int** |  | [optional] 
**entities** | **int** |  | [optional] 
**account_groups** | **int** |  | [optional] 
**labels** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions200_response_data_created import BulkAssignPermissions200ResponseDataCreated

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissions200ResponseDataCreated from a JSON string
bulk_assign_permissions200_response_data_created_instance = BulkAssignPermissions200ResponseDataCreated.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissions200ResponseDataCreated.to_json())

# convert the object into a dict
bulk_assign_permissions200_response_data_created_dict = bulk_assign_permissions200_response_data_created_instance.to_dict()
# create an instance of BulkAssignPermissions200ResponseDataCreated from a dict
bulk_assign_permissions200_response_data_created_from_dict = BulkAssignPermissions200ResponseDataCreated.from_dict(bulk_assign_permissions200_response_data_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


