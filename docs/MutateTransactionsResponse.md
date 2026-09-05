# MutateTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for POST /api/transaction/mutate (HTTP 200) — OMM-2136.  The unified mutation endpoint returns a structured diff the FE2.0 client applies to its local state without re-fetching: - status: HTTP status (always 200 on success). - data: - drops: int[] of transaction ids the FE should remove from the loaded window (deleted rows, or rows that left the loaded slice). - upserts: canonical transaction rows (camelCase wire shape) to insert/replace, each carrying the mutation-time &#x60;isOut&#x60; flag. - balanceUpdates: in-place cascade balance patches for rows whose identity did not change but whose running balance shifted. - summary (BE-42): filter-scoped AccountSummary (currency/precision/show_balance/ recent/latest) over the SAME visible scope + past/future boundary as the row diff — parity with GET /api/transaction/list. Null in account-less bulk mode.  balanceUpdates is present for account-scoped responses (accountId&gt;0) and OMITTED for account-less id-based bulk delete/duplicate (BE-13). summary is null there. | 
**data** | [**MutateTransactionsResponseData**](MutateTransactionsResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.mutate_transactions_response import MutateTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MutateTransactionsResponse from a JSON string
mutate_transactions_response_instance = MutateTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(MutateTransactionsResponse.to_json())

# convert the object into a dict
mutate_transactions_response_dict = mutate_transactions_response_instance.to_dict()
# create an instance of MutateTransactionsResponse from a dict
mutate_transactions_response_from_dict = MutateTransactionsResponse.from_dict(mutate_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


