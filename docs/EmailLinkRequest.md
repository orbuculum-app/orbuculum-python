# EmailLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**remember** | **bool** | Keep the browser session for 30 days instead of 2 hours | [optional] 
**return_to** | **str** | Same-origin relative path to open after sign-in; any other value is dropped silently | [optional] 

## Example

```python
from orbuculum_client.models.email_link_request import EmailLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailLinkRequest from a JSON string
email_link_request_instance = EmailLinkRequest.from_json(json)
# print the JSON string representation of the object
print(EmailLinkRequest.to_json())

# convert the object into a dict
email_link_request_dict = email_link_request_instance.to_dict()
# create an instance of EmailLinkRequest from a dict
email_link_request_from_dict = EmailLinkRequest.from_dict(email_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


