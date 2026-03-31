# CreateConnectionSource201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**CreateConnectionSource201ResponseData**](CreateConnectionSource201ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.create_connection_source201_response import CreateConnectionSource201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionSource201Response from a JSON string
create_connection_source201_response_instance = CreateConnectionSource201Response.from_json(json)
# print the JSON string representation of the object
print(CreateConnectionSource201Response.to_json())

# convert the object into a dict
create_connection_source201_response_dict = create_connection_source201_response_instance.to_dict()
# create an instance of CreateConnectionSource201Response from a dict
create_connection_source201_response_from_dict = CreateConnectionSource201Response.from_dict(create_connection_source201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


