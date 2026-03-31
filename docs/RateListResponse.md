# RateListResponse

Response for GET /api/rate/list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**RateListResponseData**](RateListResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.rate_list_response import RateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateListResponse from a JSON string
rate_list_response_instance = RateListResponse.from_json(json)
# print the JSON string representation of the object
print(RateListResponse.to_json())

# convert the object into a dict
rate_list_response_dict = rate_list_response_instance.to_dict()
# create an instance of RateListResponse from a dict
rate_list_response_from_dict = RateListResponse.from_dict(rate_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


