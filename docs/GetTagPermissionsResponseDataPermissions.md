# GetTagPermissionsResponseDataPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | [**List[TagPermission]**](TagPermission.md) | Read permissions | [optional] 
**manage** | [**List[TagPermission]**](TagPermission.md) | Manage permissions | [optional] 

## Example

```python
from orbuculum_client.models.get_tag_permissions_response_data_permissions import GetTagPermissionsResponseDataPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagPermissionsResponseDataPermissions from a JSON string
get_tag_permissions_response_data_permissions_instance = GetTagPermissionsResponseDataPermissions.from_json(json)
# print the JSON string representation of the object
print(GetTagPermissionsResponseDataPermissions.to_json())

# convert the object into a dict
get_tag_permissions_response_data_permissions_dict = get_tag_permissions_response_data_permissions_instance.to_dict()
# create an instance of GetTagPermissionsResponseDataPermissions from a dict
get_tag_permissions_response_data_permissions_from_dict = GetTagPermissionsResponseDataPermissions.from_dict(get_tag_permissions_response_data_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


