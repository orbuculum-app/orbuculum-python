# EmailLinkVerifyResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**new_account** | **bool** | True when this link created the account | 
**return_to** | **str** |  | 
**user** | [**EmailLinkVerifyResponseDataUser**](EmailLinkVerifyResponseDataUser.md) |  | 

## Example

```python
from orbuculum_client.models.email_link_verify_response_data import EmailLinkVerifyResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EmailLinkVerifyResponseData from a JSON string
email_link_verify_response_data_instance = EmailLinkVerifyResponseData.from_json(json)
# print the JSON string representation of the object
print(EmailLinkVerifyResponseData.to_json())

# convert the object into a dict
email_link_verify_response_data_dict = email_link_verify_response_data_instance.to_dict()
# create an instance of EmailLinkVerifyResponseData from a dict
email_link_verify_response_data_from_dict = EmailLinkVerifyResponseData.from_dict(email_link_verify_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


