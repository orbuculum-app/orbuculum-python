# SaveWorkspacePreferences200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**SaveWorkspacePreferences200ResponseData**](SaveWorkspacePreferences200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.save_workspace_preferences200_response import SaveWorkspacePreferences200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SaveWorkspacePreferences200Response from a JSON string
save_workspace_preferences200_response_instance = SaveWorkspacePreferences200Response.from_json(json)
# print the JSON string representation of the object
print(SaveWorkspacePreferences200Response.to_json())

# convert the object into a dict
save_workspace_preferences200_response_dict = save_workspace_preferences200_response_instance.to_dict()
# create an instance of SaveWorkspacePreferences200Response from a dict
save_workspace_preferences200_response_from_dict = SaveWorkspacePreferences200Response.from_dict(save_workspace_preferences200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


