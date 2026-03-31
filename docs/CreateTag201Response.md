# CreateTag201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**CreateTag201ResponseData**](CreateTag201ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.create_tag201_response import CreateTag201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTag201Response from a JSON string
create_tag201_response_instance = CreateTag201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTag201Response.to_json())

# convert the object into a dict
create_tag201_response_dict = create_tag201_response_instance.to_dict()
# create an instance of CreateTag201Response from a dict
create_tag201_response_from_dict = CreateTag201Response.from_dict(create_tag201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


