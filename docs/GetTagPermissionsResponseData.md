# GetTagPermissionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_tags** | **bool** | Whether the member&#39;s role can create tags (account groups) | [optional] 
**permissions** | [**List[GetTagPermissionsResponseDataPermissionsInner]**](GetTagPermissionsResponseDataPermissionsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_tag_permissions_response_data import GetTagPermissionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagPermissionsResponseData from a JSON string
get_tag_permissions_response_data_instance = GetTagPermissionsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetTagPermissionsResponseData.to_json())

# convert the object into a dict
get_tag_permissions_response_data_dict = get_tag_permissions_response_data_instance.to_dict()
# create an instance of GetTagPermissionsResponseData from a dict
get_tag_permissions_response_data_from_dict = GetTagPermissionsResponseData.from_dict(get_tag_permissions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


