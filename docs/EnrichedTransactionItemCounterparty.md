# EnrichedTransactionItemCounterparty

Description of the OTHER side of the transaction (relative to the perspective account).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Counterparty account ID. | 
**account_name** | **str** | Counterparty account name. | [optional] 
**entity_name** | **str** | Counterparty entity (counterparty owner) name. | [optional] 
**currency_code** | **str** | Counterparty account currency code (e.g. &#39;USD&#39;). | [optional] 

## Example

```python
from orbuculum_client.models.enriched_transaction_item_counterparty import EnrichedTransactionItemCounterparty

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedTransactionItemCounterparty from a JSON string
enriched_transaction_item_counterparty_instance = EnrichedTransactionItemCounterparty.from_json(json)
# print the JSON string representation of the object
print(EnrichedTransactionItemCounterparty.to_json())

# convert the object into a dict
enriched_transaction_item_counterparty_dict = enriched_transaction_item_counterparty_instance.to_dict()
# create an instance of EnrichedTransactionItemCounterparty from a dict
enriched_transaction_item_counterparty_from_dict = EnrichedTransactionItemCounterparty.from_dict(enriched_transaction_item_counterparty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


