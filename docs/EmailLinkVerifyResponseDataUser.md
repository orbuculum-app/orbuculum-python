# EmailLinkVerifyResponseDataUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**email** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from orbuculum_client.models.email_link_verify_response_data_user import EmailLinkVerifyResponseDataUser

# TODO update the JSON string below
json = "{}"
# create an instance of EmailLinkVerifyResponseDataUser from a JSON string
email_link_verify_response_data_user_instance = EmailLinkVerifyResponseDataUser.from_json(json)
# print the JSON string representation of the object
print(EmailLinkVerifyResponseDataUser.to_json())

# convert the object into a dict
email_link_verify_response_data_user_dict = email_link_verify_response_data_user_instance.to_dict()
# create an instance of EmailLinkVerifyResponseDataUser from a dict
email_link_verify_response_data_user_from_dict = EmailLinkVerifyResponseDataUser.from_dict(email_link_verify_response_data_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


