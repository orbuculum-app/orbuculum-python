# GetProjectsResponse

Response containing project data (array of projects or single project object)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | [optional] 
**data** | [**GetProjectsResponseData**](GetProjectsResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_projects_response import GetProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectsResponse from a JSON string
get_projects_response_instance = GetProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(GetProjectsResponse.to_json())

# convert the object into a dict
get_projects_response_dict = get_projects_response_instance.to_dict()
# create an instance of GetProjectsResponse from a dict
get_projects_response_from_dict = GetProjectsResponse.from_dict(get_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


