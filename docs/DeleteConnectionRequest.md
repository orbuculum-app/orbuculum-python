# DeleteConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**identifier** | **str** | Connection identifier (id_key) to delete | 

## Example

```python
from orbuculum_client.models.delete_connection_request import DeleteConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteConnectionRequest from a JSON string
delete_connection_request_instance = DeleteConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteConnectionRequest.to_json())

# convert the object into a dict
delete_connection_request_dict = delete_connection_request_instance.to_dict()
# create an instance of DeleteConnectionRequest from a dict
delete_connection_request_from_dict = DeleteConnectionRequest.from_dict(delete_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


