# CapturedSignInLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**CapturedSignInLinkResponseData**](CapturedSignInLinkResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.captured_sign_in_link_response import CapturedSignInLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CapturedSignInLinkResponse from a JSON string
captured_sign_in_link_response_instance = CapturedSignInLinkResponse.from_json(json)
# print the JSON string representation of the object
print(CapturedSignInLinkResponse.to_json())

# convert the object into a dict
captured_sign_in_link_response_dict = captured_sign_in_link_response_instance.to_dict()
# create an instance of CapturedSignInLinkResponse from a dict
captured_sign_in_link_response_from_dict = CapturedSignInLinkResponse.from_dict(captured_sign_in_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


