# CreateOpenQuestion201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**OpenQuestion**](OpenQuestion.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.create_open_question201_response import CreateOpenQuestion201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOpenQuestion201Response from a JSON string
create_open_question201_response_instance = CreateOpenQuestion201Response.from_json(json)
# print the JSON string representation of the object
print(CreateOpenQuestion201Response.to_json())

# convert the object into a dict
create_open_question201_response_dict = create_open_question201_response_instance.to_dict()
# create an instance of CreateOpenQuestion201Response from a dict
create_open_question201_response_from_dict = CreateOpenQuestion201Response.from_dict(create_open_question201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


