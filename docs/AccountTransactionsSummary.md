# AccountTransactionsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**currency_code** | **str** | ISO code of the account currency (&#39;&#39; when absent) | 
**precision** | **int** |  | 
**show_balance** | **bool** | Whether the requesting role may see this account&#39;s balance (BE-369). When false, recent.balance, latest.balance and opening_balance are null; sent and received are always present. | 
**recent** | [**AccountTransactionsSummaryRecent**](AccountTransactionsSummaryRecent.md) |  | [optional] 
**latest** | [**AccountTransactionsSummaryLatest**](AccountTransactionsSummaryLatest.md) |  | [optional] 
**unconfirmed_amount** | **str** | The part of the current balance (&#x60;recent.balance&#x60;) that comes from unconfirmed rows (done false, recurring or not, dated up to now). Signed: the balance minus this is what confirmed rows add up to. Account-wide: it ignores filters and label scope, and is present even when &#x60;recent&#x60; is null. Confirming a row moves this figure, not the balance. Null when this account&#39;s balance is hidden for the caller&#39;s role. | 
**opening_balance** | **str** | BE-315: the account&#39;s balance just before the date_from bound (date_from 00:00:00 in the working timezone), initial balance included: received minus sent over every transaction of the account dated before that bound, independent of the other filters and of the role&#39;s label scope (the same whole-account basis as recent.balance). Null when no date_from is sent, or when the requesting role may not see this account&#39;s balance (BE-369). Decimal string with the account currency&#39;s precision. | [optional] 

## Example

```python
from orbuculum_client.models.account_transactions_summary import AccountTransactionsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsSummary from a JSON string
account_transactions_summary_instance = AccountTransactionsSummary.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsSummary.to_json())

# convert the object into a dict
account_transactions_summary_dict = account_transactions_summary_instance.to_dict()
# create an instance of AccountTransactionsSummary from a dict
account_transactions_summary_from_dict = AccountTransactionsSummary.from_dict(account_transactions_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


