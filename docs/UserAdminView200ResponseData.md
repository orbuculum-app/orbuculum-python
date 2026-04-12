# UserAdminView200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**status_label** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 
**projects** | [**List[UserAdminView200ResponseDataProjectsInner]**](UserAdminView200ResponseDataProjectsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_view200_response_data import UserAdminView200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminView200ResponseData from a JSON string
user_admin_view200_response_data_instance = UserAdminView200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UserAdminView200ResponseData.to_json())

# convert the object into a dict
user_admin_view200_response_data_dict = user_admin_view200_response_data_instance.to_dict()
# create an instance of UserAdminView200ResponseData from a dict
user_admin_view200_response_data_from_dict = UserAdminView200ResponseData.from_dict(user_admin_view200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


