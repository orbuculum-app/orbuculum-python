# orbuculum_client.TransactionDraftApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_transaction_draft**](TransactionDraftApi.md#build_transaction_draft) | **POST** /api/transaction-draft | Compose the Add-transaction modal&#39;s complete state
[**build_transaction_draft_for_edit**](TransactionDraftApi.md#build_transaction_draft_for_edit) | **POST** /api/transaction-draft/edit | Compose the Edit-transaction modal&#39;s complete state


# **build_transaction_draft**
> TransactionDraftResponse build_transaction_draft(transaction_draft_request)

Compose the Add-transaction modal's complete state

Returns the account lists with their per-slot verdicts, the modal defaults (tab, sub-tab, label, suggestion) and the current pair's validity, in one stateless call. Composes the mechanisms already shipped by BE-58/BE-64/BE-66/BE-69; no user-visible behaviour changes.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.transaction_draft_request import TransactionDraftRequest
from orbuculum_client.models.transaction_draft_response import TransactionDraftResponse
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
    api_instance = orbuculum_client.TransactionDraftApi(api_client)
    transaction_draft_request = orbuculum_client.TransactionDraftRequest() # TransactionDraftRequest | 

    try:
        # Compose the Add-transaction modal's complete state
        api_response = api_instance.build_transaction_draft(transaction_draft_request)
        print("The response of TransactionDraftApi->build_transaction_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionDraftApi->build_transaction_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_draft_request** | [**TransactionDraftRequest**](TransactionDraftRequest.md)|  | 

### Return type

[**TransactionDraftResponse**](TransactionDraftResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modal state |  -  |
**400** | Malformed JSON body, or workspace_id absent |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no access to this workspace |  -  |
**405** | Method not allowed |  -  |
**422** | Unprocessable Entity - a rule failure (unknown sub-tab, non-positive id, malformed dt), or an id that is not in this workspace. &#x60;details[]&#x60; names the offending field. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_transaction_draft_for_edit**
> TransactionDraftResponse build_transaction_draft_for_edit(transaction_draft_edit_request)

Compose the Edit-transaction modal's complete state

The same payload for a stored transaction and the Edit draft the client sends: `sender_id`, `receiver_id`, `double_id` and `label_id` replace the stored values, and each one absent or null keeps the stored value, so the client can send the whole draft on every change. The single/double shape stays the stored one. `tab`, `subtab`, `visible_subtabs` and `suggested` are always null; the account lists apply limitations and label permissions only, with no slot rules (the `edit_any` vocabulary declares every slot unfiltered).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.transaction_draft_edit_request import TransactionDraftEditRequest
from orbuculum_client.models.transaction_draft_response import TransactionDraftResponse
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
    api_instance = orbuculum_client.TransactionDraftApi(api_client)
    transaction_draft_edit_request = orbuculum_client.TransactionDraftEditRequest() # TransactionDraftEditRequest | 

    try:
        # Compose the Edit-transaction modal's complete state
        api_response = api_instance.build_transaction_draft_for_edit(transaction_draft_edit_request)
        print("The response of TransactionDraftApi->build_transaction_draft_for_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionDraftApi->build_transaction_draft_for_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_draft_edit_request** | [**TransactionDraftEditRequest**](TransactionDraftEditRequest.md)|  | 

### Return type

[**TransactionDraftResponse**](TransactionDraftResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modal state |  -  |
**400** | Malformed JSON body, or workspace_id absent |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no access to this workspace |  -  |
**404** | Not found - no such transaction, or a leg outside the caller&#39;s accessible accounts |  -  |
**405** | Method not allowed |  -  |
**422** | Unprocessable Entity - a rule failure (non-positive id, malformed dt, a non-positive or non-integer sender_id/receiver_id/double_id/label_id), or a sender_id/receiver_id/double_id/label_id that differs from the stored value and is not available in this workspace (&#x60;details[].field&#x60; names it) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

