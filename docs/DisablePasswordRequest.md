# DisablePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from orbuculum_client.models.disable_password_request import DisablePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisablePasswordRequest from a JSON string
disable_password_request_instance = DisablePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(DisablePasswordRequest.to_json())

# convert the object into a dict
disable_password_request_dict = disable_password_request_instance.to_dict()
# create an instance of DisablePasswordRequest from a dict
disable_password_request_from_dict = DisablePasswordRequest.from_dict(disable_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


