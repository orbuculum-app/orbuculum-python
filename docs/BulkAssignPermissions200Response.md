# BulkAssignPermissions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**BulkAssignPermissions200ResponseData**](BulkAssignPermissions200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.bulk_assign_permissions200_response import BulkAssignPermissions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignPermissions200Response from a JSON string
bulk_assign_permissions200_response_instance = BulkAssignPermissions200Response.from_json(json)
# print the JSON string representation of the object
print(BulkAssignPermissions200Response.to_json())

# convert the object into a dict
bulk_assign_permissions200_response_dict = bulk_assign_permissions200_response_instance.to_dict()
# create an instance of BulkAssignPermissions200Response from a dict
bulk_assign_permissions200_response_from_dict = BulkAssignPermissions200Response.from_dict(bulk_assign_permissions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


