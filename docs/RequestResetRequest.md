# RequestResetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from orbuculum_client.models.request_reset_request import RequestResetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestResetRequest from a JSON string
request_reset_request_instance = RequestResetRequest.from_json(json)
# print the JSON string representation of the object
print(RequestResetRequest.to_json())

# convert the object into a dict
request_reset_request_dict = request_reset_request_instance.to_dict()
# create an instance of RequestResetRequest from a dict
request_reset_request_from_dict = RequestResetRequest.from_dict(request_reset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


