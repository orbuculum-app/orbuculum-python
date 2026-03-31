# ListMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**ListMembers200ResponseData**](ListMembers200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.list_members200_response import ListMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMembers200Response from a JSON string
list_members200_response_instance = ListMembers200Response.from_json(json)
# print the JSON string representation of the object
print(ListMembers200Response.to_json())

# convert the object into a dict
list_members200_response_dict = list_members200_response_instance.to_dict()
# create an instance of ListMembers200Response from a dict
list_members200_response_from_dict = ListMembers200Response.from_dict(list_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


