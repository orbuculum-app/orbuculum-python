# UpdateTagTabRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**create_tags** | **bool** | Grant tag creation permission | 
**tags** | **Dict[str, int]** | Map tag_id → access_level (1&#x3D;none, 2&#x3D;read, 3&#x3D;manage) | 

## Example

```python
from orbuculum_client.models.update_tag_tab_request import UpdateTagTabRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTagTabRequest from a JSON string
update_tag_tab_request_instance = UpdateTagTabRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTagTabRequest.to_json())

# convert the object into a dict
update_tag_tab_request_dict = update_tag_tab_request_instance.to_dict()
# create an instance of UpdateTagTabRequest from a dict
update_tag_tab_request_from_dict = UpdateTagTabRequest.from_dict(update_tag_tab_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


