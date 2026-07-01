# CommissionCreatedResponse

Response after successfully adding commission. `data.commission_id` is the created commission transaction ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**CommissionCreatedResponseData**](CommissionCreatedResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.commission_created_response import CommissionCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionCreatedResponse from a JSON string
commission_created_response_instance = CommissionCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(CommissionCreatedResponse.to_json())

# convert the object into a dict
commission_created_response_dict = commission_created_response_instance.to_dict()
# create an instance of CommissionCreatedResponse from a dict
commission_created_response_from_dict = CommissionCreatedResponse.from_dict(commission_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


