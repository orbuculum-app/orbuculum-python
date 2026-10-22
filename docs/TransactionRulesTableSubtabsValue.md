# TransactionRulesTableSubtabsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** |  | 
**receiver** | **str** |  | 
**double** | **str** | Present only on sub-tabs with a double slot | [optional] 

## Example

```python
from orbuculum_client.models.transaction_rules_table_subtabs_value import TransactionRulesTableSubtabsValue

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRulesTableSubtabsValue from a JSON string
transaction_rules_table_subtabs_value_instance = TransactionRulesTableSubtabsValue.from_json(json)
# print the JSON string representation of the object
print(TransactionRulesTableSubtabsValue.to_json())

# convert the object into a dict
transaction_rules_table_subtabs_value_dict = transaction_rules_table_subtabs_value_instance.to_dict()
# create an instance of TransactionRulesTableSubtabsValue from a dict
transaction_rules_table_subtabs_value_from_dict = TransactionRulesTableSubtabsValue.from_dict(transaction_rules_table_subtabs_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


