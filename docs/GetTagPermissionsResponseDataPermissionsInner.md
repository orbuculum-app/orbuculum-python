# GetTagPermissionsResponseDataPermissionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **int** |  | [optional] 
**level** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_tag_permissions_response_data_permissions_inner import GetTagPermissionsResponseDataPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagPermissionsResponseDataPermissionsInner from a JSON string
get_tag_permissions_response_data_permissions_inner_instance = GetTagPermissionsResponseDataPermissionsInner.from_json(json)
# print the JSON string representation of the object
print(GetTagPermissionsResponseDataPermissionsInner.to_json())

# convert the object into a dict
get_tag_permissions_response_data_permissions_inner_dict = get_tag_permissions_response_data_permissions_inner_instance.to_dict()
# create an instance of GetTagPermissionsResponseDataPermissionsInner from a dict
get_tag_permissions_response_data_permissions_inner_from_dict = GetTagPermissionsResponseDataPermissionsInner.from_dict(get_tag_permissions_response_data_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


