# AdminAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The ID of the account in the database. Cast from an integer, but not guaranteed to be a number. | 
**username** | **object** | The username of the account. | 
**domain** | **object** | The domain of the account. | 
**created_at** | **object** | When the account was first discovered | 
**email** | **object** | The email address associated with the account. | 
**ip** | **object** | The IP address last used to login to this account. | 
**locale** | **object** | The locale of the account. ISO 639 Part 1 two-letter language code. | 
**invite_request** | **object** | Invite request text ??? | 
**role** | **object** | The current role of the account. | 
**confirmed** | **object** | Whether the account has confirmed their email address. | 
**approved** | **object** | Whether the account is currently approved. | 
**disabled** | **object** | Whether the account is currently disabled. | 
**silenced** | **object** | Whether the account is currently silenced. | 
**suspended** | **object** | Whether the account is currently suspended. | 
**account** | [**Account**](Account.md) |  | 
**created_by_application_id** | **object** | The ID of the application that created this account. Cast from an integer, but not guaranteed to be a number. | [optional] 
**invited_by_account_id** | **object** | The ID of the account that invited this user. Cast from an integer, but not guaranteed to be a number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

