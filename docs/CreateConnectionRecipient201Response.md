# CreateConnectionRecipient201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**CreateConnectionRecipient201ResponseData**](CreateConnectionRecipient201ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.create_connection_recipient201_response import CreateConnectionRecipient201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionRecipient201Response from a JSON string
create_connection_recipient201_response_instance = CreateConnectionRecipient201Response.from_json(json)
# print the JSON string representation of the object
print(CreateConnectionRecipient201Response.to_json())

# convert the object into a dict
create_connection_recipient201_response_dict = create_connection_recipient201_response_instance.to_dict()
# create an instance of CreateConnectionRecipient201Response from a dict
create_connection_recipient201_response_from_dict = CreateConnectionRecipient201Response.from_dict(create_connection_recipient201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


