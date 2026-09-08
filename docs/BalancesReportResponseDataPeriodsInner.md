# BalancesReportResponseDataPeriodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**BalancesReportResponseDataPeriodsInnerPeriod**](BalancesReportResponseDataPeriodsInnerPeriod.md) |  | 
**debit** | [**BalancesReportResponseDataPeriodsInnerDebit**](BalancesReportResponseDataPeriodsInnerDebit.md) |  | 
**credit** | [**BalancesReportResponseDataPeriodsInnerCredit**](BalancesReportResponseDataPeriodsInnerCredit.md) |  | 

## Example

```python
from orbuculum_client.models.balances_report_response_data_periods_inner import BalancesReportResponseDataPeriodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataPeriodsInner from a JSON string
balances_report_response_data_periods_inner_instance = BalancesReportResponseDataPeriodsInner.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataPeriodsInner.to_json())

# convert the object into a dict
balances_report_response_data_periods_inner_dict = balances_report_response_data_periods_inner_instance.to_dict()
# create an instance of BalancesReportResponseDataPeriodsInner from a dict
balances_report_response_data_periods_inner_from_dict = BalancesReportResponseDataPeriodsInner.from_dict(balances_report_response_data_periods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


