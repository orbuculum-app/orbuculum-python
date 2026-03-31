# DeleteTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Tag ID to delete | 

## Example

```python
from orbuculum_client.models.delete_tag_request import DeleteTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTagRequest from a JSON string
delete_tag_request_instance = DeleteTagRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTagRequest.to_json())

# convert the object into a dict
delete_tag_request_dict = delete_tag_request_instance.to_dict()
# create an instance of DeleteTagRequest from a dict
delete_tag_request_from_dict = DeleteTagRequest.from_dict(delete_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


