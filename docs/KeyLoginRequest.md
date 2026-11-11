# KeyLoginRequest

Request body signing in with a client connection key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_key** | **str** | The key returned once by /api/client-connection/create. | 

## Example

```python
from orbuculum_client.models.key_login_request import KeyLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeyLoginRequest from a JSON string
key_login_request_instance = KeyLoginRequest.from_json(json)
# print the JSON string representation of the object
print(KeyLoginRequest.to_json())

# convert the object into a dict
key_login_request_dict = key_login_request_instance.to_dict()
# create an instance of KeyLoginRequest from a dict
key_login_request_from_dict = KeyLoginRequest.from_dict(key_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


