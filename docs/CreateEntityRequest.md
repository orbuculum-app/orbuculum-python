# CreateEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**name** | **str** | Entity name | 
**type** | **int** | Entity type. Allowed: null, 1 (DEBT), 2 (ACC, default), 3 (IGNORE), 5 (CFONLY_ACCOUNT), 8 (CFONLY_SOURCE), 9 (REVENUE), 10 (COSTS). | [optional] 

## Example

```python
from orbuculum_client.models.create_entity_request import CreateEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityRequest from a JSON string
create_entity_request_instance = CreateEntityRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEntityRequest.to_json())

# convert the object into a dict
create_entity_request_dict = create_entity_request_instance.to_dict()
# create an instance of CreateEntityRequest from a dict
create_entity_request_from_dict = CreateEntityRequest.from_dict(create_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


