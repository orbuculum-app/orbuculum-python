# GetManageAccess200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetManageAccess200ResponseData**](GetManageAccess200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_manage_access200_response import GetManageAccess200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetManageAccess200Response from a JSON string
get_manage_access200_response_instance = GetManageAccess200Response.from_json(json)
# print the JSON string representation of the object
print(GetManageAccess200Response.to_json())

# convert the object into a dict
get_manage_access200_response_dict = get_manage_access200_response_instance.to_dict()
# create an instance of GetManageAccess200Response from a dict
get_manage_access200_response_from_dict = GetManageAccess200Response.from_dict(get_manage_access200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


