# orbuculum_client.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_permissions_for_user**](PermissionsApi.md#get_entity_permissions_for_user) | **GET** /api/permission/entity | Get a workspace member&#39;s per-entity permissions + create_entity flag (role-free, by user_id)
[**get_general_permissions**](PermissionsApi.md#get_general_permissions) | **GET** /api/permission/general | Get a workspace member&#39;s general permission flags (role-free, by user_id)
[**get_project_permissions_for_user**](PermissionsApi.md#get_project_permissions_for_user) | **GET** /api/permission/project | Get a workspace member&#39;s per-project account permissions (role-free, by user_id)
[**get_tag_permissions_for_user**](PermissionsApi.md#get_tag_permissions_for_user) | **GET** /api/permission/tag | Get a workspace member&#39;s per-tag permissions + create_tags flag (role-free, by user_id)
[**permission_manage_access**](PermissionsApi.md#permission_manage_access) | **GET** /api/permission/manage-access | Get manage-access data for account
[**permission_manage_access_save**](PermissionsApi.md#permission_manage_access_save) | **POST** /api/permission/manage-access-save | Bulk save access permissions for an account
[**permission_toggle_flag**](PermissionsApi.md#permission_toggle_flag) | **POST** /api/permission/toggle-flag | Toggle a general permission flag for a workspace member
[**permission_toggle_full_access**](PermissionsApi.md#permission_toggle_full_access) | **POST** /api/permission/toggle-full-access | Toggle full access for a workspace member
[**permission_update_account_group**](PermissionsApi.md#permission_update_account_group) | **POST** /api/permission/update-account-group | Update account permissions (Tab 3)
[**permission_update_entity_group**](PermissionsApi.md#permission_update_entity_group) | **POST** /api/permission/update-entity-group | Update entity permissions (Tab 2)
[**permission_update_project_group**](PermissionsApi.md#permission_update_project_group) | **POST** /api/permission/update-project-group | Update label permissions (Tab 4)
[**permission_update_tag_group**](PermissionsApi.md#permission_update_tag_group) | **POST** /api/permission/update-tag-group | Update tag permissions (Tab 5)


# **get_entity_permissions_for_user**
> GetEntityPermissionsResponse get_entity_permissions_for_user(workspace_id, user_id)

Get a workspace member's per-entity permissions + create_entity flag (role-free, by user_id)

Returns per-entity permission levels (read|manage) for a workspace member addressed by user_id, plus the create_entity master flag. Requires PERMISSION_MANAGEMENT.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_entity_permissions_response import GetEntityPermissionsResponse
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    workspace_id = 56 # int | 
    user_id = 56 # int | 

    try:
        # Get a workspace member's per-entity permissions + create_entity flag (role-free, by user_id)
        api_response = api_instance.get_entity_permissions_for_user(workspace_id, user_id)
        print("The response of PermissionsApi->get_entity_permissions_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_entity_permissions_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**GetEntityPermissionsResponse**](GetEntityPermissionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-entity permissions |  -  |
**400** | Missing/invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — caller lacks PERMISSION_MANAGEMENT |  -  |
**404** | User not found in workspace |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_general_permissions**
> GetGeneralPermissionsResponse get_general_permissions(workspace_id, user_id)

Get a workspace member's general permission flags (role-free, by user_id)

Returns the four general permission flags for a workspace member addressed by user_id. Requires PERMISSION_MANAGEMENT.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_general_permissions_response import GetGeneralPermissionsResponse
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    workspace_id = 56 # int | 
    user_id = 56 # int | 

    try:
        # Get a workspace member's general permission flags (role-free, by user_id)
        api_response = api_instance.get_general_permissions(workspace_id, user_id)
        print("The response of PermissionsApi->get_general_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_general_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**GetGeneralPermissionsResponse**](GetGeneralPermissionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | General permission flags |  -  |
**400** | Missing/invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — caller lacks PERMISSION_MANAGEMENT |  -  |
**404** | User not found in workspace |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_permissions_for_user**
> GetProjectPermissionsResponse get_project_permissions_for_user(workspace_id, user_id)

Get a workspace member's per-project account permissions (role-free, by user_id)

Returns, per project, the account_id → access level map (2=read, 3=manage; absent = 1 none) for a workspace member addressed by user_id — the same project_id + accounts payload POST /api/permission/update-project-group accepts. Accounts that update-project-group rejects (system accounts, accounts of system entities) are omitted. Requires PERMISSION_MANAGEMENT.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_project_permissions_response import GetProjectPermissionsResponse
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    workspace_id = 56 # int | 
    user_id = 56 # int | 

    try:
        # Get a workspace member's per-project account permissions (role-free, by user_id)
        api_response = api_instance.get_project_permissions_for_user(workspace_id, user_id)
        print("The response of PermissionsApi->get_project_permissions_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_project_permissions_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**GetProjectPermissionsResponse**](GetProjectPermissionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-project account permissions |  -  |
**400** | Missing/invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — caller lacks PERMISSION_MANAGEMENT |  -  |
**404** | User not found in workspace |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_permissions_for_user**
> GetTagPermissionsResponse get_tag_permissions_for_user(workspace_id, user_id)

Get a workspace member's per-tag permissions + create_tags flag (role-free, by user_id)

Returns per-tag permission levels (read|manage) for a workspace member addressed by user_id, plus the create_tags master flag. Requires PERMISSION_MANAGEMENT.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_tag_permissions_response import GetTagPermissionsResponse
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    workspace_id = 56 # int | 
    user_id = 56 # int | 

    try:
        # Get a workspace member's per-tag permissions + create_tags flag (role-free, by user_id)
        api_response = api_instance.get_tag_permissions_for_user(workspace_id, user_id)
        print("The response of PermissionsApi->get_tag_permissions_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_tag_permissions_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**GetTagPermissionsResponse**](GetTagPermissionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-tag permissions |  -  |
**400** | Missing/invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — caller lacks PERMISSION_MANAGEMENT |  -  |
**404** | User not found in workspace |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_manage_access**
> PermissionManageAccess200Response permission_manage_access(workspace_id, account_id)

Get manage-access data for account

Returns user-centric view of account permissions with computed lock states for the Access modal

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.permission_manage_access200_response import PermissionManageAccess200Response
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    workspace_id = 1 # int | 
    account_id = 1 # int | 

    try:
        # Get manage-access data for account
        api_response = api_instance.permission_manage_access(workspace_id, account_id)
        print("The response of PermissionsApi->permission_manage_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_manage_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **account_id** | **int**|  | 

### Return type

[**PermissionManageAccess200Response**](PermissionManageAccess200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manage access data |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_manage_access_save**
> PermissionManageAccessSave200Response permission_manage_access_save(manage_access_save_request)

Bulk save access permissions for an account

Saves all user permission changes from the Access modal in a single atomic operation. Handles permission updates and user access removal.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.manage_access_save_request import ManageAccessSaveRequest
from orbuculum_client.models.permission_manage_access_save200_response import PermissionManageAccessSave200Response
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    manage_access_save_request = orbuculum_client.ManageAccessSaveRequest() # ManageAccessSaveRequest | 

    try:
        # Bulk save access permissions for an account
        api_response = api_instance.permission_manage_access_save(manage_access_save_request)
        print("The response of PermissionsApi->permission_manage_access_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_manage_access_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_access_save_request** | [**ManageAccessSaveRequest**](ManageAccessSaveRequest.md)|  | 

### Return type

[**PermissionManageAccessSave200Response**](PermissionManageAccessSave200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions updated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT |  -  |
**404** | Account or user not found |  -  |
**409** | Role limit exceeded |  -  |
**422** | Cannot manage permissions for system account/entity |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_toggle_flag**
> PermissionToggleFlag200Response permission_toggle_flag(toggle_flag_request)

Toggle a general permission flag for a workspace member

Grants or revokes a specific permission flag. Only works when user does NOT have full access. Allowed permissions: currency_manage, report_access, project_create.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.permission_toggle_flag200_response import PermissionToggleFlag200Response
from orbuculum_client.models.toggle_flag_request import ToggleFlagRequest
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    toggle_flag_request = orbuculum_client.ToggleFlagRequest() # ToggleFlagRequest | 

    try:
        # Toggle a general permission flag for a workspace member
        api_response = api_instance.permission_toggle_flag(toggle_flag_request)
        print("The response of PermissionsApi->permission_toggle_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_toggle_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_flag_request** | [**ToggleFlagRequest**](ToggleFlagRequest.md)|  | 

### Return type

[**PermissionToggleFlag200Response**](PermissionToggleFlag200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permission flag toggled successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict - user has full access |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_toggle_full_access**
> PermissionToggleFullAccess200Response permission_toggle_full_access(toggle_full_access_request)

Toggle full access for a workspace member

Grants or revokes full access (management permission) for a user. Accepts user_id, not role_id — role resolution is handled internally.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.permission_toggle_full_access200_response import PermissionToggleFullAccess200Response
from orbuculum_client.models.toggle_full_access_request import ToggleFullAccessRequest
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    toggle_full_access_request = orbuculum_client.ToggleFullAccessRequest() # ToggleFullAccessRequest | 

    try:
        # Toggle full access for a workspace member
        api_response = api_instance.permission_toggle_full_access(toggle_full_access_request)
        print("The response of PermissionsApi->permission_toggle_full_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_toggle_full_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_full_access_request** | [**ToggleFullAccessRequest**](ToggleFullAccessRequest.md)|  | 

### Return type

[**PermissionToggleFullAccess200Response**](PermissionToggleFullAccess200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full access toggled successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_update_account_group**
> permission_update_account_group(permission_update_account_group_request)

Update account permissions (Tab 3)

Update account-level permissions for a workspace member. Sets per-account access (full access, read-only, or no access) with balance visibility and transaction hiding options.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.permission_update_account_group_request import PermissionUpdateAccountGroupRequest
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    permission_update_account_group_request = orbuculum_client.PermissionUpdateAccountGroupRequest() # PermissionUpdateAccountGroupRequest | 

    try:
        # Update account permissions (Tab 3)
        api_instance.permission_update_account_group(permission_update_account_group_request)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_update_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_update_account_group_request** | [**PermissionUpdateAccountGroupRequest**](PermissionUpdateAccountGroupRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account permissions updated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User not found |  -  |
**409** | User has full access |  -  |
**422** | Cannot manage permissions for system account/entity |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_update_entity_group**
> permission_update_entity_group(permission_update_entity_group_request)

Update entity permissions (Tab 2)

Update entity-level permissions for a workspace member. Sets entity access levels (none/read/manage), entity creation permission, and account creation permissions per entity.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.permission_update_entity_group_request import PermissionUpdateEntityGroupRequest
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    permission_update_entity_group_request = orbuculum_client.PermissionUpdateEntityGroupRequest() # PermissionUpdateEntityGroupRequest | 

    try:
        # Update entity permissions (Tab 2)
        api_instance.permission_update_entity_group(permission_update_entity_group_request)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_update_entity_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_update_entity_group_request** | [**PermissionUpdateEntityGroupRequest**](PermissionUpdateEntityGroupRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity permissions updated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User not found |  -  |
**409** | User has full access |  -  |
**422** | Cannot manage permissions for system account/entity |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_update_project_group**
> permission_update_project_group(permission_update_project_group_request)

Update label permissions (Tab 4)

Update label-level permissions for a workspace member. Sets per-account access levels for a specific project. Accounts with full access (edit permission) are skipped.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.permission_update_project_group_request import PermissionUpdateProjectGroupRequest
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    permission_update_project_group_request = orbuculum_client.PermissionUpdateProjectGroupRequest() # PermissionUpdateProjectGroupRequest | 

    try:
        # Update label permissions (Tab 4)
        api_instance.permission_update_project_group(permission_update_project_group_request)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_update_project_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_update_project_group_request** | [**PermissionUpdateProjectGroupRequest**](PermissionUpdateProjectGroupRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label permissions updated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User not found |  -  |
**409** | User has full access |  -  |
**422** | Cannot manage permissions for system account/entity |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_update_tag_group**
> permission_update_tag_group(permission_update_tag_group_request)

Update tag permissions (Tab 5)

Update tag-level permissions for a workspace member. Sets per-tag access levels (none/read/manage) and tag creation permission.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.permission_update_tag_group_request import PermissionUpdateTagGroupRequest
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
    api_instance = orbuculum_client.PermissionsApi(api_client)
    permission_update_tag_group_request = orbuculum_client.PermissionUpdateTagGroupRequest() # PermissionUpdateTagGroupRequest | 

    try:
        # Update tag permissions (Tab 5)
        api_instance.permission_update_tag_group(permission_update_tag_group_request)
    except Exception as e:
        print("Exception when calling PermissionsApi->permission_update_tag_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_update_tag_group_request** | [**PermissionUpdateTagGroupRequest**](PermissionUpdateTagGroupRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag permissions updated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User not found |  -  |
**409** | User has full access |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

