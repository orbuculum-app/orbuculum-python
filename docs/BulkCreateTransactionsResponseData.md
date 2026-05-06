# BulkCreateTransactionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_count** | **int** | Number of transactions actually created (always 0 in dry_run mode). | 
**failed_count** | **int** | Number of items that failed validation/business rules. | 
**items** | [**List[BulkCreateTransactionsResponseDataItemsInner]**](BulkCreateTransactionsResponseDataItemsInner.md) |  | 

## Example

```python
from orbuculum_client.models.bulk_create_transactions_response_data import BulkCreateTransactionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateTransactionsResponseData from a JSON string
bulk_create_transactions_response_data_instance = BulkCreateTransactionsResponseData.from_json(json)
# print the JSON string representation of the object
print(BulkCreateTransactionsResponseData.to_json())

# convert the object into a dict
bulk_create_transactions_response_data_dict = bulk_create_transactions_response_data_instance.to_dict()
# create an instance of BulkCreateTransactionsResponseData from a dict
bulk_create_transactions_response_data_from_dict = BulkCreateTransactionsResponseData.from_dict(bulk_create_transactions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


