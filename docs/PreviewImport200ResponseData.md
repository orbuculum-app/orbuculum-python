# PreviewImport200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_key** | **str** |  | [optional] 
**has_transactions** | **bool** |  | [optional] 
**source_type** | **str** |  | [optional] 
**target_account_id** | **int** |  | [optional] 
**target_hash** | **str** |  | [optional] 
**stat** | **object** |  | [optional] 

## Example

```python
from orbuculum_client.models.preview_import200_response_data import PreviewImport200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewImport200ResponseData from a JSON string
preview_import200_response_data_instance = PreviewImport200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PreviewImport200ResponseData.to_json())

# convert the object into a dict
preview_import200_response_data_dict = preview_import200_response_data_instance.to_dict()
# create an instance of PreviewImport200ResponseData from a dict
preview_import200_response_data_from_dict = PreviewImport200ResponseData.from_dict(preview_import200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


