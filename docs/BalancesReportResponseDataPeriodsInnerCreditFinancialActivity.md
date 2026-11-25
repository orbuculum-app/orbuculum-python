# BalancesReportResponseDataPeriodsInnerCreditFinancialActivity

Forex and the balancing revaluation plug. Each is pinned to one side for all columns and is 0 on the other. revaluation is 0 on both sides when an account is omitted for the requesting role (BE-369).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forex** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**revaluation** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**total** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 

## Example

```python
from orbuculum_client.models.balances_report_response_data_periods_inner_credit_financial_activity import BalancesReportResponseDataPeriodsInnerCreditFinancialActivity

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataPeriodsInnerCreditFinancialActivity from a JSON string
balances_report_response_data_periods_inner_credit_financial_activity_instance = BalancesReportResponseDataPeriodsInnerCreditFinancialActivity.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataPeriodsInnerCreditFinancialActivity.to_json())

# convert the object into a dict
balances_report_response_data_periods_inner_credit_financial_activity_dict = balances_report_response_data_periods_inner_credit_financial_activity_instance.to_dict()
# create an instance of BalancesReportResponseDataPeriodsInnerCreditFinancialActivity from a dict
balances_report_response_data_periods_inner_credit_financial_activity_from_dict = BalancesReportResponseDataPeriodsInnerCreditFinancialActivity.from_dict(balances_report_response_data_periods_inner_credit_financial_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


