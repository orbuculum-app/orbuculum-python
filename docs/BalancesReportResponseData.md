# BalancesReportResponseData

Balances report payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | [**List[BalancesReportResponseDataPeriodsInner]**](BalancesReportResponseDataPeriodsInner.md) | One entry per report column, ascending by period start. A period is a snapshot at its end, not a sum over the period. | [optional] 
**basic_currency** | [**ReportBasicCurrency**](ReportBasicCurrency.md) |  | [optional] 
**timezone** | **str** |  | [optional] 
**effective_filters** | [**ReportEffectiveFilters**](ReportEffectiveFilters.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.balances_report_response_data import BalancesReportResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseData from a JSON string
balances_report_response_data_instance = BalancesReportResponseData.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseData.to_json())

# convert the object into a dict
balances_report_response_data_dict = balances_report_response_data_instance.to_dict()
# create an instance of BalancesReportResponseData from a dict
balances_report_response_data_from_dict = BalancesReportResponseData.from_dict(balances_report_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


