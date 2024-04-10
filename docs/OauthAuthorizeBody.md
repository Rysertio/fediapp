# OauthAuthorizeBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **object** | Should be equal to &#x60;code&#x60;. | 
**client_id** | **object** | Client ID, obtained during app registration. | 
**redirect_uri** | **object** | Set a URI to redirect the user to. If this parameter is set to &#x60;urn:ietf:wg:oauth:2.0:oob&#x60; then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration. | 
**scope** | **object** | List of requested OAuth scopes, separated by spaces. Must be a subset of scopes declared during app registration. If not provided, defaults to &#x60;read&#x60;. | [optional] 
**force_login** | **object** | Added in &#x60;2.6.0&#x60;. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

