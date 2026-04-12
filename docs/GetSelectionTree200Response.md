# GetSelectionTree200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetSelectionTree200ResponseData**](GetSelectionTree200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_selection_tree200_response import GetSelectionTree200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelectionTree200Response from a JSON string
get_selection_tree200_response_instance = GetSelectionTree200Response.from_json(json)
# print the JSON string representation of the object
print(GetSelectionTree200Response.to_json())

# convert the object into a dict
get_selection_tree200_response_dict = get_selection_tree200_response_instance.to_dict()
# create an instance of GetSelectionTree200Response from a dict
get_selection_tree200_response_from_dict = GetSelectionTree200Response.from_dict(get_selection_tree200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


