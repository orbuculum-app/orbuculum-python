# ToggleFlag200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**permission** | **str** |  | [optional] 
**granted** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.toggle_flag200_response_data import ToggleFlag200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleFlag200ResponseData from a JSON string
toggle_flag200_response_data_instance = ToggleFlag200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ToggleFlag200ResponseData.to_json())

# convert the object into a dict
toggle_flag200_response_data_dict = toggle_flag200_response_data_instance.to_dict()
# create an instance of ToggleFlag200ResponseData from a dict
toggle_flag200_response_data_from_dict = ToggleFlag200ResponseData.from_dict(toggle_flag200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


