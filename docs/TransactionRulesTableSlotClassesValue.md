# TransactionRulesTableSlotClassesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **List[int]** | Admitted account types; null &#x3D; no type test | 
**sources** | **List[str]** | Admitted account sources; null &#x3D; no source test, [] &#x3D; none required | 

## Example

```python
from orbuculum_client.models.transaction_rules_table_slot_classes_value import TransactionRulesTableSlotClassesValue

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRulesTableSlotClassesValue from a JSON string
transaction_rules_table_slot_classes_value_instance = TransactionRulesTableSlotClassesValue.from_json(json)
# print the JSON string representation of the object
print(TransactionRulesTableSlotClassesValue.to_json())

# convert the object into a dict
transaction_rules_table_slot_classes_value_dict = transaction_rules_table_slot_classes_value_instance.to_dict()
# create an instance of TransactionRulesTableSlotClassesValue from a dict
transaction_rules_table_slot_classes_value_from_dict = TransactionRulesTableSlotClassesValue.from_dict(transaction_rules_table_slot_classes_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


