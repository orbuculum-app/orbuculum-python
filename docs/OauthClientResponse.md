# OauthClientResponse

One OAuth client registration held for the MCP server (BE-332); never carries the client secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**OauthClientResponseData**](OauthClientResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.oauth_client_response import OauthClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientResponse from a JSON string
oauth_client_response_instance = OauthClientResponse.from_json(json)
# print the JSON string representation of the object
print(OauthClientResponse.to_json())

# convert the object into a dict
oauth_client_response_dict = oauth_client_response_instance.to_dict()
# create an instance of OauthClientResponse from a dict
oauth_client_response_from_dict = OauthClientResponse.from_dict(oauth_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


