# UpdateTransactionResponse

Successful response from POST /api/transaction/update with optional commission and enrichment data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for POST /api/transaction/update (200 OK).  Documents the success-data shape: - &#x60;id&#x60;             — updated transaction ID - &#x60;old_attributes&#x60; — pre-update field snapshot (free-form object, used by frontend for diffs) - &#x60;commissions&#x60;    — per-slot commission result (sender/receiver), nullable when no commission for that slot - &#x60;transactions&#x60;, &#x60;removed_ids&#x60;, &#x60;summary&#x60; — additive when caller passed &#x60;account_id&#x60; for enriched response  The &#x60;commissions.sender&#x60; / &#x60;commissions.receiver&#x60; properties reference &#x60;UpdateCommissionResult&#x60; and are nullable: &#x60;null&#x60; means the slot has no commission after the update (never existed, just deleted, or no data was provided and FK was already null). | 
**data** | [**UpdateTransactionResponseData**](UpdateTransactionResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.update_transaction_response import UpdateTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionResponse from a JSON string
update_transaction_response_instance = UpdateTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionResponse.to_json())

# convert the object into a dict
update_transaction_response_dict = update_transaction_response_instance.to_dict()
# create an instance of UpdateTransactionResponse from a dict
update_transaction_response_from_dict = UpdateTransactionResponse.from_dict(update_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


