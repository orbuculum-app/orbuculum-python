# ImportCreateResponseDataSkippedRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_index** | **int** |  | 
**reason** | **str** | permission_denied — the role may not create this row; invalid_label — the row&#39;s label does not exist in the workspace; empty_counterparty — the row has no counterparty account (unmatched in preview and not set via update-table) | 

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


