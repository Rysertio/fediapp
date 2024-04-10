# swagger_client.ListsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_accounts_id_lists**](ListsApi.md#get_api_v1_accounts_id_lists) | **GET** /api/v1/accounts/{id}/lists | Lists containing this account

# **get_api_v1_accounts_id_lists**
> object get_api_v1_accounts_id_lists(id)

Lists containing this account

User lists that you have added this account to.

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
api_instance = swagger_client.ListsApi(swagger_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Lists containing this account
    api_response = api_instance.get_api_v1_accounts_id_lists(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->get_api_v1_accounts_id_lists: %s\n" % e)
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

