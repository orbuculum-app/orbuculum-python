# ResetPasswordResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from orbuculum_client.models.reset_password_response_data import ResetPasswordResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPasswordResponseData from a JSON string
reset_password_response_data_instance = ResetPasswordResponseData.from_json(json)
# print the JSON string representation of the object
print(ResetPasswordResponseData.to_json())

# convert the object into a dict
reset_password_response_data_dict = reset_password_response_data_instance.to_dict()
# create an instance of ResetPasswordResponseData from a dict
reset_password_response_data_from_dict = ResetPasswordResponseData.from_dict(reset_password_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


