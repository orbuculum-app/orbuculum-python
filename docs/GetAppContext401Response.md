# GetAppContext401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_app_context401_response import GetAppContext401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppContext401Response from a JSON string
get_app_context401_response_instance = GetAppContext401Response.from_json(json)
# print the JSON string representation of the object
print(GetAppContext401Response.to_json())

# convert the object into a dict
get_app_context401_response_dict = get_app_context401_response_instance.to_dict()
# create an instance of GetAppContext401Response from a dict
get_app_context401_response_from_dict = GetAppContext401Response.from_dict(get_app_context401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


