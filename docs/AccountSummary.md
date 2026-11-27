# AccountSummary

Per-account summary (currency, precision, recent/latest sent/received/balance) returned with enriched transaction responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Stored currency name (may be a sign such as &#39;$&#39;); the ISO code is in currency_code. Null when the account currency is unset. | [optional] 
**currency_code** | **str** | ISO code of the account currency | [optional] 
**precision** | **int** | Decimal precision used for sent/received/balance string formatting. Defaults to 2. | 
**show_balance** | **bool** | Whether the requesting role may see this account&#39;s balance (BE-369). When false, recent.balance and latest.balance are null; sent and received are always present. | 
**recent** | [**AccountSummaryHalf**](AccountSummaryHalf.md) |  | 
**latest** | [**AccountSummaryHalf**](AccountSummaryHalf.md) |  | [optional] 
**unconfirmed_amount** | **str** | The part of the current balance (&#x60;recent.balance&#x60;) that comes from unconfirmed rows (done false, recurring or not, dated up to now). Signed: the balance minus this is what confirmed rows add up to. Account-wide: it ignores filters and label scope, and is present even when &#x60;recent&#x60; is null. Confirming a row moves this figure, not the balance. Null when this account&#39;s balance is hidden for the caller&#39;s role. Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). | 

## Example

```python
from orbuculum_client.models.account_summary import AccountSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSummary from a JSON string
account_summary_instance = AccountSummary.from_json(json)
# print the JSON string representation of the object
print(AccountSummary.to_json())

# convert the object into a dict
account_summary_dict = account_summary_instance.to_dict()
# create an instance of AccountSummary from a dict
account_summary_from_dict = AccountSummary.from_dict(account_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


