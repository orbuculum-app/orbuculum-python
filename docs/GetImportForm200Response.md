# GetImportForm200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetImportForm200ResponseData**](GetImportForm200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_import_form200_response import GetImportForm200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImportForm200Response from a JSON string
get_import_form200_response_instance = GetImportForm200Response.from_json(json)
# print the JSON string representation of the object
print(GetImportForm200Response.to_json())

# convert the object into a dict
get_import_form200_response_dict = get_import_form200_response_instance.to_dict()
# create an instance of GetImportForm200Response from a dict
get_import_form200_response_from_dict = GetImportForm200Response.from_dict(get_import_form200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


