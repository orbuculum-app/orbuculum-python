# LedgerInvariantResultOffendersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction id for I2a, I2b, I4, I5 and I8; the journal entry&#39;s model_id for I10 (null when the entry has none) | 
**model** | **str** |  | 
**reason** | **str** | One-line reason | 

## Example

```python
from orbuculum_client.models.ledger_invariant_result_offenders_inner import LedgerInvariantResultOffendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerInvariantResultOffendersInner from a JSON string
ledger_invariant_result_offenders_inner_instance = LedgerInvariantResultOffendersInner.from_json(json)
# print the JSON string representation of the object
print(LedgerInvariantResultOffendersInner.to_json())

# convert the object into a dict
ledger_invariant_result_offenders_inner_dict = ledger_invariant_result_offenders_inner_instance.to_dict()
# create an instance of LedgerInvariantResultOffendersInner from a dict
ledger_invariant_result_offenders_inner_from_dict = LedgerInvariantResultOffendersInner.from_dict(ledger_invariant_result_offenders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


