# ListOpenQuestions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**ListOpenQuestions200ResponseData**](ListOpenQuestions200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.list_open_questions200_response import ListOpenQuestions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListOpenQuestions200Response from a JSON string
list_open_questions200_response_instance = ListOpenQuestions200Response.from_json(json)
# print the JSON string representation of the object
print(ListOpenQuestions200Response.to_json())

# convert the object into a dict
list_open_questions200_response_dict = list_open_questions200_response_instance.to_dict()
# create an instance of ListOpenQuestions200Response from a dict
list_open_questions200_response_from_dict = ListOpenQuestions200Response.from_dict(list_open_questions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


