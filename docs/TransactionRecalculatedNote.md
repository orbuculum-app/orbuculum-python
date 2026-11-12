# TransactionRecalculatedNote

Names the amount the server recalculated on a single-amount update. Absent when no amount moved: both amounts or neither sent, keep_amount, refuse, an unchanged result, or a same-currency copy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The amount the server recalculated on a single-amount update (BE-300).  Shared by POST /api/transaction/update (&#x60;data.recalculated&#x60;) and POST /api/transaction/mutate action update (&#x60;data.recalculated&#x60;). | 
**old** | **str** | Stored value before the edit, decimal string. | 
**new** | **str** | Stored value after the edit, decimal string, unrounded. | 
**basis** | **str** | date_rate: the transaction date&#39;s exchange rate. fixed_rate: the stored ratio of the two amounts. | 

## Example

```python
from orbuculum_client.models.transaction_recalculated_note import TransactionRecalculatedNote

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRecalculatedNote from a JSON string
transaction_recalculated_note_instance = TransactionRecalculatedNote.from_json(json)
# print the JSON string representation of the object
print(TransactionRecalculatedNote.to_json())

# convert the object into a dict
transaction_recalculated_note_dict = transaction_recalculated_note_instance.to_dict()
# create an instance of TransactionRecalculatedNote from a dict
transaction_recalculated_note_from_dict = TransactionRecalculatedNote.from_dict(transaction_recalculated_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


