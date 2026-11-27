# SignInLinkSentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**SignInLinkSentResponseData**](SignInLinkSentResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.sign_in_link_sent_response import SignInLinkSentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignInLinkSentResponse from a JSON string
sign_in_link_sent_response_instance = SignInLinkSentResponse.from_json(json)
# print the JSON string representation of the object
print(SignInLinkSentResponse.to_json())

# convert the object into a dict
sign_in_link_sent_response_dict = sign_in_link_sent_response_instance.to_dict()
# create an instance of SignInLinkSentResponse from a dict
sign_in_link_sent_response_from_dict = SignInLinkSentResponse.from_dict(sign_in_link_sent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


