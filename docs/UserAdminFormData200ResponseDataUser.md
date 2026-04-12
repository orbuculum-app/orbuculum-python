# UserAdminFormData200ResponseDataUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_form_data200_response_data_user import UserAdminFormData200ResponseDataUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminFormData200ResponseDataUser from a JSON string
user_admin_form_data200_response_data_user_instance = UserAdminFormData200ResponseDataUser.from_json(json)
# print the JSON string representation of the object
print(UserAdminFormData200ResponseDataUser.to_json())

# convert the object into a dict
user_admin_form_data200_response_data_user_dict = user_admin_form_data200_response_data_user_instance.to_dict()
# create an instance of UserAdminFormData200ResponseDataUser from a dict
user_admin_form_data200_response_data_user_from_dict = UserAdminFormData200ResponseDataUser.from_dict(user_admin_form_data200_response_data_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


