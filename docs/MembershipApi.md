# orbuculum_client.MembershipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membership_flag_set**](MembershipApi.md#membership_flag_set) | **POST** /api/membership/flag-set | Set a member&#39;s access flag (replaces update-role)
[**membership_invite**](MembershipApi.md#membership_invite) | **POST** /api/membership/invite | Invite an existing user to the workspace (role-free)
[**membership_list**](MembershipApi.md#membership_list) | **GET** /api/membership/list | List workspace members (role-free)
[**membership_remove**](MembershipApi.md#membership_remove) | **POST** /api/membership/remove | Remove a member from the workspace


# **membership_flag_set**
> MembershipFlagSet200Response membership_flag_set(membership_flag_set_request)

Set a member's access flag (replaces update-role)

Sets exactly one of two mutually-exclusive flag forms for a member identified by user_id. Form A: full_access (boolean). Form B: permission (currency_manage | report_access | project_create) + value (boolean). Role identifiers are never accepted or returned.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.membership_flag_set200_response import MembershipFlagSet200Response
from orbuculum_client.models.membership_flag_set_request import MembershipFlagSetRequest
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
    api_instance = orbuculum_client.MembershipApi(api_client)
    membership_flag_set_request = orbuculum_client.MembershipFlagSetRequest() # MembershipFlagSetRequest | 

    try:
        # Set a member's access flag (replaces update-role)
        api_response = api_instance.membership_flag_set(membership_flag_set_request)
        print("The response of MembershipApi->membership_flag_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_flag_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_flag_set_request** | [**MembershipFlagSetRequest**](MembershipFlagSetRequest.md)|  | 

### Return type

[**MembershipFlagSet200Response**](MembershipFlagSet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag set successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Target user not a member |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict - target already has full access |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_invite**
> MembershipInvite201Response membership_invite(membership_invite_request)

Invite an existing user to the workspace (role-free)

Adds an existing (registered) user to the workspace by email. Returns the new member in the role-free contract (has_full_access; no role_id/role_name).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.membership_invite201_response import MembershipInvite201Response
from orbuculum_client.models.membership_invite_request import MembershipInviteRequest
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
    api_instance = orbuculum_client.MembershipApi(api_client)
    membership_invite_request = orbuculum_client.MembershipInviteRequest() # MembershipInviteRequest | 

    try:
        # Invite an existing user to the workspace (role-free)
        api_response = api_instance.membership_invite(membership_invite_request)
        print("The response of MembershipApi->membership_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_invite_request** | [**MembershipInviteRequest**](MembershipInviteRequest.md)|  | 

### Return type

[**MembershipInvite201Response**](MembershipInvite201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User invited |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_list**
> MembershipList200Response membership_list(workspace_id)

List workspace members (role-free)

Returns all members of the workspace. Each member carries a computed has_full_access boolean; role_id/role_name are never exposed.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.membership_list200_response import MembershipList200Response
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
    api_instance = orbuculum_client.MembershipApi(api_client)
    workspace_id = 1 # int | 

    try:
        # List workspace members (role-free)
        api_response = api_instance.membership_list(workspace_id)
        print("The response of MembershipApi->membership_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 

### Return type

[**MembershipList200Response**](MembershipList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace members |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_remove**
> MembershipRemove200Response membership_remove(membership_remove_request)

Remove a member from the workspace

Removes a member identified by their global user_id. The workspace owner cannot be removed and a caller cannot remove themselves.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.membership_remove200_response import MembershipRemove200Response
from orbuculum_client.models.membership_remove_request import MembershipRemoveRequest
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
    api_instance = orbuculum_client.MembershipApi(api_client)
    membership_remove_request = orbuculum_client.MembershipRemoveRequest() # MembershipRemoveRequest | 

    try:
        # Remove a member from the workspace
        api_response = api_instance.membership_remove(membership_remove_request)
        print("The response of MembershipApi->membership_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->membership_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_remove_request** | [**MembershipRemoveRequest**](MembershipRemoveRequest.md)|  | 

### Return type

[**MembershipRemove200Response**](MembershipRemove200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member removed |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

