# PreviewImport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**PreviewImport200ResponseData**](PreviewImport200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.preview_import200_response import PreviewImport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewImport200Response from a JSON string
preview_import200_response_instance = PreviewImport200Response.from_json(json)
# print the JSON string representation of the object
print(PreviewImport200Response.to_json())

# convert the object into a dict
preview_import200_response_dict = preview_import200_response_instance.to_dict()
# create an instance of PreviewImport200Response from a dict
preview_import200_response_from_dict = PreviewImport200Response.from_dict(preview_import200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


