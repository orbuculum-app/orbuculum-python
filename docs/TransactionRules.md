# TransactionRules

BE-150: the transaction modal's rules, published verbatim: the account-eligibility table (config/transaction-rules.php) and the sub-tab vocabulary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | [**TransactionRulesTable**](TransactionRulesTable.md) |  | 
**vocabulary** | [**TransactionRulesVocabulary**](TransactionRulesVocabulary.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_rules import TransactionRules

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRules from a JSON string
transaction_rules_instance = TransactionRules.from_json(json)
# print the JSON string representation of the object
print(TransactionRules.to_json())

# convert the object into a dict
transaction_rules_dict = transaction_rules_instance.to_dict()
# create an instance of TransactionRules from a dict
transaction_rules_from_dict = TransactionRules.from_dict(transaction_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


