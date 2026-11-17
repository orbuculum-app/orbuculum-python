# LedgerVerificationInvariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i2a** | [**LedgerInvariantResult**](LedgerInvariantResult.md) |  | 
**i2b** | [**LedgerInvariantResult**](LedgerInvariantResult.md) |  | 
**i4** | [**LedgerInvariantResult**](LedgerInvariantResult.md) |  | 
**i5** | [**LedgerInvariantResult**](LedgerInvariantResult.md) |  | 
**i8** | [**LedgerInvariantResult**](LedgerInvariantResult.md) |  | 
**i10** | [**LedgerInvariantResult**](LedgerInvariantResult.md) |  | 

## Example

```python
from orbuculum_client.models.ledger_verification_invariants import LedgerVerificationInvariants

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerVerificationInvariants from a JSON string
ledger_verification_invariants_instance = LedgerVerificationInvariants.from_json(json)
# print the JSON string representation of the object
print(LedgerVerificationInvariants.to_json())

# convert the object into a dict
ledger_verification_invariants_dict = ledger_verification_invariants_instance.to_dict()
# create an instance of LedgerVerificationInvariants from a dict
ledger_verification_invariants_from_dict = LedgerVerificationInvariants.from_dict(ledger_verification_invariants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


