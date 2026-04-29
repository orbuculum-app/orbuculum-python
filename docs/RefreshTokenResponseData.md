# RefreshTokenResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Newly issued JWT access token, valid for 1 hour. | 

## Example

```python
from orbuculum_client.models.refresh_token_response_data import RefreshTokenResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenResponseData from a JSON string
refresh_token_response_data_instance = RefreshTokenResponseData.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenResponseData.to_json())

# convert the object into a dict
refresh_token_response_data_dict = refresh_token_response_data_instance.to_dict()
# create an instance of RefreshTokenResponseData from a dict
refresh_token_response_data_from_dict = RefreshTokenResponseData.from_dict(refresh_token_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


