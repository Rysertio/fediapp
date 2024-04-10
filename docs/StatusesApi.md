# swagger_client.StatusesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_accounts_id_statuses**](StatusesApi.md#get_api_v1_accounts_id_statuses) | **GET** /api/v1/accounts/{id}/statuses | Statuses for user

# **get_api_v1_accounts_id_statuses**
> object get_api_v1_accounts_id_statuses(id)

Statuses for user

Statuses posted to the given account.  Public for public statuses only, or user_token + read:statuses (for private statuses the user is authorized to see).

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
api_instance = swagger_client.StatusesApi(swagger_client.ApiClient(configuration))
id = NULL # object | The id of the account in the database.

try:
    # Statuses for user
    api_response = api_instance.get_api_v1_accounts_id_statuses(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->get_api_v1_accounts_id_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| The id of the account in the database. | 

### Return type

**object**

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

