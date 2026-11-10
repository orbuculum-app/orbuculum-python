# LedgerVerificationResponse

Response of GET /api/transaction/verify (BE-311).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response of GET /api/transaction/verify (HTTP 200).  BE-311: the read-only ledger verifier&#39;s verdict, one result per invariant, and the limits of the selection mode used. | 
**data** | [**LedgerVerificationResponseData**](LedgerVerificationResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.ledger_verification_response import LedgerVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerVerificationResponse from a JSON string
ledger_verification_response_instance = LedgerVerificationResponse.from_json(json)
# print the JSON string representation of the object
print(LedgerVerificationResponse.to_json())

# convert the object into a dict
ledger_verification_response_dict = ledger_verification_response_instance.to_dict()
# create an instance of LedgerVerificationResponse from a dict
ledger_verification_response_from_dict = LedgerVerificationResponse.from_dict(ledger_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


