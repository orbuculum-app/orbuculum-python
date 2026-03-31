# BulkAssignPermissions200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**created** | [**BulkAssignPermissions200ResponseDataCreated**](BulkAssignPermissions200ResponseDataCreated.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions200_response_data import BulkAssignPermissions200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissions200ResponseData from a JSON string
bulk_assign_permissions200_response_data_instance = BulkAssignPermissions200ResponseData.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissions200ResponseData.to_json())

# convert the object into a dict
bulk_assign_permissions200_response_data_dict = bulk_assign_permissions200_response_data_instance.to_dict()
# create an instance of BulkAssignPermissions200ResponseData from a dict
bulk_assign_permissions200_response_data_from_dict = BulkAssignPermissions200ResponseData.from_dict(bulk_assign_permissions200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


