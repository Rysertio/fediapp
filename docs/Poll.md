# Poll

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The ID of the poll in the database. Cast from an integer but not guaranteed to be a number. | 
**expires_at** | **object** | When the poll ends. ISO8601 DateTime or null if the poll does not end. | [optional] 
**expired** | **object** | Is the poll currently expired? | 
**multiple** | **object** | Does the poll allow multiple-choice answers? | 
**votes_count** | **object** | How many votes have been recieved. | 
**voters_count** | **object** | How many unique accounts have voted on a multiple choice poll. Null if &#x60;multiple&#x60; is false. | [optional] 
**voted** | **object** | When called with a user token, has the authorized user voted? | [optional] 
**own_votes** | **object** | When called with a user token, which options has the authorized user chosen? Contains an array of index values for &#x60;options&#x60;. | [optional] 
**options** | **object** | Possible answers for the poll. | 
**emojis** | **object** | Custom emoji to be used for rendering poll options. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

