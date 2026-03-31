# Register409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.register409_response import Register409Response

# TODO update the JSON string below
json = "{}"
# create an instance of Register409Response from a JSON string
register409_response_instance = Register409Response.from_json(json)
# print the JSON string representation of the object
print(Register409Response.to_json())

# convert the object into a dict
register409_response_dict = register409_response_instance.to_dict()
# create an instance of Register409Response from a dict
register409_response_from_dict = Register409Response.from_dict(register409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


