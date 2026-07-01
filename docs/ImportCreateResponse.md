# ImportCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for POST /api/import/create (HTTP 200).  OMM-2057: per-row 3-way PLP check. Rows where the caller&#39;s role does not have &#x60;can_manage&#x3D;true&#x60; on (sender, receiver, label) are skipped. Permitted rows are inserted; denied rows are returned in &#x60;skipped_rows&#x60;. The endpoint returns 200 even when every row is denied — &#x60;inserted_count&#x3D;0&#x60;, &#x60;skipped_count&#x3D;N&#x60;, &#x60;transaction_ids&#x3D;[]&#x60;. (No 403 for \&quot;nothing imported\&quot; — silent-skip per spec.)  Backward-compat: &#x60;imported_count&#x60; is preserved as a legacy alias of &#x60;inserted_count&#x60;, and &#x60;date_from&#x60;/&#x60;date_to&#x60; continue to be emitted for the imported set.  Container shape: - status: HTTP status (always 200 on success / partial success). - data: - inserted_count: int — number of staging rows actually inserted into &#x60;transaction&#x60;. - imported_count: int — legacy alias of inserted_count, preserved for older clients. - skipped_count: int — number of staging rows denied by per-row 3-way PLP check. - transaction_ids: int[] — IDs of newly-inserted transactions (parallel to inserted set). - skipped_rows: array of &#x60;{row_index: int, reason: string}&#x60; — denied row index + reason. Reason values: \&quot;permission_denied\&quot;. - date_from: string|null — earliest dt of inserted rows, formatted in user timezone. - date_to: string|null — latest dt of inserted rows, formatted in user timezone. | 
**data** | [**ImportCreateResponseData**](ImportCreateResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.import_create_response import ImportCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCreateResponse from a JSON string
import_create_response_instance = ImportCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ImportCreateResponse.to_json())

# convert the object into a dict
import_create_response_dict = import_create_response_instance.to_dict()
# create an instance of ImportCreateResponse from a dict
import_create_response_from_dict = ImportCreateResponse.from_dict(import_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


