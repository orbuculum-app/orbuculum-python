# ToggleFullAccess200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**has_full_access** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.toggle_full_access200_response_data import ToggleFullAccess200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleFullAccess200ResponseData from a JSON string
toggle_full_access200_response_data_instance = ToggleFullAccess200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ToggleFullAccess200ResponseData.to_json())

# convert the object into a dict
toggle_full_access200_response_data_dict = toggle_full_access200_response_data_instance.to_dict()
# create an instance of ToggleFullAccess200ResponseData from a dict
toggle_full_access200_response_data_from_dict = ToggleFullAccess200ResponseData.from_dict(toggle_full_access200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


