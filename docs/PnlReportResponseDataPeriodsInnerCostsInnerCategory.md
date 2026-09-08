# PnlReportResponseDataPeriodsInnerCostsInnerCategory

The row's category. id is the account's entity_id and is present even when no Entity resolved — never read it as proof the category exists. type is a non-null slug; an unresolved or PoL category is 'pol'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_periods_inner_costs_inner_category import PnlReportResponseDataPeriodsInnerCostsInnerCategory

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataPeriodsInnerCostsInnerCategory from a JSON string
pnl_report_response_data_periods_inner_costs_inner_category_instance = PnlReportResponseDataPeriodsInnerCostsInnerCategory.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataPeriodsInnerCostsInnerCategory.to_json())

# convert the object into a dict
pnl_report_response_data_periods_inner_costs_inner_category_dict = pnl_report_response_data_periods_inner_costs_inner_category_instance.to_dict()
# create an instance of PnlReportResponseDataPeriodsInnerCostsInnerCategory from a dict
pnl_report_response_data_periods_inner_costs_inner_category_from_dict = PnlReportResponseDataPeriodsInnerCostsInnerCategory.from_dict(pnl_report_response_data_periods_inner_costs_inner_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


