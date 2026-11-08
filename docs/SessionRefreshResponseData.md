# SessionRefreshResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Newly issued JWT access token, valid for 1 hour. | 
**refresh_token** | **str** | The rotated refresh token. Replaces the one presented. | 
**refresh_expires_at** | **datetime** | When the session expires unless refreshed before then (ISO 8601 UTC). | 

## Example

```python
from orbuculum_client.models.session_refresh_response_data import SessionRefreshResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRefreshResponseData from a JSON string
session_refresh_response_data_instance = SessionRefreshResponseData.from_json(json)
# print the JSON string representation of the object
print(SessionRefreshResponseData.to_json())

# convert the object into a dict
session_refresh_response_data_dict = session_refresh_response_data_instance.to_dict()
# create an instance of SessionRefreshResponseData from a dict
session_refresh_response_data_from_dict = SessionRefreshResponseData.from_dict(session_refresh_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


