# UserAdminUpdate200ResponseData


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
from orbuculum_client.models.user_admin_update200_response_data import UserAdminUpdate200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminUpdate200ResponseData from a JSON string
user_admin_update200_response_data_instance = UserAdminUpdate200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UserAdminUpdate200ResponseData.to_json())

# convert the object into a dict
user_admin_update200_response_data_dict = user_admin_update200_response_data_instance.to_dict()
# create an instance of UserAdminUpdate200ResponseData from a dict
user_admin_update200_response_data_from_dict = UserAdminUpdate200ResponseData.from_dict(user_admin_update200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


