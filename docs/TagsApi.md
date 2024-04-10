# swagger_client.TagsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_accounts_id_featured_tags**](TagsApi.md#get_api_v1_accounts_id_featured_tags) | **GET** /api/v1/accounts/{id}/featured_tags | Featured tags

# **get_api_v1_accounts_id_featured_tags**
> object get_api_v1_accounts_id_featured_tags(id)

Featured tags

Tags featured by this account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: user-token-auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Featured tags
    api_response = api_instance.get_api_v1_accounts_id_featured_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_api_v1_accounts_id_featured_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

