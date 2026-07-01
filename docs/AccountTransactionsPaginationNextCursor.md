# AccountTransactionsPaginationNextCursor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **str** | OMM-2124: offset-ISO in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Pass back verbatim as the cursor_dt query param. | 
**id** | **int** |  | 

## Example

```python
from orbuculum_client.models.account_transactions_pagination_next_cursor import AccountTransactionsPaginationNextCursor

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsPaginationNextCursor from a JSON string
account_transactions_pagination_next_cursor_instance = AccountTransactionsPaginationNextCursor.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsPaginationNextCursor.to_json())

# convert the object into a dict
account_transactions_pagination_next_cursor_dict = account_transactions_pagination_next_cursor_instance.to_dict()
# create an instance of AccountTransactionsPaginationNextCursor from a dict
account_transactions_pagination_next_cursor_from_dict = AccountTransactionsPaginationNextCursor.from_dict(account_transactions_pagination_next_cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


