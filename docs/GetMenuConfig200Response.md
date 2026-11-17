# GetMenuConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | **object** | Category/entity/account tree with balances, permissions, and sorting preferences. Account rows (categories[].entities[].accounts[]) carry currency_name (the stored currency name, may be a sign such as &#39;$&#39;) and currency_code (its ISO code, e.g. &#39;USD&#39;). An account&#39;s balance is null when the requesting role may not see it (BE-369; can_show_balance is then false); an entity&#39;s balance sums only the accounts whose balance the role may see, and is null when there is none. | [optional] 

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


