# CreateImport200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported_count** | **int** |  | [optional] 
**date_from** | **str** |  | [optional] 
**date_to** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_import200_response_data import CreateImport200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImport200ResponseData from a JSON string
create_import200_response_data_instance = CreateImport200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateImport200ResponseData.to_json())

# convert the object into a dict
create_import200_response_data_dict = create_import200_response_data_instance.to_dict()
# create an instance of CreateImport200ResponseData from a dict
create_import200_response_data_from_dict = CreateImport200ResponseData.from_dict(create_import200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


