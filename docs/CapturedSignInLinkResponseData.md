# CapturedSignInLinkResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | 
**token** | **str** | The 43-character token of the link | 
**sent_at** | **datetime** |  | 

## Example

```python
from orbuculum_client.models.captured_sign_in_link_response_data import CapturedSignInLinkResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CapturedSignInLinkResponseData from a JSON string
captured_sign_in_link_response_data_instance = CapturedSignInLinkResponseData.from_json(json)
# print the JSON string representation of the object
print(CapturedSignInLinkResponseData.to_json())

# convert the object into a dict
captured_sign_in_link_response_data_dict = captured_sign_in_link_response_data_instance.to_dict()
# create an instance of CapturedSignInLinkResponseData from a dict
captured_sign_in_link_response_data_from_dict = CapturedSignInLinkResponseData.from_dict(captured_sign_in_link_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


