# CommissionCreatedResponseData

Created commission data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission_id** | **int** | Created commission transaction ID | 

## Example

```python
from orbuculum_client.models.commission_created_response_data import CommissionCreatedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionCreatedResponseData from a JSON string
commission_created_response_data_instance = CommissionCreatedResponseData.from_json(json)
# print the JSON string representation of the object
print(CommissionCreatedResponseData.to_json())

# convert the object into a dict
commission_created_response_data_dict = commission_created_response_data_instance.to_dict()
# create an instance of CommissionCreatedResponseData from a dict
commission_created_response_data_from_dict = CommissionCreatedResponseData.from_dict(commission_created_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


