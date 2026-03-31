# ToggleFullAccess200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**ToggleFullAccess200ResponseData**](ToggleFullAccess200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.toggle_full_access200_response import ToggleFullAccess200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleFullAccess200Response from a JSON string
toggle_full_access200_response_instance = ToggleFullAccess200Response.from_json(json)
# print the JSON string representation of the object
print(ToggleFullAccess200Response.to_json())

# convert the object into a dict
toggle_full_access200_response_dict = toggle_full_access200_response_instance.to_dict()
# create an instance of ToggleFullAccess200Response from a dict
toggle_full_access200_response_from_dict = ToggleFullAccess200Response.from_dict(toggle_full_access200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


