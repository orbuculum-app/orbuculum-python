# UploadFilesResponse

Response after successfully uploading files to a transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**UploadFilesData**](UploadFilesData.md) |  | 

## Example

```python
from orbuculum_client.models.upload_files_response import UploadFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadFilesResponse from a JSON string
upload_files_response_instance = UploadFilesResponse.from_json(json)
# print the JSON string representation of the object
print(UploadFilesResponse.to_json())

# convert the object into a dict
upload_files_response_dict = upload_files_response_instance.to_dict()
# create an instance of UploadFilesResponse from a dict
upload_files_response_from_dict = UploadFilesResponse.from_dict(upload_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


