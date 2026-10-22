# TransactionRulesTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot_classes** | [**Dict[str, TransactionRulesTableSlotClassesValue]**](TransactionRulesTableSlotClassesValue.md) | Slot class → account predicate | 
**subtabs** | [**Dict[str, TransactionRulesTableSubtabsValue]**](TransactionRulesTableSubtabsValue.md) | Sub-tab (incl. edit variants) → slot → slot class | 
**write_floor** | [**TransactionRulesTableWriteFloor**](TransactionRulesTableWriteFloor.md) |  | 
**floor** | [**TransactionRulesTableFloor**](TransactionRulesTableFloor.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_rules_table import TransactionRulesTable

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRulesTable from a JSON string
transaction_rules_table_instance = TransactionRulesTable.from_json(json)
# print the JSON string representation of the object
print(TransactionRulesTable.to_json())

# convert the object into a dict
transaction_rules_table_dict = transaction_rules_table_instance.to_dict()
# create an instance of TransactionRulesTable from a dict
transaction_rules_table_from_dict = TransactionRulesTable.from_dict(transaction_rules_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


