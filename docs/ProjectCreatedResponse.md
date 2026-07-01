# ProjectCreatedResponse

Response after creating a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | [optional] 
**message** | **str** | Success message | [optional] 
**data** | [**ProjectCreatedResponseData**](ProjectCreatedResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.project_created_response import ProjectCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreatedResponse from a JSON string
project_created_response_instance = ProjectCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectCreatedResponse.to_json())

# convert the object into a dict
project_created_response_dict = project_created_response_instance.to_dict()
# create an instance of ProjectCreatedResponse from a dict
project_created_response_from_dict = ProjectCreatedResponse.from_dict(project_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


