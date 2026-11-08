# SessionTokenRequest

Request body carrying the refresh token of a long session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | Refresh token from login or from the last session refresh. | 

## Example

```python
from orbuculum_client.models.session_token_request import SessionTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionTokenRequest from a JSON string
session_token_request_instance = SessionTokenRequest.from_json(json)
# print the JSON string representation of the object
print(SessionTokenRequest.to_json())

# convert the object into a dict
session_token_request_dict = session_token_request_instance.to_dict()
# create an instance of SessionTokenRequest from a dict
session_token_request_from_dict = SessionTokenRequest.from_dict(session_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


