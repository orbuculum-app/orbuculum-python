# EmailLinkVerify415Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**details** | **List[object]** |  | [optional] 

## Example

```python
from orbuculum_client.models.email_link_verify415_response import EmailLinkVerify415Response

# TODO update the JSON string below
json = "{}"
# create an instance of EmailLinkVerify415Response from a JSON string
email_link_verify415_response_instance = EmailLinkVerify415Response.from_json(json)
# print the JSON string representation of the object
print(EmailLinkVerify415Response.to_json())

# convert the object into a dict
email_link_verify415_response_dict = email_link_verify415_response_instance.to_dict()
# create an instance of EmailLinkVerify415Response from a dict
email_link_verify415_response_from_dict = EmailLinkVerify415Response.from_dict(email_link_verify415_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


