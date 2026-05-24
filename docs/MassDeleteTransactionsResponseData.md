# MassDeleteTransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_count** | **int** |  | 
**deleted_ids** | **List[int]** |  | 
**processed_count** | **int** |  | 
**skipped_count** | **int** |  | 
**skipped_ids** | **List[int]** |  | 
**skipped_reasons** | **Dict[str, str]** | Map of skipped ID (as string) → reason constant | 

## Example

```python
from orbuculum_client.models.mass_delete_transactions_response_data import MassDeleteTransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MassDeleteTransactionsResponseData from a JSON string
mass_delete_transactions_response_data_instance = MassDeleteTransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(MassDeleteTransactionsResponseData.to_json())

# convert the object into a dict
mass_delete_transactions_response_data_dict = mass_delete_transactions_response_data_instance.to_dict()
# create an instance of MassDeleteTransactionsResponseData from a dict
mass_delete_transactions_response_data_from_dict = MassDeleteTransactionsResponseData.from_dict(mass_delete_transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


