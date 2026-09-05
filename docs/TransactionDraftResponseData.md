# TransactionDraftResponseData

Modal state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form** | [**TransactionDraftResponseDataForm**](TransactionDraftResponseDataForm.md) |  | 
**tab** | **str** | Tab the modal opens on, derived from &#x60;subtab&#x60;. Null in edit mode. | [optional] 
**subtab** | **str** | Sub-tab the modal opens on. Null in edit mode. | [optional] 
**visible_subtabs** | **List[str]** | Sub-tabs with at least one valid pair (or triple) under the resolved label, in the modal&#39;s DOM order. Null in edit mode. | [optional] 
**suggested** | [**TransactionDraftResponseDataSuggested**](TransactionDraftResponseDataSuggested.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.transaction_draft_response_data import TransactionDraftResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftResponseData from a JSON string
transaction_draft_response_data_instance = TransactionDraftResponseData.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftResponseData.to_json())

# convert the object into a dict
transaction_draft_response_data_dict = transaction_draft_response_data_instance.to_dict()
# create an instance of TransactionDraftResponseData from a dict
transaction_draft_response_data_from_dict = TransactionDraftResponseData.from_dict(transaction_draft_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


