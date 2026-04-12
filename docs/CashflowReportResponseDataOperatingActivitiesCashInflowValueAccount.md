# CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount

Account identifier — always an object; summary rows have id=null

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account row ID, null for summary rows | [optional] 
**entity_name** | **str** | Entity name or summary label | [optional] 
**account_name** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_type_icon** | **str** |  | [optional] 
**account_id** | **int** |  | [optional] 
**currency_name** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_operating_activities_cash_inflow_value_account import CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount from a JSON string
cashflow_report_response_data_operating_activities_cash_inflow_value_account_instance = CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount.to_json())

# convert the object into a dict
cashflow_report_response_data_operating_activities_cash_inflow_value_account_dict = cashflow_report_response_data_operating_activities_cash_inflow_value_account_instance.to_dict()
# create an instance of CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount from a dict
cashflow_report_response_data_operating_activities_cash_inflow_value_account_from_dict = CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount.from_dict(cashflow_report_response_data_operating_activities_cash_inflow_value_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


