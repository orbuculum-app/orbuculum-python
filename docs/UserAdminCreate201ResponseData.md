# UserAdminCreate201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_create201_response_data import UserAdminCreate201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminCreate201ResponseData from a JSON string
user_admin_create201_response_data_instance = UserAdminCreate201ResponseData.from_json(json)
# print the JSON string representation of the object
print(UserAdminCreate201ResponseData.to_json())

# convert the object into a dict
user_admin_create201_response_data_dict = user_admin_create201_response_data_instance.to_dict()
# create an instance of UserAdminCreate201ResponseData from a dict
user_admin_create201_response_data_from_dict = UserAdminCreate201ResponseData.from_dict(user_admin_create201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


