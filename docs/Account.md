# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The account id &#x60;header&#x60;. Cast from an integer but not guaranteed to be a number. | 
**username** | **object** | The username of the account, **not including the domain**. | 
**acct** | **object** | The webfinger account URI. Equal to &#x60;username&#x60; for local users, or &#x60;username@domain&#x60; for remote users. | 
**url** | **object** | The location of the user&#x27;s profile page (HTTPS URI). | 
**moved** | [**Account**](Account.md) |  | [optional] 
**fields** | [**Field**](Field.md) |  | [optional] 
**bot** | **object** | A presentational flag. Indicates that the account may perform automated actions, may not be monitored, or identifies as a robot. | [optional] 
**suspended** | **object** | An extra entity returned when an account is suspended. | [optional] 
**mute_expires_at** | **object** | When a timed mute will expire, if applicable (ISO 8601 Datetime). | [optional] 
**created_at** | **object** | When the account was created (ISO 8601 Datetime). | 
**last_status_at** | **object** | When the most recent status was posted (ISO 8601 Datetime). | [optional] 
**statuses_count** | **object** | How many statuses are attached to this account. | 
**followers_count** | **object** | The reported followers of this profile. | 
**following_count** | **object** | The reported follows of this profile. | 
**display_name** | **object** | The profile&#x27;s display name. | 
**note** | **object** | The profile&#x27;s bio / description (HTML string). | 
**avatar** | **object** | An image icon that is shown next to statuses and in the profile. | 
**avatar_static** | **object** | A static version of the avatar. Equal to &#x60;avatar&#x60; if its value is a static image; different if &#x60;avatar&#x60; is an animated GIF. | 
**header** | **object** | An image banner that is shown above the profile and in profile cards. | 
**header_static** | **object** | A static version of the header. Equal to &#x60;header&#x60; if its value is a static image; different if &#x60;header&#x60; is an animated GIF. | 
**locked** | **object** | Whether the account manually approves follow requests. | 
**emojis** | **object** | Custom emoji entities to be used when rendering the profile. If none, an empty array will be returned. | 
**discoverable** | **object** | Whether the account has opted into discovery features such as the profile directory. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

