# GetProjectsResponseData

Project data - array when getting all projects, object when getting by ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project ID | 
**name** | **str** | Project name | 
**color** | **str** | Project colour name | 
**icon** | **str** | Project icon name | 
**is_default** | **bool** | Whether this is a default project | 

## Example

```python
from orbuculum_client.models.get_projects_response_data import GetProjectsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectsResponseData from a JSON string
get_projects_response_data_instance = GetProjectsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetProjectsResponseData.to_json())

# convert the object into a dict
get_projects_response_data_dict = get_projects_response_data_instance.to_dict()
# create an instance of GetProjectsResponseData from a dict
get_projects_response_data_from_dict = GetProjectsResponseData.from_dict(get_projects_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


