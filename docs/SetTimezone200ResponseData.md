# SetTimezone200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.set_timezone200_response_data import SetTimezone200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SetTimezone200ResponseData from a JSON string
set_timezone200_response_data_instance = SetTimezone200ResponseData.from_json(json)
# print the JSON string representation of the object
print(SetTimezone200ResponseData.to_json())

# convert the object into a dict
set_timezone200_response_data_dict = set_timezone200_response_data_instance.to_dict()
# create an instance of SetTimezone200ResponseData from a dict
set_timezone200_response_data_from_dict = SetTimezone200ResponseData.from_dict(set_timezone200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


