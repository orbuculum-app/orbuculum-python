# ListTags200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**account_count** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.list_tags200_response_data_inner import ListTags200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTags200ResponseDataInner from a JSON string
list_tags200_response_data_inner_instance = ListTags200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListTags200ResponseDataInner.to_json())

# convert the object into a dict
list_tags200_response_data_inner_dict = list_tags200_response_data_inner_instance.to_dict()
# create an instance of ListTags200ResponseDataInner from a dict
list_tags200_response_data_inner_from_dict = ListTags200ResponseDataInner.from_dict(list_tags200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


