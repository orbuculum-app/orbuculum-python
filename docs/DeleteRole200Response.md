# DeleteRole200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**DeleteRole200ResponseData**](DeleteRole200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.delete_role200_response import DeleteRole200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRole200Response from a JSON string
delete_role200_response_instance = DeleteRole200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteRole200Response.to_json())

# convert the object into a dict
delete_role200_response_dict = delete_role200_response_instance.to_dict()
# create an instance of DeleteRole200Response from a dict
delete_role200_response_from_dict = DeleteRole200Response.from_dict(delete_role200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


