# MassSetDateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**transaction_ids** | **List[int]** | Array of transaction IDs to update (max 500) | 
**var_date** | **str** | New date in Y-m-d H:i:s format | 

## Example

```python
from orbuculum_client.models.mass_set_date_request import MassSetDateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassSetDateRequest from a JSON string
mass_set_date_request_instance = MassSetDateRequest.from_json(json)
# print the JSON string representation of the object
print(MassSetDateRequest.to_json())

# convert the object into a dict
mass_set_date_request_dict = mass_set_date_request_instance.to_dict()
# create an instance of MassSetDateRequest from a dict
mass_set_date_request_from_dict = MassSetDateRequest.from_dict(mass_set_date_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


