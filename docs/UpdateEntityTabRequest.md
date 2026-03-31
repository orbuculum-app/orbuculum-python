# UpdateEntityTabRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**create_entity** | **bool** | Grant entity creation permission | 
**entities** | **Dict[str, int]** | Map entity_id → access_level (1&#x3D;none, 2&#x3D;read, 3&#x3D;manage) | 
**create_accounts** | **Dict[str, bool]** | Map entity_id → bool (can create accounts) | [optional] 

## Example

```python
from orbuculum_client.models.update_entity_tab_request import UpdateEntityTabRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityTabRequest from a JSON string
update_entity_tab_request_instance = UpdateEntityTabRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityTabRequest.to_json())

# convert the object into a dict
update_entity_tab_request_dict = update_entity_tab_request_instance.to_dict()
# create an instance of UpdateEntityTabRequest from a dict
update_entity_tab_request_from_dict = UpdateEntityTabRequest.from_dict(update_entity_tab_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


