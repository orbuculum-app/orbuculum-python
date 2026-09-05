# UpdateProjectResponseData

Updated project data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project ID | 
**name** | **str** | Project name | 
**color** | **str** | Project colour name | 
**icon** | **str** | Project icon name | 
**is_default** | **bool** | Whether this is a default project | 
**message** | **str** | Success message | [optional] 

## Example

```python
from orbuculum_client.models.update_project_response_data import UpdateProjectResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectResponseData from a JSON string
update_project_response_data_instance = UpdateProjectResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectResponseData.to_json())

# convert the object into a dict
update_project_response_data_dict = update_project_response_data_instance.to_dict()
# create an instance of UpdateProjectResponseData from a dict
update_project_response_data_from_dict = UpdateProjectResponseData.from_dict(update_project_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


