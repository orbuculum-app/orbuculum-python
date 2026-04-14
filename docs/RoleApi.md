# orbuculum_client.RoleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RoleApi.md#create_role) | **POST** /api/role/create | Create role
[**delete_role**](RoleApi.md#delete_role) | **POST** /api/role/delete | Delete role
[**get_roles**](RoleApi.md#get_roles) | **GET** /api/role/get | Get roles
[**update_role**](RoleApi.md#update_role) | **POST** /api/role/update | Update role


# **create_role**
> CreateRole201Response create_role(create_role_request)

Create role

Creates a new role in the workspace. Requires PERMISSION_MANAGEMENT access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_role201_response import CreateRole201Response
from orbuculum_client.models.create_role_request import CreateRoleRequest
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
    api_instance = orbuculum_client.RoleApi(api_client)
    create_role_request = orbuculum_client.CreateRoleRequest() # CreateRoleRequest | 

    try:
        # Create role
        api_response = api_instance.create_role(create_role_request)
        print("The response of RoleApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)|  | 

### Return type

[**CreateRole201Response**](CreateRole201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Role created successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access |  -  |
**409** | Conflict - role name already exists |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> DeleteRole200Response delete_role(delete_role_request)

Delete role

Deletes a role from the workspace. Requires PERMISSION_MANAGEMENT access. Default roles and roles with assigned members cannot be deleted.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_role200_response import DeleteRole200Response
from orbuculum_client.models.delete_role_request import DeleteRoleRequest
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
    api_instance = orbuculum_client.RoleApi(api_client)
    delete_role_request = orbuculum_client.DeleteRoleRequest() # DeleteRoleRequest | 

    try:
        # Delete role
        api_response = api_instance.delete_role(delete_role_request)
        print("The response of RoleApi->delete_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_role_request** | [**DeleteRoleRequest**](DeleteRoleRequest.md)|  | 

### Return type

[**DeleteRole200Response**](DeleteRole200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role deleted successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access or cannot delete default/assigned role |  -  |
**404** | Role not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> GetRoles200Response get_roles(workspace_id, id=id)

Get roles

Retrieves all roles for a workspace or a specific role by ID. Returns role details including name, default status, and member count.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_roles200_response import GetRoles200Response
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
    api_instance = orbuculum_client.RoleApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 1 # int | Role ID (optional, returns all roles if not specified) (optional)

    try:
        # Get roles
        api_response = api_instance.get_roles(workspace_id, id=id)
        print("The response of RoleApi->get_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Role ID (optional, returns all roles if not specified) | [optional] 

### Return type

[**GetRoles200Response**](GetRoles200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Roles retrieved successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> UpdateRole200Response update_role(update_role_request)

Update role

Updates an existing role name. Requires PERMISSION_MANAGEMENT access. Default roles cannot be renamed.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_role200_response import UpdateRole200Response
from orbuculum_client.models.update_role_request import UpdateRoleRequest
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
    api_instance = orbuculum_client.RoleApi(api_client)
    update_role_request = orbuculum_client.UpdateRoleRequest() # UpdateRoleRequest | 

    try:
        # Update role
        api_response = api_instance.update_role(update_role_request)
        print("The response of RoleApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)|  | 

### Return type

[**UpdateRole200Response**](UpdateRole200Response.md)

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
**403** | Forbidden - no PERMISSION_MANAGEMENT access or cannot modify default role |  -  |
**404** | Role not found |  -  |
**409** | Conflict - role name already exists |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

