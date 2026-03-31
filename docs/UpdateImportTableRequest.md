# UpdateImportTableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**import_key** | **str** | Import key from preview step | 
**chunk** | **int** | Chunk number (1-based) | 
**data** | **object** | Update data keyed by transaction ID | [optional] 

## Example

```python
from orbuculum_client.models.update_import_table_request import UpdateImportTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateImportTableRequest from a JSON string
update_import_table_request_instance = UpdateImportTableRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateImportTableRequest.to_json())

# convert the object into a dict
update_import_table_request_dict = update_import_table_request_instance.to_dict()
# create an instance of UpdateImportTableRequest from a dict
update_import_table_request_from_dict = UpdateImportTableRequest.from_dict(update_import_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


