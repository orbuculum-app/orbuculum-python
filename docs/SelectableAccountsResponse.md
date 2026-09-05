# SelectableAccountsResponse

Accounts the transaction modal may offer for one (sub-tab, slot) pair

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**SelectableAccountsResponseData**](SelectableAccountsResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.selectable_accounts_response import SelectableAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelectableAccountsResponse from a JSON string
selectable_accounts_response_instance = SelectableAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(SelectableAccountsResponse.to_json())

# convert the object into a dict
selectable_accounts_response_dict = selectable_accounts_response_instance.to_dict()
# create an instance of SelectableAccountsResponse from a dict
selectable_accounts_response_from_dict = SelectableAccountsResponse.from_dict(selectable_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


