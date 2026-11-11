# orbuculum_client.ProjectApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /api/project/create | Create project
[**delete_project**](ProjectApi.md#delete_project) | **POST** /api/project/delete | Delete an existing project
[**get_project**](ProjectApi.md#get_project) | **GET** /api/project/get | Get project
[**update_project**](ProjectApi.md#update_project) | **POST** /api/project/update | Update project


# **create_project**
> ProjectCreatedResponse create_project(create_project_request, x_orbuculum_change_set=x_orbuculum_change_set)

Create project

Creates a new project for organizing and categorizing transactions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_project_request import CreateProjectRequest
from orbuculum_client.models.project_created_response import ProjectCreatedResponse
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
    api_instance = orbuculum_client.ProjectApi(api_client)
    create_project_request = orbuculum_client.CreateProjectRequest() # CreateProjectRequest | 
    x_orbuculum_change_set = 56 # int | Id of an explicit change set opened with POST /api/change-set/open. The request's writes of transactions, accounts, counterparties and labels are recorded into that set. If the set was opened with mode=propose, every write of the request is rolled back and the response is 200 with data = the ChangeSet (items with before/after) instead of the endpoint's usual body; requests to a proposed set are each evaluated against the committed book, so send dependent operations in one request (e.g. one /api/transaction/mutate call). Without this header the server records the writes into an implicit set. (optional)

    try:
        # Create project
        api_response = api_instance.create_project(create_project_request, x_orbuculum_change_set=x_orbuculum_change_set)
        print("The response of ProjectApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 
 **x_orbuculum_change_set** | **int**| Id of an explicit change set opened with POST /api/change-set/open. The request&#39;s writes of transactions, accounts, counterparties and labels are recorded into that set. If the set was opened with mode&#x3D;propose, every write of the request is rolled back and the response is 200 with data &#x3D; the ChangeSet (items with before/after) instead of the endpoint&#39;s usual body; requests to a proposed set are each evaluated against the committed book, so send dependent operations in one request (e.g. one /api/transaction/mutate call). Without this header the server records the writes into an implicit set. | [optional] 

### Return type

[**ProjectCreatedResponse**](ProjectCreatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project created successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**409** | Conflict - project name already exists |  -  |
**422** | Validation failed - unknown or non-writable icon/colour name |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> SuccessResponse delete_project(delete_project_request, x_orbuculum_change_set=x_orbuculum_change_set)

Delete an existing project

Permanently deletes a project from the system. This action cannot be undone.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_project_request import DeleteProjectRequest
from orbuculum_client.models.success_response import SuccessResponse
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
    api_instance = orbuculum_client.ProjectApi(api_client)
    delete_project_request = orbuculum_client.DeleteProjectRequest() # DeleteProjectRequest | 
    x_orbuculum_change_set = 56 # int | Id of an explicit change set opened with POST /api/change-set/open. The request's writes of transactions, accounts, counterparties and labels are recorded into that set. If the set was opened with mode=propose, every write of the request is rolled back and the response is 200 with data = the ChangeSet (items with before/after) instead of the endpoint's usual body; requests to a proposed set are each evaluated against the committed book, so send dependent operations in one request (e.g. one /api/transaction/mutate call). Without this header the server records the writes into an implicit set. (optional)

    try:
        # Delete an existing project
        api_response = api_instance.delete_project(delete_project_request, x_orbuculum_change_set=x_orbuculum_change_set)
        print("The response of ProjectApi->delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_project_request** | [**DeleteProjectRequest**](DeleteProjectRequest.md)|  | 
 **x_orbuculum_change_set** | **int**| Id of an explicit change set opened with POST /api/change-set/open. The request&#39;s writes of transactions, accounts, counterparties and labels are recorded into that set. If the set was opened with mode&#x3D;propose, every write of the request is rolled back and the response is 200 with data &#x3D; the ChangeSet (items with before/after) instead of the endpoint&#39;s usual body; requests to a proposed set are each evaluated against the committed book, so send dependent operations in one request (e.g. one /api/transaction/mutate call). Without this header the server records the writes into an implicit set. | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project deleted successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> GetProjectsResponse get_project(workspace_id, id=id)

Get project

Retrieves project details for a specific workspace with optional filtering by project ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_projects_response import GetProjectsResponse
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
    api_instance = orbuculum_client.ProjectApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 1 # int | Project ID (optional, to get a specific project) (optional)

    try:
        # Get project
        api_response = api_instance.get_project(workspace_id, id=id)
        print("The response of ProjectApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Project ID (optional, to get a specific project) | [optional] 

### Return type

[**GetProjectsResponse**](GetProjectsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project details retrieved successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> UpdateProjectResponse update_project(update_project_request, x_orbuculum_change_set=x_orbuculum_change_set)

Update project

Updates an existing project with a new name, colour or icon

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_project_request import UpdateProjectRequest
from orbuculum_client.models.update_project_response import UpdateProjectResponse
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
    api_instance = orbuculum_client.ProjectApi(api_client)
    update_project_request = orbuculum_client.UpdateProjectRequest() # UpdateProjectRequest | 
    x_orbuculum_change_set = 56 # int | Id of an explicit change set opened with POST /api/change-set/open. The request's writes of transactions, accounts, counterparties and labels are recorded into that set. If the set was opened with mode=propose, every write of the request is rolled back and the response is 200 with data = the ChangeSet (items with before/after) instead of the endpoint's usual body; requests to a proposed set are each evaluated against the committed book, so send dependent operations in one request (e.g. one /api/transaction/mutate call). Without this header the server records the writes into an implicit set. (optional)

    try:
        # Update project
        api_response = api_instance.update_project(update_project_request, x_orbuculum_change_set=x_orbuculum_change_set)
        print("The response of ProjectApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | 
 **x_orbuculum_change_set** | **int**| Id of an explicit change set opened with POST /api/change-set/open. The request&#39;s writes of transactions, accounts, counterparties and labels are recorded into that set. If the set was opened with mode&#x3D;propose, every write of the request is rolled back and the response is 200 with data &#x3D; the ChangeSet (items with before/after) instead of the endpoint&#39;s usual body; requests to a proposed set are each evaluated against the committed book, so send dependent operations in one request (e.g. one /api/transaction/mutate call). Without this header the server records the writes into an implicit set. | [optional] 

### Return type

[**UpdateProjectResponse**](UpdateProjectResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project updated successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Resource not found |  -  |
**409** | Conflict - project name already exists |  -  |
**422** | Validation failed - unknown or non-writable icon/colour name |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

