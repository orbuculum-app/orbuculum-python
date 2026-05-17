# GetTagPermissionsResponse

Response containing tag permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | [optional] 
**data** | [**GetTagPermissionsResponseData**](GetTagPermissionsResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_tag_permissions_response import GetTagPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagPermissionsResponse from a JSON string
get_tag_permissions_response_instance = GetTagPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTagPermissionsResponse.to_json())

# convert the object into a dict
get_tag_permissions_response_dict = get_tag_permissions_response_instance.to_dict()
# create an instance of GetTagPermissionsResponse from a dict
get_tag_permissions_response_from_dict = GetTagPermissionsResponse.from_dict(get_tag_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


