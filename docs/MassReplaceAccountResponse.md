# MassReplaceAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for POST /api/transaction/mass-replace-account (HTTP 200).  Container shape: - status: HTTP status (always 200 on success / partial success). - data: - affected_count: number of transactions actually updated (legacy, preserved). - processed_count: same as affected_count, surfaced uniformly for new clients. - skipped_count: number of input IDs that were NOT processed. - skipped_ids: int[] of input IDs that were skipped. - skipped_reasons: object map of stringified-id → reason constant. Reason values: \&quot;permission_denied\&quot; | \&quot;not_found\&quot; | \&quot;wrong_account\&quot;. | 
**data** | [**MassReplaceAccountResponseData**](MassReplaceAccountResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.mass_replace_account_response import MassReplaceAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MassReplaceAccountResponse from a JSON string
mass_replace_account_response_instance = MassReplaceAccountResponse.from_json(json)
# print the JSON string representation of the object
print(MassReplaceAccountResponse.to_json())

# convert the object into a dict
mass_replace_account_response_dict = mass_replace_account_response_instance.to_dict()
# create an instance of MassReplaceAccountResponse from a dict
mass_replace_account_response_from_dict = MassReplaceAccountResponse.from_dict(mass_replace_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


