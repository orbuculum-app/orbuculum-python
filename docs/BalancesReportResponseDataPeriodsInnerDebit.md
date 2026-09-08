# BalancesReportResponseDataPeriodsInnerDebit

Debit side of the balance sheet for this period

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[BalancesReportResponseDataPeriodsInnerDebitCategoriesInner]**](BalancesReportResponseDataPeriodsInnerDebitCategoriesInner.md) | Categories pinned to this side, ordered by name then id | 
**financial_activity** | [**BalancesReportResponseDataPeriodsInnerDebitFinancialActivity**](BalancesReportResponseDataPeriodsInnerDebitFinancialActivity.md) |  | 
**total** | **int** | Side total; equals the opposite side&#39;s total in every period | 

## Example

```python
from orbuculum_client.models.balances_report_response_data_periods_inner_debit import BalancesReportResponseDataPeriodsInnerDebit

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataPeriodsInnerDebit from a JSON string
balances_report_response_data_periods_inner_debit_instance = BalancesReportResponseDataPeriodsInnerDebit.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataPeriodsInnerDebit.to_json())

# convert the object into a dict
balances_report_response_data_periods_inner_debit_dict = balances_report_response_data_periods_inner_debit_instance.to_dict()
# create an instance of BalancesReportResponseDataPeriodsInnerDebit from a dict
balances_report_response_data_periods_inner_debit_from_dict = BalancesReportResponseDataPeriodsInnerDebit.from_dict(balances_report_response_data_periods_inner_debit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


