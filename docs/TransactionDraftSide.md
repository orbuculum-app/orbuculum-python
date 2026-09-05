# TransactionDraftSide

One slot of the transaction modal (sender, receiver or double)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **int** | Account chosen in this slot, or null when the slot is open | [optional] 
**commission** | [**TransactionDraftSideCommission**](TransactionDraftSideCommission.md) |  | [optional] 
**selectable** | [**List[TransactionDraftSelectableAccount]**](TransactionDraftSelectableAccount.md) | Accounts this slot may offer, already ordered: counterparty promotion first, then send_ts/receive_ts DESC, then account_id ASC | 

## Example

```python
from orbuculum_client.models.transaction_draft_side import TransactionDraftSide

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftSide from a JSON string
transaction_draft_side_instance = TransactionDraftSide.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftSide.to_json())

# convert the object into a dict
transaction_draft_side_dict = transaction_draft_side_instance.to_dict()
# create an instance of TransactionDraftSide from a dict
transaction_draft_side_from_dict = TransactionDraftSide.from_dict(transaction_draft_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


