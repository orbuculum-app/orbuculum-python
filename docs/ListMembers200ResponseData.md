# ListMembers200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[ListMembers200ResponseDataMembersInner]**](ListMembers200ResponseDataMembersInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.list_members200_response_data import ListMembers200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListMembers200ResponseData from a JSON string
list_members200_response_data_instance = ListMembers200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ListMembers200ResponseData.to_json())

# convert the object into a dict
list_members200_response_data_dict = list_members200_response_data_instance.to_dict()
# create an instance of ListMembers200ResponseData from a dict
list_members200_response_data_from_dict = ListMembers200ResponseData.from_dict(list_members200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


