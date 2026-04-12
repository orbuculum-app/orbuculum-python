# BalancesReportResponse

Response containing Balances report data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for GET /api/reports/get-balances | 
**data** | [**BalancesReportResponseData**](BalancesReportResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.balances_report_response import BalancesReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponse from a JSON string
balances_report_response_instance = BalancesReportResponse.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponse.to_json())

# convert the object into a dict
balances_report_response_dict = balances_report_response_instance.to_dict()
# create an instance of BalancesReportResponse from a dict
balances_report_response_from_dict = BalancesReportResponse.from_dict(balances_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


