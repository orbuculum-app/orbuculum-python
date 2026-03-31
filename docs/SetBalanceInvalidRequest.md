# SetBalanceInvalidRequest

Request body for triggering balance recalculation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**accounts** | [**List[SetBalanceInvalidRequestAccountsInner]**](SetBalanceInvalidRequestAccountsInner.md) | Array of accounts to recalculate (max 100) | 

## Example

```python
from orbuculum_client.models.set_balance_invalid_request import SetBalanceInvalidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBalanceInvalidRequest from a JSON string
set_balance_invalid_request_instance = SetBalanceInvalidRequest.from_json(json)
# print the JSON string representation of the object
print(SetBalanceInvalidRequest.to_json())

# convert the object into a dict
set_balance_invalid_request_dict = set_balance_invalid_request_instance.to_dict()
# create an instance of SetBalanceInvalidRequest from a dict
set_balance_invalid_request_from_dict = SetBalanceInvalidRequest.from_dict(set_balance_invalid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


