# PermissionToggleFullAccess200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**PermissionToggleFullAccess200ResponseData**](PermissionToggleFullAccess200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.permission_toggle_full_access200_response import PermissionToggleFullAccess200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionToggleFullAccess200Response from a JSON string
permission_toggle_full_access200_response_instance = PermissionToggleFullAccess200Response.from_json(json)
# print the JSON string representation of the object
print(PermissionToggleFullAccess200Response.to_json())

# convert the object into a dict
permission_toggle_full_access200_response_dict = permission_toggle_full_access200_response_instance.to_dict()
# create an instance of PermissionToggleFullAccess200Response from a dict
permission_toggle_full_access200_response_from_dict = PermissionToggleFullAccess200Response.from_dict(permission_toggle_full_access200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


