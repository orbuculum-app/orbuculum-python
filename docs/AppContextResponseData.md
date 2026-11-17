# AppContextResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_guest** | **bool** |  | [optional] 
**user_id** | **int** |  | [optional] 
**current_project_id** | **int** |  | [optional] 
**timezone** | **str** | The caller&#39;s stored time zone for this workspace (project_user.timezone, set via POST /api/user/set-timezone). null &#x3D; not set (&#39;automatic&#39;) or no workspace_id; the server then resolves request time zones from the X-Timezone header, else UTC. | [optional] 
**basic_currency_precision** | **int** |  | [optional] 
**basic_currency_code** | **str** | ISO code of the workspace basic currency (Currency.name mapped via Currency::codeOf, e.g. &#39;$&#39; → &#39;USD&#39;). Present only when workspace_id is provided AND a basic currency exists; null otherwise — symmetric with basic_currency_precision. | [optional] 
**app_version** | **str** |  | [optional] 
**csrf_param** | **str** |  | [optional] 
**csrf_token** | **str** |  | [optional] 
**can_read_reports** | **bool** |  | [optional] 
**can_create_transactions** | **bool** |  | [optional] 
**can_access_accounts** | **bool** |  | [optional] 
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


