# ActivityJournalListResponseDataItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Activity entry ID | 
**dt** | **str** | Timestamp of the activity | 
**description** | **str** | Human-readable action description | [optional] 
**type_author** | **str** | Author type (user, api, mcp, chatbot) | 
**author_id** | **int** | Author user ID | [optional] 
**author_name** | **str** | Author display name (email) | [optional] 
**device** | **str** | User agent / device info | [optional] 
**ip** | **str** | IP address | [optional] 
**type_action** | **str** | Action type (create, update, delete, foreign_edit, etc.) | [optional] 
**amount_impact** | **str** | Financial impact amount | 
**type_model** | **str** | PHP model class name | [optional] 
**model_id** | **int** | Related model ID | [optional] 
**channel** | **str** | Write channel: &#x60;ui&#x60; is a browser UI (legacy web or an SPA session) | [optional] 
**client** | **str** | Client name the MCP server vouched for | [optional] 
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


