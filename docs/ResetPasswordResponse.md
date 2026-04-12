# ResetPasswordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**ResetPasswordResponseData**](ResetPasswordResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.reset_password_response import ResetPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPasswordResponse from a JSON string
reset_password_response_instance = ResetPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(ResetPasswordResponse.to_json())

# convert the object into a dict
reset_password_response_dict = reset_password_response_instance.to_dict()
# create an instance of ResetPasswordResponse from a dict
reset_password_response_from_dict = ResetPasswordResponse.from_dict(reset_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


