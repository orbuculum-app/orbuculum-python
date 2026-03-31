# CreatePassword200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**CreatePassword200ResponseData**](CreatePassword200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.create_password200_response import CreatePassword200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePassword200Response from a JSON string
create_password200_response_instance = CreatePassword200Response.from_json(json)
# print the JSON string representation of the object
print(CreatePassword200Response.to_json())

# convert the object into a dict
create_password200_response_dict = create_password200_response_instance.to_dict()
# create an instance of CreatePassword200Response from a dict
create_password200_response_from_dict = CreatePassword200Response.from_dict(create_password200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


