# AccountContextResponse

Response containing aggregated account form context data for create or edit mode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**AccountContextResponseData**](AccountContextResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.account_context_response import AccountContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContextResponse from a JSON string
account_context_response_instance = AccountContextResponse.from_json(json)
# print the JSON string representation of the object
print(AccountContextResponse.to_json())

# convert the object into a dict
account_context_response_dict = account_context_response_instance.to_dict()
# create an instance of AccountContextResponse from a dict
account_context_response_from_dict = AccountContextResponse.from_dict(account_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


