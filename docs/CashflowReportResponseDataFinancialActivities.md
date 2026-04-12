# CashflowReportResponseDataFinancialActivities

Financial activities rows keyed by account ID; special key 'total'. Empty when label_id != default label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_financial_activities import CashflowReportResponseDataFinancialActivities

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataFinancialActivities from a JSON string
cashflow_report_response_data_financial_activities_instance = CashflowReportResponseDataFinancialActivities.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataFinancialActivities.to_json())

# convert the object into a dict
cashflow_report_response_data_financial_activities_dict = cashflow_report_response_data_financial_activities_instance.to_dict()
# create an instance of CashflowReportResponseDataFinancialActivities from a dict
cashflow_report_response_data_financial_activities_from_dict = CashflowReportResponseDataFinancialActivities.from_dict(cashflow_report_response_data_financial_activities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


