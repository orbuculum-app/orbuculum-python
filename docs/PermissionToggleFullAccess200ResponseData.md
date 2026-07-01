# PermissionToggleFullAccess200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**has_full_access** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.permission_toggle_full_access200_response_data import PermissionToggleFullAccess200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionToggleFullAccess200ResponseData from a JSON string
permission_toggle_full_access200_response_data_instance = PermissionToggleFullAccess200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PermissionToggleFullAccess200ResponseData.to_json())

# convert the object into a dict
permission_toggle_full_access200_response_data_dict = permission_toggle_full_access200_response_data_instance.to_dict()
# create an instance of PermissionToggleFullAccess200ResponseData from a dict
permission_toggle_full_access200_response_data_from_dict = PermissionToggleFullAccess200ResponseData.from_dict(permission_toggle_full_access200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


