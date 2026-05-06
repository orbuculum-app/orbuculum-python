# GetGeneralPermissionsResponse

Response wrapper for GET /api/permission/general

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetGeneralPermissionsResponseData**](GetGeneralPermissionsResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_general_permissions_response import GetGeneralPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGeneralPermissionsResponse from a JSON string
get_general_permissions_response_instance = GetGeneralPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetGeneralPermissionsResponse.to_json())

# convert the object into a dict
get_general_permissions_response_dict = get_general_permissions_response_instance.to_dict()
# create an instance of GetGeneralPermissionsResponse from a dict
get_general_permissions_response_from_dict = GetGeneralPermissionsResponse.from_dict(get_general_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


