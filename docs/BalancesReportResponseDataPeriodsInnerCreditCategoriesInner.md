# BalancesReportResponseDataPeriodsInnerCreditCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** | Account type slug; the int id is type_id | 
**type_id** | **int** | Account type id (int); null &#x3D; P&amp;L account | 
**accounts** | [**List[BalancesReportResponseDataPeriodsInnerCreditCategoriesInnerAccountsInner]**](BalancesReportResponseDataPeriodsInnerCreditCategoriesInnerAccountsInner.md) |  | 
**total** | **int** |  | 

## Example

```python
from orbuculum_client.models.balances_report_response_data_periods_inner_credit_categories_inner import BalancesReportResponseDataPeriodsInnerCreditCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataPeriodsInnerCreditCategoriesInner from a JSON string
balances_report_response_data_periods_inner_credit_categories_inner_instance = BalancesReportResponseDataPeriodsInnerCreditCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataPeriodsInnerCreditCategoriesInner.to_json())

# convert the object into a dict
balances_report_response_data_periods_inner_credit_categories_inner_dict = balances_report_response_data_periods_inner_credit_categories_inner_instance.to_dict()
# create an instance of BalancesReportResponseDataPeriodsInnerCreditCategoriesInner from a dict
balances_report_response_data_periods_inner_credit_categories_inner_from_dict = BalancesReportResponseDataPeriodsInnerCreditCategoriesInner.from_dict(balances_report_response_data_periods_inner_credit_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


