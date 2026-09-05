# EnrichedTransactionItem

Perspective-aware transaction row used in the `transactions[]` enrichment of mutation responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction ID. | 
**dt** | **datetime** | Transaction date and time. Format: YYYY-MM-DD HH:MM:SS. When &#x60;time_unset&#x60; is true this is the stable canonical &#39;YYYY-MM-DD 00:00:00&#39; regardless of X-Timezone. | 
**time_unset** | **bool** | True when the transaction was saved with a date but no time; &#x60;dt&#x60; is then the stable canonical &#39;YYYY-MM-DD 00:00:00&#39;. | 
**sender_account_id** | **int** | Sender account ID. | 
**receiver_account_id** | **int** | Receiver account ID. | 
**sender_amount** | **str** | Sender amount. Decimal value as number_format-style string. | 
**receiver_amount** | **str** | Receiver amount. Decimal value as number_format-style string. | 
**comment** | **str** | Transaction comment. | [optional] 
**label_id** | **int** | Label ID (legacy alias: API &#x60;project_id&#x60; &#x3D; DB &#x60;label_id&#x60;). | [optional] 
**done** | **bool** | Whether the transaction is marked done. | 
**is_future** | **bool** | True when the transaction is dated in the future relative to the seam (dt &gt; NOW() + 59s, evaluated UTC; STRICT — dt &#x3D;&#x3D; seam is false). Temporal flag only; recurrence is signalled separately by is_recurrent. | 
**is_recurrent** | **bool** | True when the transaction is part of a recurring schedule (future_id set). Drives the FE recurrence icon. | 
**balance_after** | **str** | Balance on the perspective account after this transaction. Decimal value as number_format-style string. | [optional] 
**counterparty** | [**EnrichedTransactionItemCounterparty**](EnrichedTransactionItemCounterparty.md) |  | 
**chained_id** | **int** | ID of the paired transaction in a debt-pair, when applicable. | [optional] 
**chained_commission_id** | **int** | ID of the sender-side commission transaction generated alongside this one. | [optional] 
**editable** | **bool** | Whether the consumer can edit this transaction. Always true in the create path. | 

## Example

```python
from orbuculum_client.models.enriched_transaction_item import EnrichedTransactionItem

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedTransactionItem from a JSON string
enriched_transaction_item_instance = EnrichedTransactionItem.from_json(json)
# print the JSON string representation of the object
print(EnrichedTransactionItem.to_json())

# convert the object into a dict
enriched_transaction_item_dict = enriched_transaction_item_instance.to_dict()
# create an instance of EnrichedTransactionItem from a dict
enriched_transaction_item_from_dict = EnrichedTransactionItem.from_dict(enriched_transaction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


