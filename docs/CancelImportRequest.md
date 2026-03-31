# CancelImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**import_key** | **str** | Import key from preview step | 

## Example

```python
from orbuculum_client.models.cancel_import_request import CancelImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelImportRequest from a JSON string
cancel_import_request_instance = CancelImportRequest.from_json(json)
# print the JSON string representation of the object
print(CancelImportRequest.to_json())

# convert the object into a dict
cancel_import_request_dict = cancel_import_request_instance.to_dict()
# create an instance of CancelImportRequest from a dict
cancel_import_request_from_dict = CancelImportRequest.from_dict(cancel_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


