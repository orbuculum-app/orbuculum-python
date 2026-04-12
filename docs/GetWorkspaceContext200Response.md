# GetWorkspaceContext200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetWorkspaceContext200ResponseData**](GetWorkspaceContext200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_workspace_context200_response import GetWorkspaceContext200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspaceContext200Response from a JSON string
get_workspace_context200_response_instance = GetWorkspaceContext200Response.from_json(json)
# print the JSON string representation of the object
print(GetWorkspaceContext200Response.to_json())

# convert the object into a dict
get_workspace_context200_response_dict = get_workspace_context200_response_instance.to_dict()
# create an instance of GetWorkspaceContext200Response from a dict
get_workspace_context200_response_from_dict = GetWorkspaceContext200Response.from_dict(get_workspace_context200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


