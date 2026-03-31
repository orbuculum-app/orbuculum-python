# MassSetDoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**transaction_ids** | **List[int]** | Array of transaction IDs to update (max 500) | 
**done** | **bool** | true &#x3D; set done, false &#x3D; set undone | 

## Example

```python
from orbuculum_client.models.mass_set_done_request import MassSetDoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassSetDoneRequest from a JSON string
mass_set_done_request_instance = MassSetDoneRequest.from_json(json)
# print the JSON string representation of the object
print(MassSetDoneRequest.to_json())

# convert the object into a dict
mass_set_done_request_dict = mass_set_done_request_instance.to_dict()
# create an instance of MassSetDoneRequest from a dict
mass_set_done_request_from_dict = MassSetDoneRequest.from_dict(mass_set_done_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


