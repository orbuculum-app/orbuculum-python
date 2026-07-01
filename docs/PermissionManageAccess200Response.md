# PermissionManageAccess200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**PermissionManageAccess200ResponseData**](PermissionManageAccess200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.permission_manage_access200_response import PermissionManageAccess200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionManageAccess200Response from a JSON string
permission_manage_access200_response_instance = PermissionManageAccess200Response.from_json(json)
# print the JSON string representation of the object
print(PermissionManageAccess200Response.to_json())

# convert the object into a dict
permission_manage_access200_response_dict = permission_manage_access200_response_instance.to_dict()
# create an instance of PermissionManageAccess200Response from a dict
permission_manage_access200_response_from_dict = PermissionManageAccess200Response.from_dict(permission_manage_access200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


