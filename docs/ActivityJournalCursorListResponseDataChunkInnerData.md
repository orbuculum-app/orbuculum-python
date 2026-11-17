# ActivityJournalCursorListResponseDataChunkInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**dt** | **str** | OMM-2124: entry timestamp emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC …Z when absent/invalid). Cursor mode only. | 
**description** | **str** |  | [optional] 
**type_author** | **str** |  | [optional] 
**author_id** | **int** |  | [optional] 
**author_name** | **str** |  | [optional] 
**device** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**type_action** | **str** | Action type (create, update, delete, foreign_edit, etc.) | [optional] 
**amount_impact** | **str** |  | [optional] 
**type_model** | **str** |  | [optional] 
**model_id** | **int** |  | [optional] 
**channel** | **str** | Write channel: &#x60;ui&#x60; is a browser UI (legacy web or an SPA session), &#x60;mcp&#x60; the attested MCP server, &#x60;bot&#x60; the attested chatbot v2 server, &#x60;api&#x60; any other API client, &#x60;chatbot&#x60; the X-Source-Channel chatbot header, &#x60;import&#x60; rows an import created (seen as &#x60;foreign_edit.creator.channel&#x60;; the import&#39;s own event carries the channel of the request that ran it) | [optional] 
**client** | **str** | Client name the MCP server vouched for | [optional] 
**change_set_id** | **int** | Change set the write is recorded in (BE-337): the set named by X-Orbuculum-Change-Set, else the set the server resolved for the request. Set on write events of transactions, accounts, counterparties and labels (foreign_edit rows of updates and deletes included) and on model-less write summaries such as an import. Null for reads, logins and endpoint-access rows, for writes to other models (currencies, rates, users, roles and the like), when the set could not be resolved, and for rows journaled before BE-339. | [optional] 
**transaction_dt** | **str** | The transaction&#39;s stored date, verbatim, as Y-m-d H:i:s | [optional] 
**entity_id_1** | **int** | Sender entity ID | [optional] 
**account_id_1** | **int** | Sender account ID | [optional] 
**entity_id_2** | **int** | Receiver entity ID | [optional] 
**account_id_2** | **int** | Receiver account ID | [optional] 
**foreign_edit** | [**ActivityJournalForeignEdit**](ActivityJournalForeignEdit.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.activity_journal_cursor_list_response_data_chunk_inner_data import ActivityJournalCursorListResponseDataChunkInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalCursorListResponseDataChunkInnerData from a JSON string
activity_journal_cursor_list_response_data_chunk_inner_data_instance = ActivityJournalCursorListResponseDataChunkInnerData.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalCursorListResponseDataChunkInnerData.to_json())

# convert the object into a dict
activity_journal_cursor_list_response_data_chunk_inner_data_dict = activity_journal_cursor_list_response_data_chunk_inner_data_instance.to_dict()
# create an instance of ActivityJournalCursorListResponseDataChunkInnerData from a dict
activity_journal_cursor_list_response_data_chunk_inner_data_from_dict = ActivityJournalCursorListResponseDataChunkInnerData.from_dict(activity_journal_cursor_list_response_data_chunk_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


