# GetUserWorkspaces200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetUserWorkspaces200ResponseData**](GetUserWorkspaces200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_user_workspaces200_response import GetUserWorkspaces200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserWorkspaces200Response from a JSON string
get_user_workspaces200_response_instance = GetUserWorkspaces200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserWorkspaces200Response.to_json())

# convert the object into a dict
get_user_workspaces200_response_dict = get_user_workspaces200_response_instance.to_dict()
# create an instance of GetUserWorkspaces200Response from a dict
get_user_workspaces200_response_from_dict = GetUserWorkspaces200Response.from_dict(get_user_workspaces200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


