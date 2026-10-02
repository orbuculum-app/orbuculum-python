# orbuculum_client.MatchingApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matching_create_anti_pattern**](MatchingApi.md#matching_create_anti_pattern) | **POST** /api/matching/create-anti-pattern | Create an anti-pattern (negative learning from rejected suggestion)
[**matching_create_example**](MatchingApi.md#matching_create_example) | **POST** /api/matching/create-example | Create a confirmed matching example (learning loop)
[**matching_create_keyword_pattern**](MatchingApi.md#matching_create_keyword_pattern) | **POST** /api/matching/create-keyword-pattern | Create or update a keyword pattern (upsert)
[**matching_list_examples**](MatchingApi.md#matching_list_examples) | **GET** /api/matching/list-examples | List confirmed matching examples for workspace
[**matching_list_keyword_patterns**](MatchingApi.md#matching_list_keyword_patterns) | **GET** /api/matching/list-keyword-patterns | List keyword patterns for workspace
[**matching_suggest**](MatchingApi.md#matching_suggest) | **POST** /api/matching/suggest | Get account matching suggestions for counterparty
[**matching_update_example**](MatchingApi.md#matching_update_example) | **POST** /api/matching/update-example | Update a matching example (confidence, times_matched, is_active)


# **matching_create_anti_pattern**
> MatchingListExamples200Response matching_create_anti_pattern(matching_anti_pattern_create_request)

Create an anti-pattern (negative learning from rejected suggestion)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_anti_pattern_create_request import MatchingAntiPatternCreateRequest
from orbuculum_client.models.matching_list_examples200_response import MatchingListExamples200Response
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    matching_anti_pattern_create_request = orbuculum_client.MatchingAntiPatternCreateRequest() # MatchingAntiPatternCreateRequest | 

    try:
        # Create an anti-pattern (negative learning from rejected suggestion)
        api_response = api_instance.matching_create_anti_pattern(matching_anti_pattern_create_request)
        print("The response of MatchingApi->matching_create_anti_pattern:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_create_anti_pattern: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matching_anti_pattern_create_request** | [**MatchingAntiPatternCreateRequest**](MatchingAntiPatternCreateRequest.md)|  | 

### Return type

[**MatchingListExamples200Response**](MatchingListExamples200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Anti-pattern created |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matching_create_example**
> MatchingListExamples200Response matching_create_example(matching_example_create_request)

Create a confirmed matching example (learning loop)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_example_create_request import MatchingExampleCreateRequest
from orbuculum_client.models.matching_list_examples200_response import MatchingListExamples200Response
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    matching_example_create_request = orbuculum_client.MatchingExampleCreateRequest() # MatchingExampleCreateRequest | 

    try:
        # Create a confirmed matching example (learning loop)
        api_response = api_instance.matching_create_example(matching_example_create_request)
        print("The response of MatchingApi->matching_create_example:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_create_example: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matching_example_create_request** | [**MatchingExampleCreateRequest**](MatchingExampleCreateRequest.md)|  | 

### Return type

[**MatchingListExamples200Response**](MatchingListExamples200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example created |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matching_create_keyword_pattern**
> MatchingListExamples200Response matching_create_keyword_pattern(matching_keyword_pattern_create_request)

Create or update a keyword pattern (upsert)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_keyword_pattern_create_request import MatchingKeywordPatternCreateRequest
from orbuculum_client.models.matching_list_examples200_response import MatchingListExamples200Response
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    matching_keyword_pattern_create_request = orbuculum_client.MatchingKeywordPatternCreateRequest() # MatchingKeywordPatternCreateRequest | 

    try:
        # Create or update a keyword pattern (upsert)
        api_response = api_instance.matching_create_keyword_pattern(matching_keyword_pattern_create_request)
        print("The response of MatchingApi->matching_create_keyword_pattern:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_create_keyword_pattern: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matching_keyword_pattern_create_request** | [**MatchingKeywordPatternCreateRequest**](MatchingKeywordPatternCreateRequest.md)|  | 

### Return type

[**MatchingListExamples200Response**](MatchingListExamples200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keyword pattern created or updated |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matching_list_examples**
> MatchingListExamples200Response matching_list_examples(workspace_id, is_active=is_active, page=page, per_page=per_page)

List confirmed matching examples for workspace

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_list_examples200_response import MatchingListExamples200Response
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    workspace_id = 123 # int | 
    is_active = True # bool |  (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 20 # int |  (optional) (default to 20)

    try:
        # List confirmed matching examples for workspace
        api_response = api_instance.matching_list_examples(workspace_id, is_active=is_active, page=page, per_page=per_page)
        print("The response of MatchingApi->matching_list_examples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_list_examples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **is_active** | **bool**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 20]

### Return type

[**MatchingListExamples200Response**](MatchingListExamples200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of matching examples |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matching_list_keyword_patterns**
> MatchingListExamples200Response matching_list_keyword_patterns(workspace_id, is_active=is_active)

List keyword patterns for workspace

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_list_examples200_response import MatchingListExamples200Response
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    workspace_id = 123 # int | 
    is_active = True # bool |  (optional)

    try:
        # List keyword patterns for workspace
        api_response = api_instance.matching_list_keyword_patterns(workspace_id, is_active=is_active)
        print("The response of MatchingApi->matching_list_keyword_patterns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_list_keyword_patterns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **is_active** | **bool**|  | [optional] 

### Return type

[**MatchingListExamples200Response**](MatchingListExamples200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of keyword patterns |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matching_suggest**
> MatchingSuggest200Response matching_suggest(matching_suggest_request)

Get account matching suggestions for counterparty

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_suggest200_response import MatchingSuggest200Response
from orbuculum_client.models.matching_suggest_request import MatchingSuggestRequest
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    matching_suggest_request = orbuculum_client.MatchingSuggestRequest() # MatchingSuggestRequest | 

    try:
        # Get account matching suggestions for counterparty
        api_response = api_instance.matching_suggest(matching_suggest_request)
        print("The response of MatchingApi->matching_suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_suggest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matching_suggest_request** | [**MatchingSuggestRequest**](MatchingSuggestRequest.md)|  | 

### Return type

[**MatchingSuggest200Response**](MatchingSuggest200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching suggestions returned |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matching_update_example**
> MatchingListExamples200Response matching_update_example(matching_example_update_request)

Update a matching example (confidence, times_matched, is_active)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_example_update_request import MatchingExampleUpdateRequest
from orbuculum_client.models.matching_list_examples200_response import MatchingListExamples200Response
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    matching_example_update_request = orbuculum_client.MatchingExampleUpdateRequest() # MatchingExampleUpdateRequest | 

    try:
        # Update a matching example (confidence, times_matched, is_active)
        api_response = api_instance.matching_update_example(matching_example_update_request)
        print("The response of MatchingApi->matching_update_example:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_update_example: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matching_example_update_request** | [**MatchingExampleUpdateRequest**](MatchingExampleUpdateRequest.md)|  | 

### Return type

[**MatchingListExamples200Response**](MatchingListExamples200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example updated |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

