# SaveWorkspacePreferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**type** | **str** |  | 
**settings** | **object** | Report view blob, stored per user and report type. &#x60;period&#x60;, when present, must be a period-kind word (the same vocabulary as the reports&#39; &#x60;range&#x60;), otherwise 400; it is stored as the report engine code and echoed back as sent. Other keys are stored as sent. | 

## Example

```python
from orbuculum_client.models.save_workspace_preferences_request import SaveWorkspacePreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveWorkspacePreferencesRequest from a JSON string
save_workspace_preferences_request_instance = SaveWorkspacePreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(SaveWorkspacePreferencesRequest.to_json())

# convert the object into a dict
save_workspace_preferences_request_dict = save_workspace_preferences_request_instance.to_dict()
# create an instance of SaveWorkspacePreferencesRequest from a dict
save_workspace_preferences_request_from_dict = SaveWorkspacePreferencesRequest.from_dict(save_workspace_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


