# AccountTransactionsPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_date** | **str** | OMM-2124: offset-ISO in the working timezone (X-Timezone header; UTC …Z when absent/invalid). | [optional] 
**last_date** | **str** | OMM-2124: offset-ISO in the working timezone (X-Timezone header; UTC …Z when absent/invalid). | [optional] 
**total_count** | **int** |  | [optional] 
**next_cursor** | [**AccountTransactionsPaginationNextCursor**](AccountTransactionsPaginationNextCursor.md) |  | [optional] 
**has_more** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.account_transactions_pagination import AccountTransactionsPagination

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsPagination from a JSON string
account_transactions_pagination_instance = AccountTransactionsPagination.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsPagination.to_json())

# convert the object into a dict
account_transactions_pagination_dict = account_transactions_pagination_instance.to_dict()
# create an instance of AccountTransactionsPagination from a dict
account_transactions_pagination_from_dict = AccountTransactionsPagination.from_dict(account_transactions_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


