# SessionRefreshResponse

Response body returned on a successful session refresh

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**SessionRefreshResponseData**](SessionRefreshResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.session_refresh_response import SessionRefreshResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRefreshResponse from a JSON string
session_refresh_response_instance = SessionRefreshResponse.from_json(json)
# print the JSON string representation of the object
print(SessionRefreshResponse.to_json())

# convert the object into a dict
session_refresh_response_dict = session_refresh_response_instance.to_dict()
# create an instance of SessionRefreshResponse from a dict
session_refresh_response_from_dict = SessionRefreshResponse.from_dict(session_refresh_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


