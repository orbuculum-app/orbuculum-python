# GetAppContext403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_app_context403_response import GetAppContext403Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppContext403Response from a JSON string
get_app_context403_response_instance = GetAppContext403Response.from_json(json)
# print the JSON string representation of the object
print(GetAppContext403Response.to_json())

# convert the object into a dict
get_app_context403_response_dict = get_app_context403_response_instance.to_dict()
# create an instance of GetAppContext403Response from a dict
get_app_context403_response_from_dict = GetAppContext403Response.from_dict(get_app_context403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


