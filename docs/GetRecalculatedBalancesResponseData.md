# GetRecalculatedBalancesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[GetRecalculatedBalancesResponseDataAccountsInner]**](GetRecalculatedBalancesResponseDataAccountsInner.md) |  | 

## Example

```python
from orbuculum_client.models.get_recalculated_balances_response_data import GetRecalculatedBalancesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecalculatedBalancesResponseData from a JSON string
get_recalculated_balances_response_data_instance = GetRecalculatedBalancesResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRecalculatedBalancesResponseData.to_json())

# convert the object into a dict
get_recalculated_balances_response_data_dict = get_recalculated_balances_response_data_instance.to_dict()
# create an instance of GetRecalculatedBalancesResponseData from a dict
get_recalculated_balances_response_data_from_dict = GetRecalculatedBalancesResponseData.from_dict(get_recalculated_balances_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


