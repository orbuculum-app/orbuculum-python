# SetLocaleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | 

## Example

```python
from orbuculum_client.models.set_locale_request import SetLocaleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetLocaleRequest from a JSON string
set_locale_request_instance = SetLocaleRequest.from_json(json)
# print the JSON string representation of the object
print(SetLocaleRequest.to_json())

# convert the object into a dict
set_locale_request_dict = set_locale_request_instance.to_dict()
# create an instance of SetLocaleRequest from a dict
set_locale_request_from_dict = SetLocaleRequest.from_dict(set_locale_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


