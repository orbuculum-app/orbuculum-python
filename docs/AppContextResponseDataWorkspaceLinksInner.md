# AppContextResponseDataWorkspaceLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**icon_key** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.app_context_response_data_workspace_links_inner import AppContextResponseDataWorkspaceLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of AppContextResponseDataWorkspaceLinksInner from a JSON string
app_context_response_data_workspace_links_inner_instance = AppContextResponseDataWorkspaceLinksInner.from_json(json)
# print the JSON string representation of the object
print(AppContextResponseDataWorkspaceLinksInner.to_json())

# convert the object into a dict
app_context_response_data_workspace_links_inner_dict = app_context_response_data_workspace_links_inner_instance.to_dict()
# create an instance of AppContextResponseDataWorkspaceLinksInner from a dict
app_context_response_data_workspace_links_inner_from_dict = AppContextResponseDataWorkspaceLinksInner.from_dict(app_context_response_data_workspace_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


