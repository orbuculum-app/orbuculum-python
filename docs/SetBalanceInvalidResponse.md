# SetBalanceInvalidResponse

Response after successful balance recalculation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**SetBalanceInvalidResponseData**](SetBalanceInvalidResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.set_balance_invalid_response import SetBalanceInvalidResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetBalanceInvalidResponse from a JSON string
set_balance_invalid_response_instance = SetBalanceInvalidResponse.from_json(json)
# print the JSON string representation of the object
print(SetBalanceInvalidResponse.to_json())

# convert the object into a dict
set_balance_invalid_response_dict = set_balance_invalid_response_instance.to_dict()
# create an instance of SetBalanceInvalidResponse from a dict
set_balance_invalid_response_from_dict = SetBalanceInvalidResponse.from_dict(set_balance_invalid_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


