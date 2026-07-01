# BalanceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction ID to patch | 
**sender_balance_after** | **str** | New sender balance after the transaction. Decimal serialized as string to preserve precision; null when not computed. | [optional] 
**receiver_balance_after** | **str** | New receiver balance after the transaction. Decimal serialized as string to preserve precision; null when not computed. | [optional] 

## Example

```python
from orbuculum_client.models.balance_update import BalanceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceUpdate from a JSON string
balance_update_instance = BalanceUpdate.from_json(json)
# print the JSON string representation of the object
print(BalanceUpdate.to_json())

# convert the object into a dict
balance_update_dict = balance_update_instance.to_dict()
# create an instance of BalanceUpdate from a dict
balance_update_from_dict = BalanceUpdate.from_dict(balance_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


