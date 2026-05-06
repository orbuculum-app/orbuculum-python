# AppContextResponseDataUserLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**icon_key** | **str** |  | [optional] 
**children** | [**List[AppContextResponseDataUserLinksInnerChildrenInner]**](AppContextResponseDataUserLinksInnerChildrenInner.md) | Present only on group entries (e.g. Admin). Nested items share the link-item shape. | [optional] 

## Example

```python
from orbuculum_client.models.app_context_response_data_user_links_inner import AppContextResponseDataUserLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of AppContextResponseDataUserLinksInner from a JSON string
app_context_response_data_user_links_inner_instance = AppContextResponseDataUserLinksInner.from_json(json)
# print the JSON string representation of the object
print(AppContextResponseDataUserLinksInner.to_json())

# convert the object into a dict
app_context_response_data_user_links_inner_dict = app_context_response_data_user_links_inner_instance.to_dict()
# create an instance of AppContextResponseDataUserLinksInner from a dict
app_context_response_data_user_links_inner_from_dict = AppContextResponseDataUserLinksInner.from_dict(app_context_response_data_user_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


