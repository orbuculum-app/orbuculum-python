# orbuculum_client.MembershipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invite_member**](MembershipApi.md#invite_member) | **POST** /api/membership/invite | Invite user to workspace
[**list_members**](MembershipApi.md#list_members) | **GET** /api/membership/list | List workspace members
[**remove_member**](MembershipApi.md#remove_member) | **POST** /api/membership/remove | Remove user from workspace
[**update_member_role**](MembershipApi.md#update_member_role) | **POST** /api/membership/update-role | Update member role in workspace


# **invite_member**
> InviteMember201Response invite_member(invite_member_request)

Invite user to workspace

Invites an existing user to the workspace by email. Creates a personal role with GUEST_ACCESS permission. Requires PERMISSION_MANAGEMENT access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.invite_member201_response import InviteMember201Response
from orbuculum_client.models.invite_member_request import InviteMemberRequest
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
    invite_member_request = orbuculum_client.InviteMemberRequest() # InviteMemberRequest | 

    try:
        # Invite user to workspace
        api_response = api_instance.invite_member(invite_member_request)
        print("The response of MembershipApi->invite_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->invite_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_member_request** | [**InviteMemberRequest**](InviteMemberRequest.md)|  | 

### Return type

[**InviteMember201Response**](InviteMember201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User invited successfully |  -  |
**400** | Bad request - validation failed or invalid email format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access |  -  |
**404** | User not found - must register first |  -  |
**409** | Conflict - user already a member of this workspace |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> ListMembers200Response list_members(workspace_id)

List workspace members

Retrieves all members of a workspace with their role information. Requires PERMISSION_MANAGEMENT access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.list_members200_response import ListMembers200Response
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
    workspace_id = 1 # int | Workspace ID

    try:
        # List workspace members
        api_response = api_instance.list_members(workspace_id)
        print("The response of MembershipApi->list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->list_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 

### Return type

[**ListMembers200Response**](ListMembers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Members retrieved successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member**
> RemoveMember200Response remove_member(remove_member_request)

Remove user from workspace

Removes a user from the workspace. Cannot remove the workspace owner or yourself. Requires PERMISSION_MANAGEMENT access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.remove_member200_response import RemoveMember200Response
from orbuculum_client.models.remove_member_request import RemoveMemberRequest
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
    remove_member_request = orbuculum_client.RemoveMemberRequest() # RemoveMemberRequest | 

    try:
        # Remove user from workspace
        api_response = api_instance.remove_member(remove_member_request)
        print("The response of MembershipApi->remove_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->remove_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_member_request** | [**RemoveMemberRequest**](RemoveMemberRequest.md)|  | 

### Return type

[**RemoveMember200Response**](RemoveMember200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User removed successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access, cannot remove owner, or cannot remove self |  -  |
**404** | User not found in workspace |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_role**
> UpdateMemberRole200Response update_member_role(update_member_role_request)

Update member role in workspace

Changes a workspace member's role. Cannot change the workspace owner's role. Cannot assign owner role. Requires PERMISSION_MANAGEMENT access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_member_role200_response import UpdateMemberRole200Response
from orbuculum_client.models.update_member_role_request import UpdateMemberRoleRequest
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
    update_member_role_request = orbuculum_client.UpdateMemberRoleRequest() # UpdateMemberRoleRequest | 

    try:
        # Update member role in workspace
        api_response = api_instance.update_member_role(update_member_role_request)
        print("The response of MembershipApi->update_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipApi->update_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_member_role_request** | [**UpdateMemberRoleRequest**](UpdateMemberRoleRequest.md)|  | 

### Return type

[**UpdateMemberRole200Response**](UpdateMemberRole200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role updated successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access, cannot change owner role, or cannot assign owner role |  -  |
**404** | User or role not found in workspace |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

