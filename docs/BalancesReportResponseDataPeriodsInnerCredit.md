# BalancesReportResponseDataPeriodsInnerCredit

Credit side of the balance sheet for this period. Amounts come already positive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[BalancesReportResponseDataPeriodsInnerCreditCategoriesInner]**](BalancesReportResponseDataPeriodsInnerCreditCategoriesInner.md) | Categories pinned to this side, ordered by name then id | 
**financial_activity** | [**BalancesReportResponseDataPeriodsInnerCreditFinancialActivity**](BalancesReportResponseDataPeriodsInnerCreditFinancialActivity.md) |  | 
**total** | **int** | Side total; equals the opposite side&#39;s total in every period. When an account is omitted for the requesting role (BE-369), revaluation is 0 and the two side totals need not be equal. | 

## Example

```python
from orbuculum_client.models.balances_report_response_data_periods_inner_credit import BalancesReportResponseDataPeriodsInnerCredit

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataPeriodsInnerCredit from a JSON string
balances_report_response_data_periods_inner_credit_instance = BalancesReportResponseDataPeriodsInnerCredit.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataPeriodsInnerCredit.to_json())

# convert the object into a dict
balances_report_response_data_periods_inner_credit_dict = balances_report_response_data_periods_inner_credit_instance.to_dict()
# create an instance of BalancesReportResponseDataPeriodsInnerCredit from a dict
balances_report_response_data_periods_inner_credit_from_dict = BalancesReportResponseDataPeriodsInnerCredit.from_dict(balances_report_response_data_periods_inner_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


