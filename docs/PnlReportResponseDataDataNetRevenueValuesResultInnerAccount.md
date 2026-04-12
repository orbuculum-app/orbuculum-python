# PnlReportResponseDataDataNetRevenueValuesResultInnerAccount

Account identifier — always an object; summary rows have id=null

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account row ID, null for summary rows | [optional] 
**account_name** | **str** | Account name or summary label | [optional] 
**account_id** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 
**category_id** | **int** |  | [optional] 
**category_type** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_data_net_revenue_values_result_inner_account import PnlReportResponseDataDataNetRevenueValuesResultInnerAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataDataNetRevenueValuesResultInnerAccount from a JSON string
pnl_report_response_data_data_net_revenue_values_result_inner_account_instance = PnlReportResponseDataDataNetRevenueValuesResultInnerAccount.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataDataNetRevenueValuesResultInnerAccount.to_json())

# convert the object into a dict
pnl_report_response_data_data_net_revenue_values_result_inner_account_dict = pnl_report_response_data_data_net_revenue_values_result_inner_account_instance.to_dict()
# create an instance of PnlReportResponseDataDataNetRevenueValuesResultInnerAccount from a dict
pnl_report_response_data_data_net_revenue_values_result_inner_account_from_dict = PnlReportResponseDataDataNetRevenueValuesResultInnerAccount.from_dict(pnl_report_response_data_data_net_revenue_values_result_inner_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


