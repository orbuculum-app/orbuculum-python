# WorkspaceContextAccountType

Type, source and commission settings of one account, plus its hidden flag, currency, entity and send/receive ordering timestamps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Account type code; null &#x3D; PoL account | 
**source** | **str** | &#39;PoL&#39;, &#39;revenue&#39;, &#39;costs&#39; or &#39;&#39; (empty string) | 
**commission_account_id** | **int** |  | 
**custom_commission_sender_id** | **int** |  | 
**commission_appliance** | **bool** |  | 
**hidden** | **bool** |  | 
**currency_id** | **int** |  | 
**entity_id** | **int** |  | 
**send_ts** | **int** |  | 
**receive_ts** | **int** |  | 

## Example

```python
from orbuculum_client.models.workspace_context_account_type import WorkspaceContextAccountType

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextAccountType from a JSON string
workspace_context_account_type_instance = WorkspaceContextAccountType.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextAccountType.to_json())

# convert the object into a dict
workspace_context_account_type_dict = workspace_context_account_type_instance.to_dict()
# create an instance of WorkspaceContextAccountType from a dict
workspace_context_account_type_from_dict = WorkspaceContextAccountType.from_dict(workspace_context_account_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


