# Register201ResponseDataUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.register201_response_data_user import Register201ResponseDataUser

# TODO update the JSON string below
json = "{}"
# create an instance of Register201ResponseDataUser from a JSON string
register201_response_data_user_instance = Register201ResponseDataUser.from_json(json)
# print the JSON string representation of the object
print(Register201ResponseDataUser.to_json())

# convert the object into a dict
register201_response_data_user_dict = register201_response_data_user_instance.to_dict()
# create an instance of Register201ResponseDataUser from a dict
register201_response_data_user_from_dict = Register201ResponseDataUser.from_dict(register201_response_data_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


