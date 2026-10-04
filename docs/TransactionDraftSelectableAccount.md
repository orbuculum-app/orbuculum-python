# TransactionDraftSelectableAccount

An account the slot offers. Limitation-locked accounts are excluded from the list; label_restricted still only dims

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account ID | 
**entity_id** | **int** | Owning entity, so the client can group into category strips without a second call | 
**hidden** | **bool** | The account is hidden; the modal removes these outside edit mode | 
**drops_counterparty** | **bool** | True only for a stored leg of the transaction being edited whose stored pair violates a current limitation — those legs are the one kind of entry the pairwise limitation rule keeps instead of removing, so the client may badge them. False for every other entry, and always false on POST /api/transaction-draft. | 
**label_restricted** | **bool** | The account is not manageable under the resolved label echoed in form.label_id. Dimmed, not hidden. | 
**recent** | **bool** | True only when the account is in this slot&#39;s counterparty pair map: accounts already paired with the account chosen opposite (for the double slot, with the sender). These are exactly the entries sorted first, so they always form a prefix of selectable[]. A non-zero send/receive timestamp alone does not make an entry recent. With no counterparty chosen, or one with no pair history, every entry is false. The picker&#39;s \&quot;Recently used\&quot; strip shows the first 3 visible entries carrying it. Same rule on POST /api/transaction-draft and /api/transaction-draft/edit. | 

## Example

```python
from orbuculum_client.models.transaction_draft_selectable_account import TransactionDraftSelectableAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftSelectableAccount from a JSON string
transaction_draft_selectable_account_instance = TransactionDraftSelectableAccount.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftSelectableAccount.to_json())

# convert the object into a dict
transaction_draft_selectable_account_dict = transaction_draft_selectable_account_instance.to_dict()
# create an instance of TransactionDraftSelectableAccount from a dict
transaction_draft_selectable_account_from_dict = TransactionDraftSelectableAccount.from_dict(transaction_draft_selectable_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


