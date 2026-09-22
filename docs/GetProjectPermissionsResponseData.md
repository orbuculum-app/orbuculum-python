# GetProjectPermissionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Target member (echo of the user_id query param) | [optional] 
**permissions** | [**List[GetProjectPermissionsResponseDataPermissionsInner]**](GetProjectPermissionsResponseDataPermissionsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_project_permissions_response_data import GetProjectPermissionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectPermissionsResponseData from a JSON string
get_project_permissions_response_data_instance = GetProjectPermissionsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetProjectPermissionsResponseData.to_json())

# convert the object into a dict
get_project_permissions_response_data_dict = get_project_permissions_response_data_instance.to_dict()
# create an instance of GetProjectPermissionsResponseData from a dict
get_project_permissions_response_data_from_dict = GetProjectPermissionsResponseData.from_dict(get_project_permissions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


