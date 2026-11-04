# UpdateWorkspaceLocaleRequest

Request body for setting or clearing a workspace's locale

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | ID of the workspace | 
**locale** | **str** | BCP 47 tag with a region subtag (language[-Script]-REGION, e.g. \&quot;en-GB\&quot;, \&quot;sr-Latn-RS\&quot;, \&quot;es-419\&quot;), stored as given; null clears the locale. The key is required. | 

## Example

```python
from orbuculum_client.models.update_workspace_locale_request import UpdateWorkspaceLocaleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceLocaleRequest from a JSON string
update_workspace_locale_request_instance = UpdateWorkspaceLocaleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkspaceLocaleRequest.to_json())

# convert the object into a dict
update_workspace_locale_request_dict = update_workspace_locale_request_instance.to_dict()
# create an instance of UpdateWorkspaceLocaleRequest from a dict
update_workspace_locale_request_from_dict = UpdateWorkspaceLocaleRequest.from_dict(update_workspace_locale_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


