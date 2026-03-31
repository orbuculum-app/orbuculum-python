# UpdateImportTable200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UpdateImportTable200ResponseData**](UpdateImportTable200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.update_import_table200_response import UpdateImportTable200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateImportTable200Response from a JSON string
update_import_table200_response_instance = UpdateImportTable200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateImportTable200Response.to_json())

# convert the object into a dict
update_import_table200_response_dict = update_import_table200_response_instance.to_dict()
# create an instance of UpdateImportTable200Response from a dict
update_import_table200_response_from_dict = UpdateImportTable200Response.from_dict(update_import_table200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


