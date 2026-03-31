# DisconnectSocial409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.disconnect_social409_response import DisconnectSocial409Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectSocial409Response from a JSON string
disconnect_social409_response_instance = DisconnectSocial409Response.from_json(json)
# print the JSON string representation of the object
print(DisconnectSocial409Response.to_json())

# convert the object into a dict
disconnect_social409_response_dict = disconnect_social409_response_instance.to_dict()
# create an instance of DisconnectSocial409Response from a dict
disconnect_social409_response_from_dict = DisconnectSocial409Response.from_dict(disconnect_social409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


