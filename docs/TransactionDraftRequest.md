# TransactionDraftRequest

Filter inputs for the transaction-modal draft facade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**subtab** | **str** | Sub-tab to compose the draft for. Omit or send null to let the server derive it from the modal defaults. | [optional] 
**label_id** | **int** | Label (\&quot;project\&quot;) override; must be manageable in this workspace | [optional] 
**sender_id** | **int** | Account already chosen in the sender slot | [optional] 
**receiver_id** | **int** | Account already chosen in the receiver slot | [optional] 
**double_id** | **int** | Account already chosen in the intermediary (double) slot | [optional] 
**context_account_id** | **int** | Account the modal was opened from; drives the derived tab/sub-tab and the suggestion | [optional] 
**exclude_trx_id** | **int** | A transaction that may not become its own anchor when the sub-tab is derived | [optional] 
**dt** | **str** | Date the modal is showing, &#39;Y-m-d H:i:s&#39; in UTC. Selects the per-currency rate rows behind &#x60;form.rate&#x60;. Defaults to now. | [optional] 

## Example

```python
from orbuculum_client.models.transaction_draft_request import TransactionDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftRequest from a JSON string
transaction_draft_request_instance = TransactionDraftRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftRequest.to_json())

# convert the object into a dict
transaction_draft_request_dict = transaction_draft_request_instance.to_dict()
# create an instance of TransactionDraftRequest from a dict
transaction_draft_request_from_dict = TransactionDraftRequest.from_dict(transaction_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


