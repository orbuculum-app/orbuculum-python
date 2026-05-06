# BalancesReportResponseData

Balances report payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_left** | [**List[BalancesReportResponseDataDataLeftInner]**](BalancesReportResponseDataDataLeftInner.md) | Left-side data rows with dynamic attribute keys | [optional] 
**data_right** | [**List[BalancesReportResponseDataDataLeftInner]**](BalancesReportResponseDataDataLeftInner.md) | Right-side data rows with dynamic attribute keys | [optional] 
**left_classes** | **Dict[str, str]** | CSS classes for left-side rows, keyed by row index | [optional] 
**right_classes** | **Dict[str, str]** | CSS classes for right-side rows, keyed by row index | [optional] 
**left_columns** | [**List[ReportColumnInfo]**](ReportColumnInfo.md) | Column descriptors for left-side GridView | [optional] 
**right_columns** | [**List[ReportColumnInfo]**](ReportColumnInfo.md) | Column descriptors for right-side GridView | [optional] 
**result_columns** | **List[str]** | Result column keys | [optional] 
**total** | **float** | Combined total value | [optional] 
**left_total** | **float** | Left-side total value | [optional] 
**right_total** | **float** | Right-side total value | [optional] 
**project_id** | **int** |  | [optional] 
**date_range_from** | **str** |  | [optional] 
**date_range_to** | **str** |  | [optional] 
**range** | **int** |  | [optional] 
**full_period** | **bool** |  | [optional] 
**include_future_periods** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**basic_currency** | [**ReportBasicCurrency**](ReportBasicCurrency.md) |  | [optional] 
**user_report_settings** | [**BalancesReportResponseDataUserReportSettings**](BalancesReportResponseDataUserReportSettings.md) |  | [optional] 

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


