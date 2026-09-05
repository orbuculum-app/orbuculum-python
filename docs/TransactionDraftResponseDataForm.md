# TransactionDraftResponseDataForm

The modal's form state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[Project]**](Project.md) | Labels (\&quot;projects\&quot;) the caller may manage in this workspace | 
**label_id** | **int** | The resolved label every verdict in this response was computed under | [optional] 
**sender** | [**TransactionDraftSide**](TransactionDraftSide.md) |  | [optional] 
**receiver** | [**TransactionDraftSide**](TransactionDraftSide.md) |  | [optional] 
**double** | [**TransactionDraftSide**](TransactionDraftSide.md) |  | [optional] 
**rate** | **str** | Sender -&gt; receiver rate in force at the effective &#x60;dt&#x60;, as a bcmath scale-18 decimal STRING (never a JSON number). Null when either side is unset, a currency has no rate rows, or the sender rate is zero. | [optional] 
**pair_valid** | **bool** | Whether the currently chosen accounts form a pair (and triple) the write path accepts. True while fewer than two sides are set. | 
**accounts_count** | **int** | Accounts available to the caller in this workspace | 

## Example

```python
from orbuculum_client.models.transaction_draft_response_data_form import TransactionDraftResponseDataForm

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftResponseDataForm from a JSON string
transaction_draft_response_data_form_instance = TransactionDraftResponseDataForm.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftResponseDataForm.to_json())

# convert the object into a dict
transaction_draft_response_data_form_dict = transaction_draft_response_data_form_instance.to_dict()
# create an instance of TransactionDraftResponseDataForm from a dict
transaction_draft_response_data_form_from_dict = TransactionDraftResponseDataForm.from_dict(transaction_draft_response_data_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


