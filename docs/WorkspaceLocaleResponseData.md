# WorkspaceLocaleResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | BE-230: the workspace locale as stored; null when cleared | 

## Example

```python
from orbuculum_client.models.workspace_locale_response_data import WorkspaceLocaleResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceLocaleResponseData from a JSON string
workspace_locale_response_data_instance = WorkspaceLocaleResponseData.from_json(json)
# print the JSON string representation of the object
print(WorkspaceLocaleResponseData.to_json())

# convert the object into a dict
workspace_locale_response_data_dict = workspace_locale_response_data_instance.to_dict()
# create an instance of WorkspaceLocaleResponseData from a dict
workspace_locale_response_data_from_dict = WorkspaceLocaleResponseData.from_dict(workspace_locale_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


