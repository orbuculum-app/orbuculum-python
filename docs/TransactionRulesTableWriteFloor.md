# TransactionRulesTableWriteFloor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_subtabs** | **List[str]** |  | 
**classes** | [**Dict[str, TransactionRulesTableWriteFloorClassesValue]**](TransactionRulesTableWriteFloorClassesValue.md) |  | 
**forbidden_slot_classes** | **Dict[str, Dict[str, str]]** | Slot → (class → rule id) | 
**forbidden_pairs** | [**List[TransactionRulesTableWriteFloorForbiddenPairsInner]**](TransactionRulesTableWriteFloorForbiddenPairsInner.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_rules_table_write_floor import TransactionRulesTableWriteFloor

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRulesTableWriteFloor from a JSON string
transaction_rules_table_write_floor_instance = TransactionRulesTableWriteFloor.from_json(json)
# print the JSON string representation of the object
print(TransactionRulesTableWriteFloor.to_json())

# convert the object into a dict
transaction_rules_table_write_floor_dict = transaction_rules_table_write_floor_instance.to_dict()
# create an instance of TransactionRulesTableWriteFloor from a dict
transaction_rules_table_write_floor_from_dict = TransactionRulesTableWriteFloor.from_dict(transaction_rules_table_write_floor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


