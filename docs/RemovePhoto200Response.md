# RemovePhoto200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**RemovePhoto200ResponseData**](RemovePhoto200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.remove_photo200_response import RemovePhoto200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemovePhoto200Response from a JSON string
remove_photo200_response_instance = RemovePhoto200Response.from_json(json)
# print the JSON string representation of the object
print(RemovePhoto200Response.to_json())

# convert the object into a dict
remove_photo200_response_dict = remove_photo200_response_instance.to_dict()
# create an instance of RemovePhoto200Response from a dict
remove_photo200_response_from_dict = RemovePhoto200Response.from_dict(remove_photo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


