# TransactionDraftEditRequest

Transaction whose modal state is to be composed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Transaction being edited | 
**dt** | **str** | Date the modal is showing, &#39;Y-m-d H:i:s&#39; in UTC. Selects the per-currency rate rows behind &#x60;form.rate&#x60;. Defaults to the STORED TRANSACTION&#39;S OWN dt, not to now. | [optional] 

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


