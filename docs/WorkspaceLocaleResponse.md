# WorkspaceLocaleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**WorkspaceLocaleResponseData**](WorkspaceLocaleResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.workspace_locale_response import WorkspaceLocaleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceLocaleResponse from a JSON string
workspace_locale_response_instance = WorkspaceLocaleResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceLocaleResponse.to_json())

# convert the object into a dict
workspace_locale_response_dict = workspace_locale_response_instance.to_dict()
# create an instance of WorkspaceLocaleResponse from a dict
workspace_locale_response_from_dict = WorkspaceLocaleResponse.from_dict(workspace_locale_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


