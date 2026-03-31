# SetTimezoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**timezone** | **str** |  | 

## Example

```python
from orbuculum_client.models.set_timezone_request import SetTimezoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTimezoneRequest from a JSON string
set_timezone_request_instance = SetTimezoneRequest.from_json(json)
# print the JSON string representation of the object
print(SetTimezoneRequest.to_json())

# convert the object into a dict
set_timezone_request_dict = set_timezone_request_instance.to_dict()
# create an instance of SetTimezoneRequest from a dict
set_timezone_request_from_dict = SetTimezoneRequest.from_dict(set_timezone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


