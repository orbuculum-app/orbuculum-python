# MassSetDoneResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_count** | **int** |  | 
**processed_count** | **int** |  | 
**skipped_count** | **int** |  | 
**skipped_ids** | **List[int]** |  | 
**skipped_reasons** | **Dict[str, str]** | Map of skipped ID (as string) → reason constant | 

## Example

```python
from orbuculum_client.models.mass_set_done_response_data import MassSetDoneResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MassSetDoneResponseData from a JSON string
mass_set_done_response_data_instance = MassSetDoneResponseData.from_json(json)
# print the JSON string representation of the object
print(MassSetDoneResponseData.to_json())

# convert the object into a dict
mass_set_done_response_data_dict = mass_set_done_response_data_instance.to_dict()
# create an instance of MassSetDoneResponseData from a dict
mass_set_done_response_data_from_dict = MassSetDoneResponseData.from_dict(mass_set_done_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


