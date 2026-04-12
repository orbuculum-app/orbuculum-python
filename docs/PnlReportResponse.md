# PnlReportResponse

Response containing P&L report data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for GET /api/reports/get-pnl | 
**data** | [**PnlReportResponseData**](PnlReportResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.pnl_report_response import PnlReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponse from a JSON string
pnl_report_response_instance = PnlReportResponse.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponse.to_json())

# convert the object into a dict
pnl_report_response_dict = pnl_report_response_instance.to_dict()
# create an instance of PnlReportResponse from a dict
pnl_report_response_from_dict = PnlReportResponse.from_dict(pnl_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


