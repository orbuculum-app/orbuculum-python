# orbuculum_client.OpenQuestionApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_open_question**](OpenQuestionApi.md#close_open_question) | **POST** /api/open-question/close | Close an open question with a note
[**create_open_question**](OpenQuestionApi.md#create_open_question) | **POST** /api/open-question/create | Create an open question
[**list_open_questions**](OpenQuestionApi.md#list_open_questions) | **GET** /api/open-question/list | List open questions


# **close_open_question**
> CloseOpenQuestion200Response close_open_question(close_open_question_request)

Close an open question with a note

Sets the question to `closed` with the note. For each linked transaction, needs_review is cleared when no other open question links it and the mark was not set by hand; closing never sets the mark. Needs edit permission on every linked transaction; otherwise the question stays open.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.close_open_question200_response import CloseOpenQuestion200Response
from orbuculum_client.models.close_open_question_request import CloseOpenQuestionRequest
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
    api_instance = orbuculum_client.OpenQuestionApi(api_client)
    close_open_question_request = orbuculum_client.CloseOpenQuestionRequest() # CloseOpenQuestionRequest | 

    try:
        # Close an open question with a note
        api_response = api_instance.close_open_question(close_open_question_request)
        print("The response of OpenQuestionApi->close_open_question:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenQuestionApi->close_open_question: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_open_question_request** | [**CloseOpenQuestionRequest**](CloseOpenQuestionRequest.md)|  | 

### Return type

[**CloseOpenQuestion200Response**](CloseOpenQuestion200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The closed question |  -  |
**400** | Malformed JSON; id not a positive integer; note missing, not a string or blank |  -  |
**401** | Unauthorized |  -  |
**403** | No access to this workspace, or no permission to edit a linked transaction; the question stays open |  -  |
**404** | Question not found |  -  |
**405** | Method not allowed |  -  |
**409** | Question is already closed |  -  |
**500** | Internal server error; the question stays open |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_open_question**
> CreateOpenQuestion201Response create_open_question(create_open_question_request)

Create an open question

Creates a question with status `open`, optionally linked to transactions. Every linked transaction gets needs_review = true; a transaction already marked by hand keeps that. Linking needs edit permission on every linked transaction; otherwise nothing is written.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_open_question201_response import CreateOpenQuestion201Response
from orbuculum_client.models.create_open_question_request import CreateOpenQuestionRequest
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
    api_instance = orbuculum_client.OpenQuestionApi(api_client)
    create_open_question_request = orbuculum_client.CreateOpenQuestionRequest() # CreateOpenQuestionRequest | 

    try:
        # Create an open question
        api_response = api_instance.create_open_question(create_open_question_request)
        print("The response of OpenQuestionApi->create_open_question:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenQuestionApi->create_open_question: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_open_question_request** | [**CreateOpenQuestionRequest**](CreateOpenQuestionRequest.md)|  | 

### Return type

[**CreateOpenQuestion201Response**](CreateOpenQuestion201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created question |  -  |
**400** | Malformed JSON; text missing, not a string or blank; transaction_ids not a list of positive integers |  -  |
**401** | Unauthorized |  -  |
**403** | No access to this workspace, or no permission to edit a linked transaction; nothing is written |  -  |
**404** | A linked transaction was not found; nothing is written |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error; nothing is written |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_open_questions**
> ListOpenQuestions200Response list_open_questions(workspace_id, status=status, transaction_id=transaction_id, page=page, per_page=per_page)

List open questions

Questions of the workspace, newest first (created_at, then id, descending), paginated. A question linked to a transaction the caller's role cannot view is not listed; unlinked questions are listed to every workspace member. A transaction_id that matches no transaction, or one the role cannot view, gives an empty list.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.list_open_questions200_response import ListOpenQuestions200Response
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
    api_instance = orbuculum_client.OpenQuestionApi(api_client)
    workspace_id = 7 # int | Workspace ID
    status = 'open' # str | Only questions with this status; omit or empty for all (optional)
    transaction_id = 101 # int | Only questions linked to this transaction (optional)
    page = 1 # int | Page number, from 1; a smaller value is read as 1 (optional) (default to 1)
    per_page = 20 # int | Items per page; clamped to 1..100 (optional) (default to 20)

    try:
        # List open questions
        api_response = api_instance.list_open_questions(workspace_id, status=status, transaction_id=transaction_id, page=page, per_page=per_page)
        print("The response of OpenQuestionApi->list_open_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenQuestionApi->list_open_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **status** | **str**| Only questions with this status; omit or empty for all | [optional] 
 **transaction_id** | **int**| Only questions linked to this transaction | [optional] 
 **page** | **int**| Page number, from 1; a smaller value is read as 1 | [optional] [default to 1]
 **per_page** | **int**| Items per page; clamped to 1..100 | [optional] [default to 20]

### Return type

[**ListOpenQuestions200Response**](ListOpenQuestions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page of questions |  -  |
**400** | workspace_id missing, status not open/closed, or transaction_id not a positive integer |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no access to this workspace |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

