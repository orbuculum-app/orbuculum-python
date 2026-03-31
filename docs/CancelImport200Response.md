# CancelImport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**CancelImport200ResponseData**](CancelImport200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.cancel_import200_response import CancelImport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CancelImport200Response from a JSON string
cancel_import200_response_instance = CancelImport200Response.from_json(json)
# print the JSON string representation of the object
print(CancelImport200Response.to_json())

# convert the object into a dict
cancel_import200_response_dict = cancel_import200_response_instance.to_dict()
# create an instance of CancelImport200Response from a dict
cancel_import200_response_from_dict = CancelImport200Response.from_dict(cancel_import200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


