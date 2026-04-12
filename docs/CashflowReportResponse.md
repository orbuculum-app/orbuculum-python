# CashflowReportResponse

Response containing Cash Flow report data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for GET /api/reports/get-cashflow | 
**data** | [**CashflowReportResponseData**](CashflowReportResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.cashflow_report_response import CashflowReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponse from a JSON string
cashflow_report_response_instance = CashflowReportResponse.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponse.to_json())

# convert the object into a dict
cashflow_report_response_dict = cashflow_report_response_instance.to_dict()
# create an instance of CashflowReportResponse from a dict
cashflow_report_response_from_dict = CashflowReportResponse.from_dict(cashflow_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


