# OpenChangeSet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**ChangeSet**](ChangeSet.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.open_change_set200_response import OpenChangeSet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OpenChangeSet200Response from a JSON string
open_change_set200_response_instance = OpenChangeSet200Response.from_json(json)
# print the JSON string representation of the object
print(OpenChangeSet200Response.to_json())

# convert the object into a dict
open_change_set200_response_dict = open_change_set200_response_instance.to_dict()
# create an instance of OpenChangeSet200Response from a dict
open_change_set200_response_from_dict = OpenChangeSet200Response.from_dict(open_change_set200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


