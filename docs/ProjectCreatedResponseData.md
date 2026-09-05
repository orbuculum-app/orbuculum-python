# ProjectCreatedResponseData

Created project data

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
from orbuculum_client.models.project_created_response_data import ProjectCreatedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreatedResponseData from a JSON string
project_created_response_data_instance = ProjectCreatedResponseData.from_json(json)
# print the JSON string representation of the object
print(ProjectCreatedResponseData.to_json())

# convert the object into a dict
project_created_response_data_dict = project_created_response_data_instance.to_dict()
# create an instance of ProjectCreatedResponseData from a dict
project_created_response_data_from_dict = ProjectCreatedResponseData.from_dict(project_created_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


