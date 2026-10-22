# TransactionRulesTableFloor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**subtabs** | **List[str]** |  | 
**slot_class** | **str** |  | 

## Example

```python
from orbuculum_client.models.transaction_rules_table_floor import TransactionRulesTableFloor

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRulesTableFloor from a JSON string
transaction_rules_table_floor_instance = TransactionRulesTableFloor.from_json(json)
# print the JSON string representation of the object
print(TransactionRulesTableFloor.to_json())

# convert the object into a dict
transaction_rules_table_floor_dict = transaction_rules_table_floor_instance.to_dict()
# create an instance of TransactionRulesTableFloor from a dict
transaction_rules_table_floor_from_dict = TransactionRulesTableFloor.from_dict(transaction_rules_table_floor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


