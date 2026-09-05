# GetEntityPermissionsResponseDataPermissionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** |  | [optional] 
**level** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_entity_permissions_response_data_permissions_inner import GetEntityPermissionsResponseDataPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityPermissionsResponseDataPermissionsInner from a JSON string
get_entity_permissions_response_data_permissions_inner_instance = GetEntityPermissionsResponseDataPermissionsInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityPermissionsResponseDataPermissionsInner.to_json())

# convert the object into a dict
get_entity_permissions_response_data_permissions_inner_dict = get_entity_permissions_response_data_permissions_inner_instance.to_dict()
# create an instance of GetEntityPermissionsResponseDataPermissionsInner from a dict
get_entity_permissions_response_data_permissions_inner_from_dict = GetEntityPermissionsResponseDataPermissionsInner.from_dict(get_entity_permissions_response_data_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


