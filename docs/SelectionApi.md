# orbuculum_client.SelectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_selection_tree**](SelectionApi.md#get_selection_tree) | **GET** /api/selection/tree | Get filtered entity/account tree


# **get_selection_tree**
> GetSelectionTree200Response get_selection_tree(workspace_id, selection_type=selection_type, mode=mode, manageable=manageable, show_hidden=show_hidden, account_id=account_id, tag_id=tag_id)

Get filtered entity/account tree

Returns a filtered entity→accounts tree for the universal picker component. Supports 8 selection types with different filtering logic. The 'author' type returns a user list instead of an account tree.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_selection_tree200_response import GetSelectionTree200Response
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.SelectionApi(api_client)
    workspace_id = 1 # int | Workspace ID
    selection_type = all # str | Selection type filter. Allowed: all, author, counterparty, replacement, account_in_tag, commission, sending_commission, import_counterparty_list (optional) (default to all)
    mode = leaf # str | Tree mode. 'leaf' = entities disabled, accounts selectable. 'entities' = entities selectable, accounts disabled. (optional) (default to leaf)
    manageable = 1 # int | Filter by manage (1) or view (0) permission (optional) (default to 1)
    show_hidden = 0 # int | Include hidden entities/accounts (0 = exclude, 1 = include) (optional) (default to 0)
    account_id = 0 # int | Context account ID (used by counterparty, replacement, commission, sending_commission, import_counterparty_list) (optional) (default to 0)
    tag_id = 0 # int | Context tag/group ID (used by account_in_tag) (optional) (default to 0)

    try:
        # Get filtered entity/account tree
        api_response = api_instance.get_selection_tree(workspace_id, selection_type=selection_type, mode=mode, manageable=manageable, show_hidden=show_hidden, account_id=account_id, tag_id=tag_id)
        print("The response of SelectionApi->get_selection_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectionApi->get_selection_tree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **selection_type** | **str**| Selection type filter. Allowed: all, author, counterparty, replacement, account_in_tag, commission, sending_commission, import_counterparty_list | [optional] [default to all]
 **mode** | **str**| Tree mode. &#39;leaf&#39; &#x3D; entities disabled, accounts selectable. &#39;entities&#39; &#x3D; entities selectable, accounts disabled. | [optional] [default to leaf]
 **manageable** | **int**| Filter by manage (1) or view (0) permission | [optional] [default to 1]
 **show_hidden** | **int**| Include hidden entities/accounts (0 &#x3D; exclude, 1 &#x3D; include) | [optional] [default to 0]
 **account_id** | **int**| Context account ID (used by counterparty, replacement, commission, sending_commission, import_counterparty_list) | [optional] [default to 0]
 **tag_id** | **int**| Context tag/group ID (used by account_in_tag) | [optional] [default to 0]

### Return type

[**GetSelectionTree200Response**](GetSelectionTree200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Selection tree retrieved successfully |  -  |
**400** | Bad request - invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

