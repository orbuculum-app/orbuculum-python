# SystemErrorLog200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**SystemErrorLog200ResponseData**](SystemErrorLog200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.system_error_log200_response import SystemErrorLog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemErrorLog200Response from a JSON string
system_error_log200_response_instance = SystemErrorLog200Response.from_json(json)
# print the JSON string representation of the object
print(SystemErrorLog200Response.to_json())

# convert the object into a dict
system_error_log200_response_dict = system_error_log200_response_instance.to_dict()
# create an instance of SystemErrorLog200Response from a dict
system_error_log200_response_from_dict = SystemErrorLog200Response.from_dict(system_error_log200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


