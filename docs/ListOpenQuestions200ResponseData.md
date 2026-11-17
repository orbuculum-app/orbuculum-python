# ListOpenQuestions200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OpenQuestion]**](OpenQuestion.md) |  | [optional] 
**total** | **int** | Number of questions matching the filters and visible to the caller | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.list_open_questions200_response_data import ListOpenQuestions200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListOpenQuestions200ResponseData from a JSON string
list_open_questions200_response_data_instance = ListOpenQuestions200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ListOpenQuestions200ResponseData.to_json())

# convert the object into a dict
list_open_questions200_response_data_dict = list_open_questions200_response_data_instance.to_dict()
# create an instance of ListOpenQuestions200ResponseData from a dict
list_open_questions200_response_data_from_dict = ListOpenQuestions200ResponseData.from_dict(list_open_questions200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


