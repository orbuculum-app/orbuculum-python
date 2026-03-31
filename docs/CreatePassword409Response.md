# CreatePassword409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_password409_response import CreatePassword409Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePassword409Response from a JSON string
create_password409_response_instance = CreatePassword409Response.from_json(json)
# print the JSON string representation of the object
print(CreatePassword409Response.to_json())

# convert the object into a dict
create_password409_response_dict = create_password409_response_instance.to_dict()
# create an instance of CreatePassword409Response from a dict
create_password409_response_from_dict = CreatePassword409Response.from_dict(create_password409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


