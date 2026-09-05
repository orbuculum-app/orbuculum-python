# SelectableAccountsResponseData

Selectable-account sets for the requested slot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtab** | **str** | Echo of the requested sub-tab | 
**slot** | **str** | Echo of the requested slot | 
**slot_class** | **str** | Resolved eligibility class | 
**account_ids** | **List[int]** | Accounts matching the slot and not hidden, in natural name order | 
**hidden_account_ids** | **List[int]** | Accounts matching the slot but hidden; an edit-mode client un-hides the participants of the edited transaction from this set | 

## Example

```python
from orbuculum_client.models.selectable_accounts_response_data import SelectableAccountsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SelectableAccountsResponseData from a JSON string
selectable_accounts_response_data_instance = SelectableAccountsResponseData.from_json(json)
# print the JSON string representation of the object
print(SelectableAccountsResponseData.to_json())

# convert the object into a dict
selectable_accounts_response_data_dict = selectable_accounts_response_data_instance.to_dict()
# create an instance of SelectableAccountsResponseData from a dict
selectable_accounts_response_data_from_dict = SelectableAccountsResponseData.from_dict(selectable_accounts_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


