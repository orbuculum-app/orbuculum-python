# GetMenuConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | **object** | Category/entity/account tree with balances, permissions, and sorting preferences | [optional] 

## Example

```python
from orbuculum_client.models.get_menu_config200_response import GetMenuConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMenuConfig200Response from a JSON string
get_menu_config200_response_instance = GetMenuConfig200Response.from_json(json)
# print the JSON string representation of the object
print(GetMenuConfig200Response.to_json())

# convert the object into a dict
get_menu_config200_response_dict = get_menu_config200_response_instance.to_dict()
# create an instance of GetMenuConfig200Response from a dict
get_menu_config200_response_from_dict = GetMenuConfig200Response.from_dict(get_menu_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


