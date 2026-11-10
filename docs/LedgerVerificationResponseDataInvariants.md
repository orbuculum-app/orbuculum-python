# LedgerVerificationResponseDataInvariants


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
from orbuculum_client.models.ledger_verification_response_data_invariants import LedgerVerificationResponseDataInvariants

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerVerificationResponseDataInvariants from a JSON string
ledger_verification_response_data_invariants_instance = LedgerVerificationResponseDataInvariants.from_json(json)
# print the JSON string representation of the object
print(LedgerVerificationResponseDataInvariants.to_json())

# convert the object into a dict
ledger_verification_response_data_invariants_dict = ledger_verification_response_data_invariants_instance.to_dict()
# create an instance of LedgerVerificationResponseDataInvariants from a dict
ledger_verification_response_data_invariants_from_dict = LedgerVerificationResponseDataInvariants.from_dict(ledger_verification_response_data_invariants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


