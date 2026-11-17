# CloseOpenQuestion200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**OpenQuestion**](OpenQuestion.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.close_open_question200_response import CloseOpenQuestion200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CloseOpenQuestion200Response from a JSON string
close_open_question200_response_instance = CloseOpenQuestion200Response.from_json(json)
# print the JSON string representation of the object
print(CloseOpenQuestion200Response.to_json())

# convert the object into a dict
close_open_question200_response_dict = close_open_question200_response_instance.to_dict()
# create an instance of CloseOpenQuestion200Response from a dict
close_open_question200_response_from_dict = CloseOpenQuestion200Response.from_dict(close_open_question200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


