# LedgerVerificationResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdict** | **str** | rejected if and only if at least one invariant has status fail | 
**invariants** | [**LedgerVerificationResponseDataInvariants**](LedgerVerificationResponseDataInvariants.md) |  | 
**limitations** | **List[str]** | What the selection mode used cannot see | 

## Example

```python
from orbuculum_client.models.ledger_verification_response_data import LedgerVerificationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerVerificationResponseData from a JSON string
ledger_verification_response_data_instance = LedgerVerificationResponseData.from_json(json)
# print the JSON string representation of the object
print(LedgerVerificationResponseData.to_json())

# convert the object into a dict
ledger_verification_response_data_dict = ledger_verification_response_data_instance.to_dict()
# create an instance of LedgerVerificationResponseData from a dict
ledger_verification_response_data_from_dict = LedgerVerificationResponseData.from_dict(ledger_verification_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


