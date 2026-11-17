# LedgerVerification

The ledger verifier's verdict (BE-311): one result per invariant and the limits of the selection mode. Returned by GET /api/transaction/verify and by the change-set gate (BE-341).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdict** | **str** | rejected if and only if at least one invariant has status fail | 
**invariants** | [**LedgerVerificationInvariants**](LedgerVerificationInvariants.md) |  | 
**limitations** | **List[str]** | What the selection mode used cannot see | 

## Example

```python
from orbuculum_client.models.ledger_verification import LedgerVerification

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerVerification from a JSON string
ledger_verification_instance = LedgerVerification.from_json(json)
# print the JSON string representation of the object
print(LedgerVerification.to_json())

# convert the object into a dict
ledger_verification_dict = ledger_verification_instance.to_dict()
# create an instance of LedgerVerification from a dict
ledger_verification_from_dict = LedgerVerification.from_dict(ledger_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


