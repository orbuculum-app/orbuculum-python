# OauthClientResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**registration** | **Dict[str, object]** | the registration document without client_secret | 
**client_secret_sha256** | **str** | sha256 hex of the client secret; null for public clients | 
**created_at** | **datetime** | When the client was registered (ISO 8601 UTC). | 

## Example

```python
from orbuculum_client.models.oauth_client_response_data import OauthClientResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientResponseData from a JSON string
oauth_client_response_data_instance = OauthClientResponseData.from_json(json)
# print the JSON string representation of the object
print(OauthClientResponseData.to_json())

# convert the object into a dict
oauth_client_response_data_dict = oauth_client_response_data_instance.to_dict()
# create an instance of OauthClientResponseData from a dict
oauth_client_response_data_from_dict = OauthClientResponseData.from_dict(oauth_client_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


