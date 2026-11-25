# MatchingSuggestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**sender_account_id** | **int** |  | [optional] 
**receiver_account_id** | **int** |  | [optional] 
**amount** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**limit** | **int** |  | [optional] [default to 5]
**counterparty_hash** | **str** |  | [optional] 
**import_id** | **int** |  | [optional] 
**label_id** | **int** |  | [optional] 
**as_of** | **datetime** | Optional, for evaluation replays of past phrases: the precedent strategy uses only transactions created at or before this instant. It compares the transaction&#39;s creation time, not its date (dt); precedent ranking is unchanged. Older transactions with no recorded creation time count as earlier; exclude those with exclude_transaction_ids. The account-pair strategy counts its usage counters (\&quot;Used N times, last N days ago\&quot;) only over transactions dated (dt) strictly before this instant, and measures \&quot;last N days ago\&quot; from it; the pair list itself and the score of pairs with no counted use are not cut off. Other strategies are not affected. Accepts the API&#39;s date-time formats: YYYY-MM-DD HH:MM:SS or YYYY-MM-DDTHH:MM:SS, optionally ending in Z or ±HH:MM, or a date alone (YYYY-MM-DD, read as 00:00:00). A value with Z or an offset is converted to UTC; a value without one is read as UTC. An invalid value answers 422. Omitted or empty: no cutoff. | [optional] 
**exclude_transaction_ids** | **List[int]** | Optional, for evaluation replays of past phrases: ids of transactions the precedent strategy must not use as precedents and the account-pair strategy must not count in its usage counters, for example the transaction the replayed phrase produced. Other strategies are not affected. Each id must be a positive integer, otherwise 422. Omitted or empty: nothing is excluded. | [optional] 

## Example

```python
from orbuculum_client.models.matching_suggest_request import MatchingSuggestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingSuggestRequest from a JSON string
matching_suggest_request_instance = MatchingSuggestRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingSuggestRequest.to_json())

# convert the object into a dict
matching_suggest_request_dict = matching_suggest_request_instance.to_dict()
# create an instance of MatchingSuggestRequest from a dict
matching_suggest_request_from_dict = MatchingSuggestRequest.from_dict(matching_suggest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


