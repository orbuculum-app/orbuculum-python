# SetTimezone200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**SetTimezone200ResponseData**](SetTimezone200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.set_timezone200_response import SetTimezone200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetTimezone200Response from a JSON string
set_timezone200_response_instance = SetTimezone200Response.from_json(json)
# print the JSON string representation of the object
print(SetTimezone200Response.to_json())

# convert the object into a dict
set_timezone200_response_dict = set_timezone200_response_instance.to_dict()
# create an instance of SetTimezone200Response from a dict
set_timezone200_response_from_dict = SetTimezone200Response.from_dict(set_timezone200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


