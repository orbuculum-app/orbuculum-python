# GetRecalculatedBalancesResponse

Balance recalculation status per account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**GetRecalculatedBalancesResponseData**](GetRecalculatedBalancesResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.get_recalculated_balances_response import GetRecalculatedBalancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecalculatedBalancesResponse from a JSON string
get_recalculated_balances_response_instance = GetRecalculatedBalancesResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecalculatedBalancesResponse.to_json())

# convert the object into a dict
get_recalculated_balances_response_dict = get_recalculated_balances_response_instance.to_dict()
# create an instance of GetRecalculatedBalancesResponse from a dict
get_recalculated_balances_response_from_dict = GetRecalculatedBalancesResponse.from_dict(get_recalculated_balances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


