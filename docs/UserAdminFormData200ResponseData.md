# UserAdminFormData200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserAdminFormData200ResponseDataUser**](UserAdminFormData200ResponseDataUser.md) |  | [optional] 
**available_projects** | [**List[UserAdminView200ResponseDataProjectsInner]**](UserAdminView200ResponseDataProjectsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_form_data200_response_data import UserAdminFormData200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminFormData200ResponseData from a JSON string
user_admin_form_data200_response_data_instance = UserAdminFormData200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UserAdminFormData200ResponseData.to_json())

# convert the object into a dict
user_admin_form_data200_response_data_dict = user_admin_form_data200_response_data_instance.to_dict()
# create an instance of UserAdminFormData200ResponseData from a dict
user_admin_form_data200_response_data_from_dict = UserAdminFormData200ResponseData.from_dict(user_admin_form_data200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


