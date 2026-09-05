# UpdateProjectResponse

Response after updating a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | [optional] 
**data** | [**UpdateProjectResponseData**](UpdateProjectResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.update_project_response import UpdateProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectResponse from a JSON string
update_project_response_instance = UpdateProjectResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectResponse.to_json())

# convert the object into a dict
update_project_response_dict = update_project_response_instance.to_dict()
# create an instance of UpdateProjectResponse from a dict
update_project_response_from_dict = UpdateProjectResponse.from_dict(update_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


