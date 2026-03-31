# PreviewImportRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**account_id** | **int** | Target account ID | 
**import_type** | **str** | Import source type | 
**timezone** | **str** | User timezone | [optional] 
**with_already_imported** | **bool** | Include already imported transactions | [optional] 
**check_duplicated** | **bool** | Check for duplicate transactions | [optional] 

## Example

```python
from orbuculum_client.models.preview_import_request1 import PreviewImportRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewImportRequest1 from a JSON string
preview_import_request1_instance = PreviewImportRequest1.from_json(json)
# print the JSON string representation of the object
print(PreviewImportRequest1.to_json())

# convert the object into a dict
preview_import_request1_dict = preview_import_request1_instance.to_dict()
# create an instance of PreviewImportRequest1 from a dict
preview_import_request1_from_dict = PreviewImportRequest1.from_dict(preview_import_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


