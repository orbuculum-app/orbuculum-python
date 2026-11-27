# AccountSummaryHalf

Sent / received / balance triplet for one period (recent or latest) of an AccountSummary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **str** | Total sent in the period. Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). | 
**received** | **str** | Total received in the period. Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). | 
**balance** | **str** | Account balance at end of the period. Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). Null when the requesting role may not see this account&#39;s balance (BE-369). | 

## Example

```python
from orbuculum_client.models.account_summary_half import AccountSummaryHalf

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSummaryHalf from a JSON string
account_summary_half_instance = AccountSummaryHalf.from_json(json)
# print the JSON string representation of the object
print(AccountSummaryHalf.to_json())

# convert the object into a dict
account_summary_half_dict = account_summary_half_instance.to_dict()
# create an instance of AccountSummaryHalf from a dict
account_summary_half_from_dict = AccountSummaryHalf.from_dict(account_summary_half_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


