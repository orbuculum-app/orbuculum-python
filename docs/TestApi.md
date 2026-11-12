# orbuculum_client.TestApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_workspace_create**](TestApi.md#test_workspace_create) | **POST** /api/test/workspace-create | Test only: create a workspace from a fixture database
[**test_workspace_delete**](TestApi.md#test_workspace_delete) | **POST** /api/test/workspace-delete | Test only: delete a fixture clone and its database
[**test_workspace_reset**](TestApi.md#test_workspace_reset) | **POST** /api/test/workspace-reset | Test only: recreate a fixture clone&#39;s database from its fixture


# **test_workspace_create**
> WorkspaceFixtureCloneResponse test_workspace_create(create_workspace_from_fixture_request)

Test only: create a workspace from a fixture database

Answers 404 unless params.enableTestEndpoints is on. The caller becomes the workspace's admin.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_workspace_from_fixture_request import CreateWorkspaceFromFixtureRequest
from orbuculum_client.models.workspace_fixture_clone_response import WorkspaceFixtureCloneResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
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
    api_instance = orbuculum_client.TestApi(api_client)
    create_workspace_from_fixture_request = orbuculum_client.CreateWorkspaceFromFixtureRequest() # CreateWorkspaceFromFixtureRequest | 

    try:
        # Test only: create a workspace from a fixture database
        api_response = api_instance.test_workspace_create(create_workspace_from_fixture_request)
        print("The response of TestApi->test_workspace_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->test_workspace_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_from_fixture_request** | [**CreateWorkspaceFromFixtureRequest**](CreateWorkspaceFromFixtureRequest.md)|  | 

### Return type

[**WorkspaceFixtureCloneResponse**](WorkspaceFixtureCloneResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workspace created |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**404** | Test endpoints are off |  -  |
**405** | Method not allowed |  -  |
**409** | Fixture database is in use |  -  |
**422** | Invalid or unknown fixture name |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_workspace_delete**
> WorkspaceDeletedResponse test_workspace_delete(delete_workspace_request)

Test only: delete a fixture clone and its database

Answers 404 unless params.enableTestEndpoints is on. Refuses a workspace that is not a fixture clone.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_workspace_request import DeleteWorkspaceRequest
from orbuculum_client.models.workspace_deleted_response import WorkspaceDeletedResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
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
    api_instance = orbuculum_client.TestApi(api_client)
    delete_workspace_request = orbuculum_client.DeleteWorkspaceRequest() # DeleteWorkspaceRequest | 

    try:
        # Test only: delete a fixture clone and its database
        api_response = api_instance.test_workspace_delete(delete_workspace_request)
        print("The response of TestApi->test_workspace_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->test_workspace_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_workspace_request** | [**DeleteWorkspaceRequest**](DeleteWorkspaceRequest.md)|  | 

### Return type

[**WorkspaceDeletedResponse**](WorkspaceDeletedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace deleted |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**403** | No access, insufficient role, or not a fixture clone |  -  |
**404** | Test endpoints are off, or workspace not found |  -  |
**405** | Method not allowed |  -  |
**422** | Invalid workspace_id |  -  |
**500** | Server error |  -  |
**503** | Failed to drop the database, retry possible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_workspace_reset**
> WorkspaceFixtureCloneResponse test_workspace_reset(delete_workspace_request)

Test only: recreate a fixture clone's database from its fixture

Answers 404 unless params.enableTestEndpoints is on. Refuses a workspace that is not a fixture clone.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_workspace_request import DeleteWorkspaceRequest
from orbuculum_client.models.workspace_fixture_clone_response import WorkspaceFixtureCloneResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
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
    api_instance = orbuculum_client.TestApi(api_client)
    delete_workspace_request = orbuculum_client.DeleteWorkspaceRequest() # DeleteWorkspaceRequest | 

    try:
        # Test only: recreate a fixture clone's database from its fixture
        api_response = api_instance.test_workspace_reset(delete_workspace_request)
        print("The response of TestApi->test_workspace_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->test_workspace_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_workspace_request** | [**DeleteWorkspaceRequest**](DeleteWorkspaceRequest.md)|  | 

### Return type

[**WorkspaceFixtureCloneResponse**](WorkspaceFixtureCloneResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace reset |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**403** | No access, insufficient role, or not a fixture clone |  -  |
**404** | Test endpoints are off, or workspace or its database not found |  -  |
**405** | Method not allowed |  -  |
**409** | Fixture database is in use |  -  |
**422** | Invalid workspace_id, or the fixture database no longer exists |  -  |
**500** | Server error |  -  |
**503** | Failed to drop the database, retry possible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

