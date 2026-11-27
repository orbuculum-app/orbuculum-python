# EmailLinkVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token from the link&#39;s fragment | 

## Example

```python
from orbuculum_client.models.email_link_verify_request import EmailLinkVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailLinkVerifyRequest from a JSON string
email_link_verify_request_instance = EmailLinkVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(EmailLinkVerifyRequest.to_json())

# convert the object into a dict
email_link_verify_request_dict = email_link_verify_request_instance.to_dict()
# create an instance of EmailLinkVerifyRequest from a dict
email_link_verify_request_from_dict = EmailLinkVerifyRequest.from_dict(email_link_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


