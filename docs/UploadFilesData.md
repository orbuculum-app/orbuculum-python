# UploadFilesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[TransactionFile]**](TransactionFile.md) | Array of uploaded file metadata | 

## Example

```python
from orbuculum_client.models.upload_files_data import UploadFilesData

# TODO update the JSON string below
json = "{}"
# create an instance of UploadFilesData from a JSON string
upload_files_data_instance = UploadFilesData.from_json(json)
# print the JSON string representation of the object
print(UploadFilesData.to_json())

# convert the object into a dict
upload_files_data_dict = upload_files_data_instance.to_dict()
# create an instance of UploadFilesData from a dict
upload_files_data_from_dict = UploadFilesData.from_dict(upload_files_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


