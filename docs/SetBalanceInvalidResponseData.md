# SetBalanceInvalidResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**processed_count** | **int** |  | 

## Example

```python
from orbuculum_client.models.set_balance_invalid_response_data import SetBalanceInvalidResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SetBalanceInvalidResponseData from a JSON string
set_balance_invalid_response_data_instance = SetBalanceInvalidResponseData.from_json(json)
# print the JSON string representation of the object
print(SetBalanceInvalidResponseData.to_json())

# convert the object into a dict
set_balance_invalid_response_data_dict = set_balance_invalid_response_data_instance.to_dict()
# create an instance of SetBalanceInvalidResponseData from a dict
set_balance_invalid_response_data_from_dict = SetBalanceInvalidResponseData.from_dict(set_balance_invalid_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


