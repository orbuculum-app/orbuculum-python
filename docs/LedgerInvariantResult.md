# LedgerInvariantResult

Result of one ledger invariant (BE-311): its status and, when it fails, the offending records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | One invariant&#39;s result inside GET /api/transaction/verify (BE-311). | 
**offenders** | [**List[LedgerInvariantResultOffendersInner]**](LedgerInvariantResultOffendersInner.md) | Empty unless status is fail; a fail always has at least one offender | 

## Example

```python
from orbuculum_client.models.ledger_invariant_result import LedgerInvariantResult

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerInvariantResult from a JSON string
ledger_invariant_result_instance = LedgerInvariantResult.from_json(json)
# print the JSON string representation of the object
print(LedgerInvariantResult.to_json())

# convert the object into a dict
ledger_invariant_result_dict = ledger_invariant_result_instance.to_dict()
# create an instance of LedgerInvariantResult from a dict
ledger_invariant_result_from_dict = LedgerInvariantResult.from_dict(ledger_invariant_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


