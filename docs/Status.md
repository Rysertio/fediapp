# Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID of the status in the database. Cast from integer but not guaranteed to be a number. | 
**uri** | **object** | URI of the status used for federation. | 
**created_at** | **object** | The date when this status was created (ISO 8601 DateTime). | 
**account** | [**Account**](Account.md) |  | 
**content** | **object** | HTML-encoded status content. | 
**visibility** | **object** | Visibility of this status. - &#x60;public&#x60; &#x3D; Visible to everyone, shown in public timelines. - &#x60;unlisted&#x60; &#x3D; Visible to public, but not included in public timelines. - &#x60;private&#x60; &#x3D; Visible to followers only, and to any mentioned users. - &#x60;direct&#x60; &#x3D; Visible only to mentioned users. | 
**sensitive** | **object** | Is the status marked as sensitive content? | 
**spoiler_text** | **object** | Subject or summary line, below which status content is collapsed until expanded. | 
**media_attachements** | **object** | Media that is attached to this status. | 
**application** | [**Application**](Application.md) |  | 
**url** | **object** | A link to the status&#x27;s HTML representation. | [optional] 
**in_reply_to_id** | **object** | ID of the status being replied. Cast from an integer but not guaranteed to be a number. | [optional] 
**in_reply_to_account_id** | **object** | ID of the account being replied to. Cast from integer but not guaranteed to be a number. | [optional] 
**reblog** | [**Status**](Status.md) |  | [optional] 
**poll** | [**Poll**](Poll.md) |  | [optional] 
**card** | [**Card**](Card.md) |  | [optional] 
**language** | **object** | Primary langauge of this status. ISO 639 Part 1 two-letter langauge code. | [optional] 
**text** | **object** | Plain-text source of a status. Returned instead of &#x60;content&#x60; when status is deleted, so the user may redraft from the source text without the client having to reverse-engineer the original text from the HTML content. | [optional] 
**mentions** | **object** | Mentions of users within the status content. | 
**tags** | **object** | Hashtags used within the status content. | 
**emojis** | **object** | Custom emoji to be used while rendering status content. | 
**reblogs_count** | **object** | How many boosts this status has received. | 
**favourites_count** | **object** | How many favourites this status has received. | 
**replies_count** | **object** | How many replies this status has received. | 
**favourited** | **object** | Have you favourited this status? | [optional] 
**reblogged** | **object** | Have you boosted this status? | [optional] 
**muted** | **object** | Have you muted notifications for this status&#x27;s conversation? | [optional] 
**bookmarked** | **object** | Have you bookmarked this status? | [optional] 
**pinned** | **object** | Have you pinned this status? Only appears if the status is pinnable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

