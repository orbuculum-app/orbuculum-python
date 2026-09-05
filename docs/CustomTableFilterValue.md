# CustomTableFilterValue

Value to compare against. Can be string, number, boolean, null, or array (for IN/NOT IN). Not required for IS NULL/IS NOT NULL. For ILIKE and NOT ILIKE this MUST be a non-empty string treated as a raw substring: the server wraps it in %…% (case-insensitive contains-match) and escapes literal %, _ and \\ inside it. Backward compatibility: if the value is wrapped in a single outer %…% pair it is stripped once before wrapping (so a legacy \"%john%\" still means \"contains john\"). An empty or null value for ILIKE/NOT ILIKE returns HTTP 400. Matching a string that literally begins AND ends with % is not supported under these semantics — use a shorter inner fragment or a one-sided form (%foo or foo%).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from orbuculum_client.models.custom_table_filter_value import CustomTableFilterValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTableFilterValue from a JSON string
custom_table_filter_value_instance = CustomTableFilterValue.from_json(json)
# print the JSON string representation of the object
print(CustomTableFilterValue.to_json())

# convert the object into a dict
custom_table_filter_value_dict = custom_table_filter_value_instance.to_dict()
# create an instance of CustomTableFilterValue from a dict
custom_table_filter_value_from_dict = CustomTableFilterValue.from_dict(custom_table_filter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


