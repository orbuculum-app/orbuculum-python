# CreateConnectionSourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**sender_ids** | **str** | Comma-separated sender account IDs | 
**receiver_ids** | **str** | Comma-separated receiver account IDs | 
**receiving_data** | **str** | Data sending configuration | 

## Example

```python
from orbuculum_client.models.create_connection_source_request import CreateConnectionSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionSourceRequest from a JSON string
create_connection_source_request_instance = CreateConnectionSourceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConnectionSourceRequest.to_json())

# convert the object into a dict
create_connection_source_request_dict = create_connection_source_request_instance.to_dict()
# create an instance of CreateConnectionSourceRequest from a dict
create_connection_source_request_from_dict = CreateConnectionSourceRequest.from_dict(create_connection_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


