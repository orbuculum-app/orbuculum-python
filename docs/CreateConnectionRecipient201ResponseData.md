# CreateConnectionRecipient201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_key** | **str** |  | [optional] 
**sender_id** | **int** |  | [optional] 
**receiver_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_connection_recipient201_response_data import CreateConnectionRecipient201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionRecipient201ResponseData from a JSON string
create_connection_recipient201_response_data_instance = CreateConnectionRecipient201ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateConnectionRecipient201ResponseData.to_json())

# convert the object into a dict
create_connection_recipient201_response_data_dict = create_connection_recipient201_response_data_instance.to_dict()
# create an instance of CreateConnectionRecipient201ResponseData from a dict
create_connection_recipient201_response_data_from_dict = CreateConnectionRecipient201ResponseData.from_dict(create_connection_recipient201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


