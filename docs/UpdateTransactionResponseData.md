# UpdateTransactionResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**old_attributes** | **Dict[str, object]** | Pre-update field snapshot (free-form). sender_balance_after / receiver_balance_after are null for a leg whose account balance the requesting role may not see (BE-369); on such a note description is null too. | [optional] 
**commissions** | [**UpdateTransactionResponseDataCommissions**](UpdateTransactionResponseDataCommissions.md) |  | [optional] 
**recalculated** | [**TransactionRecalculatedNote**](TransactionRecalculatedNote.md) |  | [optional] 
**transactions** | **List[object]** | Enriched transactions list (present only when request includes account_id). Each item has the shape of EnrichedTransactionItem, including &#x60;schedule_status&#x60;. | [optional] 
**removed_ids** | **List[int]** | IDs removed from the account view (present only when request includes account_id) | [optional] 
**summary** | **Dict[str, object]** | Account summary recompute (present only when request includes account_id). It has the shape of AccountSummary, including &#x60;unconfirmed_amount&#x60;, or is an empty array when the account is not found. | [optional] 

## Example

```python
from orbuculum_client.models.update_transaction_response_data import UpdateTransactionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionResponseData from a JSON string
update_transaction_response_data_instance = UpdateTransactionResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionResponseData.to_json())

# convert the object into a dict
update_transaction_response_data_dict = update_transaction_response_data_instance.to_dict()
# create an instance of UpdateTransactionResponseData from a dict
update_transaction_response_data_from_dict = UpdateTransactionResponseData.from_dict(update_transaction_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


