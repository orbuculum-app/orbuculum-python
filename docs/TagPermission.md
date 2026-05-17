# TagPermission

Tag (account group) permission object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | Role ID | [optional] 
**permission_id** | **int** | Permission ID | [optional] 
**tag_id** | **int** | Tag (account group) ID | [optional] 
**can_manage** | **bool** | Manage access flag | [optional] 

## Example

```python
from orbuculum_client.models.tag_permission import TagPermission

# TODO update the JSON string below
json = "{}"
# create an instance of TagPermission from a JSON string
tag_permission_instance = TagPermission.from_json(json)
# print the JSON string representation of the object
print(TagPermission.to_json())

# convert the object into a dict
tag_permission_dict = tag_permission_instance.to_dict()
# create an instance of TagPermission from a dict
tag_permission_from_dict = TagPermission.from_dict(tag_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


