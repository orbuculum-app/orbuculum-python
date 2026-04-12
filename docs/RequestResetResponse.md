# RequestResetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**RequestResetResponseData**](RequestResetResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.request_reset_response import RequestResetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestResetResponse from a JSON string
request_reset_response_instance = RequestResetResponse.from_json(json)
# print the JSON string representation of the object
print(RequestResetResponse.to_json())

# convert the object into a dict
request_reset_response_dict = request_reset_response_instance.to_dict()
# create an instance of RequestResetResponse from a dict
request_reset_response_from_dict = RequestResetResponse.from_dict(request_reset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


