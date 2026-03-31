# ChangeEmail409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.change_email409_response import ChangeEmail409Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEmail409Response from a JSON string
change_email409_response_instance = ChangeEmail409Response.from_json(json)
# print the JSON string representation of the object
print(ChangeEmail409Response.to_json())

# convert the object into a dict
change_email409_response_dict = change_email409_response_instance.to_dict()
# create an instance of ChangeEmail409Response from a dict
change_email409_response_from_dict = ChangeEmail409Response.from_dict(change_email409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


