# EmailLinkVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**EmailLinkVerifyResponseData**](EmailLinkVerifyResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.email_link_verify_response import EmailLinkVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailLinkVerifyResponse from a JSON string
email_link_verify_response_instance = EmailLinkVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(EmailLinkVerifyResponse.to_json())

# convert the object into a dict
email_link_verify_response_dict = email_link_verify_response_instance.to_dict()
# create an instance of EmailLinkVerifyResponse from a dict
email_link_verify_response_from_dict = EmailLinkVerifyResponse.from_dict(email_link_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


