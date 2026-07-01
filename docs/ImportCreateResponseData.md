# ImportCreateResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_count** | **int** |  | 
**imported_count** | **int** |  | 
**skipped_count** | **int** |  | 
**transaction_ids** | **List[int]** |  | 
**skipped_rows** | [**List[ImportCreateResponseDataSkippedRowsInner]**](ImportCreateResponseDataSkippedRowsInner.md) |  | 
**date_from** | **str** |  | [optional] 
**date_to** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.import_create_response_data import ImportCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCreateResponseData from a JSON string
import_create_response_data_instance = ImportCreateResponseData.from_json(json)
# print the JSON string representation of the object
print(ImportCreateResponseData.to_json())

# convert the object into a dict
import_create_response_data_dict = import_create_response_data_instance.to_dict()
# create an instance of ImportCreateResponseData from a dict
import_create_response_data_from_dict = ImportCreateResponseData.from_dict(import_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


