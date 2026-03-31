# CreatePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from orbuculum_client.models.create_password_request import CreatePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasswordRequest from a JSON string
create_password_request_instance = CreatePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePasswordRequest.to_json())

# convert the object into a dict
create_password_request_dict = create_password_request_instance.to_dict()
# create an instance of CreatePasswordRequest from a dict
create_password_request_from_dict = CreatePasswordRequest.from_dict(create_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


