# GetSelectionTree200ResponseDataTreeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**icon_html** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**children** | [**List[GetSelectionTree200ResponseDataTreeInnerChildrenInner]**](GetSelectionTree200ResponseDataTreeInnerChildrenInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_selection_tree200_response_data_tree_inner import GetSelectionTree200ResponseDataTreeInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelectionTree200ResponseDataTreeInner from a JSON string
get_selection_tree200_response_data_tree_inner_instance = GetSelectionTree200ResponseDataTreeInner.from_json(json)
# print the JSON string representation of the object
print(GetSelectionTree200ResponseDataTreeInner.to_json())

# convert the object into a dict
get_selection_tree200_response_data_tree_inner_dict = get_selection_tree200_response_data_tree_inner_instance.to_dict()
# create an instance of GetSelectionTree200ResponseDataTreeInner from a dict
get_selection_tree200_response_data_tree_inner_from_dict = GetSelectionTree200ResponseDataTreeInner.from_dict(get_selection_tree200_response_data_tree_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


