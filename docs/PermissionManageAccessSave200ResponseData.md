# PermissionManageAccessSave200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**updated_users** | **int** |  | [optional] 
**removed_users** | **int** |  | [optional] 
**skipped_users** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.permission_manage_access_save200_response_data import PermissionManageAccessSave200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionManageAccessSave200ResponseData from a JSON string
permission_manage_access_save200_response_data_instance = PermissionManageAccessSave200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PermissionManageAccessSave200ResponseData.to_json())

# convert the object into a dict
permission_manage_access_save200_response_data_dict = permission_manage_access_save200_response_data_instance.to_dict()
# create an instance of PermissionManageAccessSave200ResponseData from a dict
permission_manage_access_save200_response_data_from_dict = PermissionManageAccessSave200ResponseData.from_dict(permission_manage_access_save200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


