# TransactionDraftEditRequest

Transaction whose modal state is to be composed, and the Edit draft's current inputs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Transaction being edited | 
**dt** | **str** | Date the modal is showing, &#39;Y-m-d H:i:s&#39; in UTC. Selects the per-currency rate rows behind &#x60;form.rate&#x60;. Defaults to the STORED TRANSACTION&#39;S OWN dt, not to now. | [optional] 
**label_id** | **int** | Label (\&quot;project\&quot;) the draft is composed for. Absent or null &#x3D; the stored transaction&#39;s label. A value that differs from it must be manageable in this workspace (else 422). | [optional] 
**sender_id** | **int** | Account in the sender slot. Absent or null &#x3D; the stored sender. A value that differs from it must be accessible in this workspace (else 422). | [optional] 
**receiver_id** | **int** | Account in the receiver slot. Absent or null &#x3D; the stored receiver. A value that differs from it must be accessible in this workspace (else 422). | [optional] 
**double_id** | **int** | Account in the intermediary (double) slot. Absent or null &#x3D; the stored intermediary. A value that differs from it must be accessible in this workspace (else 422). The single/double shape stays the stored one: on a stored single transaction it is checked, then ignored (form.double stays null). | [optional] 

## Example

```python
from orbuculum_client.models.transaction_draft_edit_request import TransactionDraftEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftEditRequest from a JSON string
transaction_draft_edit_request_instance = TransactionDraftEditRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftEditRequest.to_json())

# convert the object into a dict
transaction_draft_edit_request_dict = transaction_draft_edit_request_instance.to_dict()
# create an instance of TransactionDraftEditRequest from a dict
transaction_draft_edit_request_from_dict = TransactionDraftEditRequest.from_dict(transaction_draft_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


