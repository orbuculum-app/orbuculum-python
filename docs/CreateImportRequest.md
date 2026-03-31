# CreateImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**account_id** | **int** | Target account ID | 
**import_key** | **str** | Import key from preview step | 
**timezone** | **str** | User timezone | [optional] 
**source_type** | **str** | Import source type | [optional] 
**target_account_id** | **int** | Target account ID for AccountAssociation | [optional] 
**target_hash** | **str** | Target hash for AccountAssociation (blockchain address) | [optional] 
**data** | **object** | Last-minute edits keyed by transaction ID | [optional] 

## Example

```python
from orbuculum_client.models.create_import_request import CreateImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImportRequest from a JSON string
create_import_request_instance = CreateImportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateImportRequest.to_json())

# convert the object into a dict
create_import_request_dict = create_import_request_instance.to_dict()
# create an instance of CreateImportRequest from a dict
create_import_request_from_dict = CreateImportRequest.from_dict(create_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


