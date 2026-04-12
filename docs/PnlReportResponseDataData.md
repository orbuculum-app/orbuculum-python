# PnlReportResponseDataData

Report data rows grouped by section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_revenue_values_result** | [**List[PnlReportResponseDataDataNetRevenueValuesResultInner]**](PnlReportResponseDataDataNetRevenueValuesResultInner.md) | Net revenue rows | [optional] 
**gross_profit_values_result** | [**List[PnlReportResponseDataDataNetRevenueValuesResultInner]**](PnlReportResponseDataDataNetRevenueValuesResultInner.md) | Gross profit rows | [optional] 
**net_profit_values_total** | [**List[PnlReportResponseDataDataNetRevenueValuesResultInner]**](PnlReportResponseDataDataNetRevenueValuesResultInner.md) | Net profit rows | [optional] 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_data import PnlReportResponseDataData

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataData from a JSON string
pnl_report_response_data_data_instance = PnlReportResponseDataData.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataData.to_json())

# convert the object into a dict
pnl_report_response_data_data_dict = pnl_report_response_data_data_instance.to_dict()
# create an instance of PnlReportResponseDataData from a dict
pnl_report_response_data_data_from_dict = PnlReportResponseDataData.from_dict(pnl_report_response_data_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


