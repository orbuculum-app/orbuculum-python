# CreateCustomRecordResponseData

Created custom record envelope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Success message | 
**id** | **int** | Created record&#39;s primary key (id column of the custom table) | 

## Example

```python
from orbuculum_client.models.create_custom_record_response_data import CreateCustomRecordResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomRecordResponseData from a JSON string
create_custom_record_response_data_instance = CreateCustomRecordResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateCustomRecordResponseData.to_json())

# convert the object into a dict
create_custom_record_response_data_dict = create_custom_record_response_data_instance.to_dict()
# create an instance of CreateCustomRecordResponseData from a dict
create_custom_record_response_data_from_dict = CreateCustomRecordResponseData.from_dict(create_custom_record_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


