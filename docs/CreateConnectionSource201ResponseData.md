# CreateConnectionSource201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_key** | **str** |  | [optional] 
**sender_ids** | **str** |  | [optional] 
**receiver_ids** | **str** |  | [optional] 
**sending_data** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_connection_source201_response_data import CreateConnectionSource201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionSource201ResponseData from a JSON string
create_connection_source201_response_data_instance = CreateConnectionSource201ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateConnectionSource201ResponseData.to_json())

# convert the object into a dict
create_connection_source201_response_data_dict = create_connection_source201_response_data_instance.to_dict()
# create an instance of CreateConnectionSource201ResponseData from a dict
create_connection_source201_response_data_from_dict = CreateConnectionSource201ResponseData.from_dict(create_connection_source201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


