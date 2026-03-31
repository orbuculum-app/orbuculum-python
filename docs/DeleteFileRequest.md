# DeleteFileRequest

Request body for deleting a transaction file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**transaction_id** | **int** | Parent transaction ID | 
**file_id** | **int** | File ID to delete | 

## Example

```python
from orbuculum_client.models.delete_file_request import DeleteFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFileRequest from a JSON string
delete_file_request_instance = DeleteFileRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteFileRequest.to_json())

# convert the object into a dict
delete_file_request_dict = delete_file_request_instance.to_dict()
# create an instance of DeleteFileRequest from a dict
delete_file_request_from_dict = DeleteFileRequest.from_dict(delete_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


