# ToggleFlag200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**ToggleFlag200ResponseData**](ToggleFlag200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.toggle_flag200_response import ToggleFlag200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleFlag200Response from a JSON string
toggle_flag200_response_instance = ToggleFlag200Response.from_json(json)
# print the JSON string representation of the object
print(ToggleFlag200Response.to_json())

# convert the object into a dict
toggle_flag200_response_dict = toggle_flag200_response_instance.to_dict()
# create an instance of ToggleFlag200Response from a dict
toggle_flag200_response_from_dict = ToggleFlag200Response.from_dict(toggle_flag200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


