# UpdateCustomRecordsResponseData

Updated custom record envelope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Success message | 
**id** | **int** | Updated record&#39;s primary key (id column of the custom table) | 

## Example

```python
from orbuculum_client.models.update_custom_records_response_data import UpdateCustomRecordsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomRecordsResponseData from a JSON string
update_custom_records_response_data_instance = UpdateCustomRecordsResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomRecordsResponseData.to_json())

# convert the object into a dict
update_custom_records_response_data_dict = update_custom_records_response_data_instance.to_dict()
# create an instance of UpdateCustomRecordsResponseData from a dict
update_custom_records_response_data_from_dict = UpdateCustomRecordsResponseData.from_dict(update_custom_records_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


