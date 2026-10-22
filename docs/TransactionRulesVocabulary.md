# TransactionRulesVocabulary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidates** | **List[str]** | The twelve sub-tabs in fixed DOM order | 
**base_subtabs** | **Dict[str, List[str]]** | Tab → its base sub-tabs, in DOM order | 
**double_variants** | **Dict[str, str]** | Base sub-tab → its double variant | 
**label_buckets** | **Dict[str, str]** | Sub-tab → preferred-label bucket | 
**subtab_tabs** | **Dict[str, str]** | Sub-tab → its tab (bucket any → tab custom) | 

## Example

```python
from orbuculum_client.models.transaction_rules_vocabulary import TransactionRulesVocabulary

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRulesVocabulary from a JSON string
transaction_rules_vocabulary_instance = TransactionRulesVocabulary.from_json(json)
# print the JSON string representation of the object
print(TransactionRulesVocabulary.to_json())

# convert the object into a dict
transaction_rules_vocabulary_dict = transaction_rules_vocabulary_instance.to_dict()
# create an instance of TransactionRulesVocabulary from a dict
transaction_rules_vocabulary_from_dict = TransactionRulesVocabulary.from_dict(transaction_rules_vocabulary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


