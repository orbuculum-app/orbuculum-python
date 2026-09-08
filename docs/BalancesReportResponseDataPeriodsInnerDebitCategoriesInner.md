# BalancesReportResponseDataPeriodsInnerDebitCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**accounts** | [**List[BalancesReportResponseDataPeriodsInnerDebitCategoriesInnerAccountsInner]**](BalancesReportResponseDataPeriodsInnerDebitCategoriesInnerAccountsInner.md) |  | 
**total** | **int** |  | 

## Example

```python
from orbuculum_client.models.balances_report_response_data_periods_inner_debit_categories_inner import BalancesReportResponseDataPeriodsInnerDebitCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataPeriodsInnerDebitCategoriesInner from a JSON string
balances_report_response_data_periods_inner_debit_categories_inner_instance = BalancesReportResponseDataPeriodsInnerDebitCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataPeriodsInnerDebitCategoriesInner.to_json())

# convert the object into a dict
balances_report_response_data_periods_inner_debit_categories_inner_dict = balances_report_response_data_periods_inner_debit_categories_inner_instance.to_dict()
# create an instance of BalancesReportResponseDataPeriodsInnerDebitCategoriesInner from a dict
balances_report_response_data_periods_inner_debit_categories_inner_from_dict = BalancesReportResponseDataPeriodsInnerDebitCategoriesInner.from_dict(balances_report_response_data_periods_inner_debit_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


