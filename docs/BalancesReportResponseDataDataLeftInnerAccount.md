# BalancesReportResponseDataDataLeftInnerAccount

Row identifier — always an object with row_type discriminator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_type** | **str** | Discriminator: data&#x3D;account row, header&#x3D;entity group header, placeholder&#x3D;empty row, summary&#x3D;total row | [optional] 
**id** | **int** | Account or entity ID, null for placeholder/summary rows | [optional] 
**name** | **str** | Account name for data rows | [optional] 
**entity_name** | **str** | Entity name for header rows | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**icon_html** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.balances_report_response_data_data_left_inner_account import BalancesReportResponseDataDataLeftInnerAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataDataLeftInnerAccount from a JSON string
balances_report_response_data_data_left_inner_account_instance = BalancesReportResponseDataDataLeftInnerAccount.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataDataLeftInnerAccount.to_json())

# convert the object into a dict
balances_report_response_data_data_left_inner_account_dict = balances_report_response_data_data_left_inner_account_instance.to_dict()
# create an instance of BalancesReportResponseDataDataLeftInnerAccount from a dict
balances_report_response_data_data_left_inner_account_from_dict = BalancesReportResponseDataDataLeftInnerAccount.from_dict(balances_report_response_data_data_left_inner_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


