# ActivityJournalListResponseDataItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Activity entry ID | 
**dt** | **str** | Timestamp of the activity | 
**description** | **str** | Human-readable action description | [optional] 
**type_author** | **str** | Author type (user, api, mcp, chatbot, bot): the class of the request that wrote the event. &#x60;import&#x60; is a row channel only (seen as foreign_edit.creator.channel) and is never an event&#39;s author type: an import&#39;s event carries the type of the request that ran it. | 
**author_id** | **int** | Author user ID | [optional] 
**author_name** | **str** | Author display name (email) | [optional] 
**device** | **str** | User agent / device info | [optional] 
**ip** | **str** | IP address | [optional] 
**type_action** | **str** | Action type (create, update, delete, foreign_edit, etc.) | [optional] 
**amount_impact** | **str** | Financial impact amount | 
**type_model** | **str** | PHP model class name | [optional] 
**model_id** | **int** | Related model ID | [optional] 
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
from orbuculum_client.models.activity_journal_list_response_data_items_inner import ActivityJournalListResponseDataItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityJournalListResponseDataItemsInner from a JSON string
activity_journal_list_response_data_items_inner_instance = ActivityJournalListResponseDataItemsInner.from_json(json)
# print the JSON string representation of the object
print(ActivityJournalListResponseDataItemsInner.to_json())

# convert the object into a dict
activity_journal_list_response_data_items_inner_dict = activity_journal_list_response_data_items_inner_instance.to_dict()
# create an instance of ActivityJournalListResponseDataItemsInner from a dict
activity_journal_list_response_data_items_inner_from_dict = ActivityJournalListResponseDataItemsInner.from_dict(activity_journal_list_response_data_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


