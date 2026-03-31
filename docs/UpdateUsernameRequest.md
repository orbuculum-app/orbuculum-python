# UpdateUsernameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 

## Example

```python
from orbuculum_client.models.update_username_request import UpdateUsernameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUsernameRequest from a JSON string
update_username_request_instance = UpdateUsernameRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUsernameRequest.to_json())

# convert the object into a dict
update_username_request_dict = update_username_request_instance.to_dict()
# create an instance of UpdateUsernameRequest from a dict
update_username_request_from_dict = UpdateUsernameRequest.from_dict(update_username_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


