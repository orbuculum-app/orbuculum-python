# CashflowReportResponseDataOperatingActivities

Operating activities section with cash inflow, outflow and free cash

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_inflow** | [**Dict[str, CashflowReportResponseDataOperatingActivitiesCashInflowValue]**](CashflowReportResponseDataOperatingActivitiesCashInflowValue.md) | Cash inflow rows keyed by account ID; special key &#39;inflow_total&#39; | [optional] 
**cash_outflow** | [**Dict[str, CashflowReportResponseDataOperatingActivitiesCashInflowValue]**](CashflowReportResponseDataOperatingActivitiesCashInflowValue.md) | Cash outflow rows keyed by account ID; special key &#39;outflow_total&#39; | [optional] 
**free_cash** | [**CashflowReportResponseDataOperatingActivitiesFreeCash**](CashflowReportResponseDataOperatingActivitiesFreeCash.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_operating_activities import CashflowReportResponseDataOperatingActivities

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataOperatingActivities from a JSON string
cashflow_report_response_data_operating_activities_instance = CashflowReportResponseDataOperatingActivities.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataOperatingActivities.to_json())

# convert the object into a dict
cashflow_report_response_data_operating_activities_dict = cashflow_report_response_data_operating_activities_instance.to_dict()
# create an instance of CashflowReportResponseDataOperatingActivities from a dict
cashflow_report_response_data_operating_activities_from_dict = CashflowReportResponseDataOperatingActivities.from_dict(cashflow_report_response_data_operating_activities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


