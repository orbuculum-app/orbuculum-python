# BulkCreateTransactionsResponseDataItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_index** | **int** | 0-based index in the input transactions array. | 
**id** | **int** | Database id of the created transaction (real run, success only). | [optional] 
**preview** | **object** | Validation preview (dry_run mode, success only). Shape mirrors single-create response data. | [optional] 
**errors** | [**List[BulkCreateTransactionsResponseDataItemsInnerErrorsInner]**](BulkCreateTransactionsResponseDataItemsInnerErrorsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.bulk_create_transactions_response_data_items_inner import BulkCreateTransactionsResponseDataItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateTransactionsResponseDataItemsInner from a JSON string
bulk_create_transactions_response_data_items_inner_instance = BulkCreateTransactionsResponseDataItemsInner.from_json(json)
# print the JSON string representation of the object
print(BulkCreateTransactionsResponseDataItemsInner.to_json())

# convert the object into a dict
bulk_create_transactions_response_data_items_inner_dict = bulk_create_transactions_response_data_items_inner_instance.to_dict()
# create an instance of BulkCreateTransactionsResponseDataItemsInner from a dict
bulk_create_transactions_response_data_items_inner_from_dict = BulkCreateTransactionsResponseDataItemsInner.from_dict(bulk_create_transactions_response_data_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


