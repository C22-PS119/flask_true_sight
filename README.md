Table Of Contents
=================

- [API](#api)
  - [Auth API](#auth-api)
  - [Register API](#register-api)
  - [Search API](#search-api)
  - [Predict API](#predict-api)
  - [Get Profile Details](#get-profile-details)
  - [Get Claim Details](#get-claim-details)
  - [Set Own Profile](#set-own-profile)
  - [Set Claim Details](#set-claim-details)
  - [Create New Claim](#create-new-claim)
- [Page Links](#page-links)
  - [Claim Resources](#claim-resources)
  - [User Avatar](#user-avatar)

# Api

## Auth API

### Usage

- URL: `/api/auth/`
- Content-Type: `application/json` or `application/x-www-form-urlencoded` or `multipart/form-data`
- Fields:
  - username > Username
  - password > User password

### Response

**_Api Key_** as String

### Description

User login to get **_Api Key_**.

## Register API

### Usage

- URL: `/api/registration/`
- Content-Type: `application/json` or `application/x-www-form-urlencoded` or `multipart/form-data`
- Fields:
  - username > Username
  - email > User email
  - full_name > Full name [Optional]
  - password > User password

### Response

Response status

### Description

Register new user

## Search API

### Usage

- URL: `/api/search/`
- Content-Type: `application/json` or `application/x-www-form-urlencoded` or `multipart/form-data`
- x-api-key: <USER_API_KEY>
- Fields:
  - keyword > "Text to search"
  - begin > Start index [Optional]
  - limit > Maximum Result [Optional]

### Response

Array of dictionary search result:

```json
{ 
  "attachment",
  "author_id",
  "comment_id",
  "date_created",
  "description",
  "downvote",
  "fake",
  "id",
  "num_click",
  "title",
  "upvote",
  "url",
  "verified_by"
  }
  ```

### Description

Search claims with given keywords.

## Predict API

### Usage

- URL: `/api/predict/`
- Content-Type: `application/json` or `application/x-www-form-urlencoded` or `multipart/form-data`
- x-api-key: <USER_API_KEY>
- Fields:
  - title > Title of claim
  - content > Content of claim

### Response

Dictionary of claim prediction

```json
{
  "claim",
  "prediction",
  "val_prediction"
}
```

### Description

Predict claim fake or fact

## Get Profile Details

### Usage

- URL: `/api/get/profile/`
- Content-Type: `application/json` or `application/x-www-form-urlencoded` or `multipart/form-data`
- x-api-key: <USER_API_KEY>
- Fields:
  - id > Target User ID to Query

### Response

Dictionary of User Details

```json
{
  "id",
  "username",
  "full_name",
  "email",
  "bookmarks",
  "date_created",
  "verified",
  "votes"
}
```

### Description

Get user details by ID

## Get Claim Details

### Usage

- URL: `/api/get/claim/`
- Content-Type: `application/json` or `application/x-www-form-urlencoded` or `multipart/form-data`
- x-api-key: <USER_API_KEY>
- Fields:
  - id > Target Claim ID to Query

### Response

Dictionary of User Details

```json
{
  "id",
  "title",
  "description",
  "fake",
  "author_id",
  "date_created",
  "attachment",
  "url",
  "upvote",
  "downvote",
  "num_click",
  "verified_by",
  "comment_id"
}
```
**Error**:
> _NOT ACCEPTABLE_

### Description

Get claim details by ID

## Set Own Profile

### Usage

- URL: `/api/set/profile/`
- Content-Type: `multipart/form-data`
- x-api-key: <USER_API_KEY>
- Maximum File Size Allowed: `5 MiB`
- Allowed Upload Extensions: `JPG` `JPEG` `PNG` `BMP` 
- Changeable Fields:
  - email > Change email [Optional]
  - full_name > Change Full name [Optional]
  - avatar > Change Profile Picture (Upload File) [Optional]

### Response

**Error**:
> _Extension not allowed_, _File already exists_, _File size is too big_

### Description

Set Own Profile Attributes

## Set Claim Details

### Usage

- URL: `/api/set/claim/`
- Content-Type: `multipart/form-data`
- x-api-key: <USER_API_KEY>
- Maximum File Size Allowed: `5 MiB`
- Allowed Upload Extensions: `JPG` `JPEG` `PNG` `BMP` 
- Changeable Fields:
  - title > Change claim title [Optional]
  - description > Change claim description [Optional]
  - fake > Change status Fake or Fact (**as integer**) [Optional]
  - url > Change url
  - [...attachment_files...] > Change attachment files (just upload file with random field) [Optional]

### Response

**Error**:
> _Extension not allowed_, _File already exists_, _File size is too big_

### Description

Set claim details

## Create new Claim

### Usage

- URL: `/api/create/claim/`
- Content-Type: `multipart/form-data`
- x-api-key: <USER_API_KEY>
- Maximum File Size Allowed: `5 MiB`
- Allowed Upload Extensions: `JPG` `JPEG` `PNG` `BMP` 
- Fields:
  - title > Change claim title
  - description > Change claim description
  - fake > Change status Fake or Fact (**as integer**)
  - url > Change url
  - [...attachment_files...] > Change attachment files (just upload file with random field) [Optional]

### Response

**Error**:
> _Extension not allowed_, _File already exists_, _File size is too big_

### Description

Create new Claim

# Page Links

## Claim Resources

- URL: `/uploads/claim/<claim_id>/<resources_path>`
- Content-Type: **None**

# Page Links

## User Avatar

- URL: `/uploads/avatar/<user_id>`
- Content-Type: **None**
- x-api-key: <User_API_Key>
