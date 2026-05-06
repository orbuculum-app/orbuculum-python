# AppContextResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_guest** | **bool** |  | [optional] 
**user_id** | **int** |  | [optional] 
**current_project_id** | **int** |  | [optional] 
**timezone** | **str** |  | [optional] 
**basic_currency_precision** | **int** |  | [optional] 
**app_version** | **str** |  | [optional] 
**csrf_param** | **str** |  | [optional] 
**csrf_token** | **str** |  | [optional] 
**can_read_reports** | **bool** |  | [optional] 
**can_create_transactions** | **bool** |  | [optional] 
**can_access_accounts** | **bool** |  | [optional] 
**is_accounts_page** | **bool** |  | [optional] 
**is_reports_page** | **bool** |  | [optional] 
**is_user_area_page** | **bool** |  | [optional] 
**is_workspace_area_page** | **bool** |  | [optional] 
**account_transactions** | [**AppContextResponseDataAccountTransactions**](AppContextResponseDataAccountTransactions.md) |  | [optional] 
**reports** | [**List[AppContextResponseDataReportsInner]**](AppContextResponseDataReportsInner.md) |  | [optional] 
**user** | [**AppContextResponseDataUser**](AppContextResponseDataUser.md) |  | [optional] 
**workspace** | [**AppContextResponseDataWorkspace**](AppContextResponseDataWorkspace.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.app_context_response_data import AppContextResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AppContextResponseData from a JSON string
app_context_response_data_instance = AppContextResponseData.from_json(json)
# print the JSON string representation of the object
print(AppContextResponseData.to_json())

# convert the object into a dict
app_context_response_data_dict = app_context_response_data_instance.to_dict()
# create an instance of AppContextResponseData from a dict
app_context_response_data_from_dict = AppContextResponseData.from_dict(app_context_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


