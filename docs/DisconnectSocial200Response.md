# DisconnectSocial200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**DisconnectSocial200ResponseData**](DisconnectSocial200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.disconnect_social200_response import DisconnectSocial200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectSocial200Response from a JSON string
disconnect_social200_response_instance = DisconnectSocial200Response.from_json(json)
# print the JSON string representation of the object
print(DisconnectSocial200Response.to_json())

# convert the object into a dict
disconnect_social200_response_dict = disconnect_social200_response_instance.to_dict()
# create an instance of DisconnectSocial200Response from a dict
disconnect_social200_response_from_dict = DisconnectSocial200Response.from_dict(disconnect_social200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


