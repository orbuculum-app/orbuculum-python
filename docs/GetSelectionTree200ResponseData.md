# GetSelectionTree200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection_type** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**tree** | [**List[GetSelectionTree200ResponseDataTreeInner]**](GetSelectionTree200ResponseDataTreeInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_selection_tree200_response_data import GetSelectionTree200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelectionTree200ResponseData from a JSON string
get_selection_tree200_response_data_instance = GetSelectionTree200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetSelectionTree200ResponseData.to_json())

# convert the object into a dict
get_selection_tree200_response_data_dict = get_selection_tree200_response_data_instance.to_dict()
# create an instance of GetSelectionTree200ResponseData from a dict
get_selection_tree200_response_data_from_dict = GetSelectionTree200ResponseData.from_dict(get_selection_tree200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


