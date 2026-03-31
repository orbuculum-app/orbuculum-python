# DeleteRate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**DeleteRate200ResponseData**](DeleteRate200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.delete_rate200_response import DeleteRate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRate200Response from a JSON string
delete_rate200_response_instance = DeleteRate200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteRate200Response.to_json())

# convert the object into a dict
delete_rate200_response_dict = delete_rate200_response_instance.to_dict()
# create an instance of DeleteRate200Response from a dict
delete_rate200_response_from_dict = DeleteRate200Response.from_dict(delete_rate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


