# TransactionDraftSideCommission

Commission configuration of the chosen account; null when no account is chosen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission_account_id** | **int** |  | [optional] 
**custom_commission_sender_id** | **int** |  | [optional] 
**commission_appliance** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.transaction_draft_side_commission import TransactionDraftSideCommission

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDraftSideCommission from a JSON string
transaction_draft_side_commission_instance = TransactionDraftSideCommission.from_json(json)
# print the JSON string representation of the object
print(TransactionDraftSideCommission.to_json())

# convert the object into a dict
transaction_draft_side_commission_dict = transaction_draft_side_commission_instance.to_dict()
# create an instance of TransactionDraftSideCommission from a dict
transaction_draft_side_commission_from_dict = TransactionDraftSideCommission.from_dict(transaction_draft_side_commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


