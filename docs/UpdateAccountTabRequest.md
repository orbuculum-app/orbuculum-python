# UpdateAccountTabRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**accounts** | [**Dict[str, UpdateAccountTabRequestAccountsValue]**](UpdateAccountTabRequestAccountsValue.md) | Map account_id → settings object | 

## Example

```python
from orbuculum_client.models.update_account_tab_request import UpdateAccountTabRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountTabRequest from a JSON string
update_account_tab_request_instance = UpdateAccountTabRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountTabRequest.to_json())

# convert the object into a dict
update_account_tab_request_dict = update_account_tab_request_instance.to_dict()
# create an instance of UpdateAccountTabRequest from a dict
update_account_tab_request_from_dict = UpdateAccountTabRequest.from_dict(update_account_tab_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


