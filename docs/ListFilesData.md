# ListFilesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[TransactionFile]**](TransactionFile.md) | Array of file metadata for the transaction | 

## Example

```python
from orbuculum_client.models.list_files_data import ListFilesData

# TODO update the JSON string below
json = "{}"
# create an instance of ListFilesData from a JSON string
list_files_data_instance = ListFilesData.from_json(json)
# print the JSON string representation of the object
print(ListFilesData.to_json())

# convert the object into a dict
list_files_data_dict = list_files_data_instance.to_dict()
# create an instance of ListFilesData from a dict
list_files_data_from_dict = ListFilesData.from_dict(list_files_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


