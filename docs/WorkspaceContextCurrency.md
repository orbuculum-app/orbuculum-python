# WorkspaceContextCurrency

A currency with its latest rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**rate** | **str** | latest rate as a decimal string; null when the currency has no rate | 
**precision** | **int** |  | 

## Example

```python
from orbuculum_client.models.workspace_context_currency import WorkspaceContextCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextCurrency from a JSON string
workspace_context_currency_instance = WorkspaceContextCurrency.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextCurrency.to_json())

# convert the object into a dict
workspace_context_currency_dict = workspace_context_currency_instance.to_dict()
# create an instance of WorkspaceContextCurrency from a dict
workspace_context_currency_from_dict = WorkspaceContextCurrency.from_dict(workspace_context_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


