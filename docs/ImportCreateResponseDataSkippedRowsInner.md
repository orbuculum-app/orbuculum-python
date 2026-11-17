# ImportCreateResponseDataSkippedRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_index** | **int** |  | 
**reason** | **str** | permission_denied — the role may not create this row; invalid_label — the row&#39;s label does not exist in the workspace; empty_counterparty — the row has no counterparty account (unmatched in preview and not set via update-table); already_existed: a transaction with this row&#39;s idempotency key already exists on the account (BE-340); nothing was created for the row; duplicate_candidate: the row has no source id and matches an existing transaction you can view, or an earlier row of this import (see duplicate_candidate). Nothing was created for it, and it stays staged under the same import_key, even when other rows were inserted: repeat POST /api/import/create with that import_key and allow_duplicate: true to write it, or POST /api/import/cancel to discard it (BE-403). | 
**duplicate_candidate** | [**DuplicateCandidate**](DuplicateCandidate.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.import_create_response_data_skipped_rows_inner import ImportCreateResponseDataSkippedRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCreateResponseDataSkippedRowsInner from a JSON string
import_create_response_data_skipped_rows_inner_instance = ImportCreateResponseDataSkippedRowsInner.from_json(json)
# print the JSON string representation of the object
print(ImportCreateResponseDataSkippedRowsInner.to_json())

# convert the object into a dict
import_create_response_data_skipped_rows_inner_dict = import_create_response_data_skipped_rows_inner_instance.to_dict()
# create an instance of ImportCreateResponseDataSkippedRowsInner from a dict
import_create_response_data_skipped_rows_inner_from_dict = ImportCreateResponseDataSkippedRowsInner.from_dict(import_create_response_data_skipped_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


