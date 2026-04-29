# AccountSummary

Per-account summary (currency, precision, recent/latest sent/received/balance) returned with enriched transaction responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Account currency code (e.g. &#39;USD&#39;). Null when the account currency is unset. | [optional] 
**precision** | **int** | Decimal precision used for sent/received/balance string formatting. Defaults to 2. | 
**show_balance** | **bool** | Whether the balance values are meaningful for this account (false for accounts where balances are not tracked). | 
**recent** | [**AccountSummaryHalf**](AccountSummaryHalf.md) |  | 
**latest** | [**AccountSummaryHalf**](AccountSummaryHalf.md) |  | [optional] 

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


