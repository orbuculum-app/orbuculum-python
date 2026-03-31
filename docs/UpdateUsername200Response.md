# UpdateUsername200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UpdateUsername200ResponseData**](UpdateUsername200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.update_username200_response import UpdateUsername200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUsername200Response from a JSON string
update_username200_response_instance = UpdateUsername200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateUsername200Response.to_json())

# convert the object into a dict
update_username200_response_dict = update_username200_response_instance.to_dict()
# create an instance of UpdateUsername200Response from a dict
update_username200_response_from_dict = UpdateUsername200Response.from_dict(update_username200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


