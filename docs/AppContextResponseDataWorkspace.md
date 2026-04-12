# AppContextResponseDataWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**links** | [**List[AppContextResponseDataReportsInner]**](AppContextResponseDataReportsInner.md) |  | [optional] 
**projects** | [**List[AppContextResponseDataWorkspaceProjectsInner]**](AppContextResponseDataWorkspaceProjectsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.app_context_response_data_workspace import AppContextResponseDataWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of AppContextResponseDataWorkspace from a JSON string
app_context_response_data_workspace_instance = AppContextResponseDataWorkspace.from_json(json)
# print the JSON string representation of the object
print(AppContextResponseDataWorkspace.to_json())

# convert the object into a dict
app_context_response_data_workspace_dict = app_context_response_data_workspace_instance.to_dict()
# create an instance of AppContextResponseDataWorkspace from a dict
app_context_response_data_workspace_from_dict = AppContextResponseDataWorkspace.from_dict(app_context_response_data_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


