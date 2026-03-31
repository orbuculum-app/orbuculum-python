# DisconnectSocialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Social auth provider to disconnect | 

## Example

```python
from orbuculum_client.models.disconnect_social_request import DisconnectSocialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectSocialRequest from a JSON string
disconnect_social_request_instance = DisconnectSocialRequest.from_json(json)
# print the JSON string representation of the object
print(DisconnectSocialRequest.to_json())

# convert the object into a dict
disconnect_social_request_dict = disconnect_social_request_instance.to_dict()
# create an instance of DisconnectSocialRequest from a dict
disconnect_social_request_from_dict = DisconnectSocialRequest.from_dict(disconnect_social_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


