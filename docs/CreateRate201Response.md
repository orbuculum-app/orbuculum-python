# CreateRate201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**CreateRate201ResponseData**](CreateRate201ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.create_rate201_response import CreateRate201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRate201Response from a JSON string
create_rate201_response_instance = CreateRate201Response.from_json(json)
# print the JSON string representation of the object
print(CreateRate201Response.to_json())

# convert the object into a dict
create_rate201_response_dict = create_rate201_response_instance.to_dict()
# create an instance of CreateRate201Response from a dict
create_rate201_response_from_dict = CreateRate201Response.from_dict(create_rate201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


