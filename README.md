API Overview
=================
This API let users to perform fake news prediction and contribution in indonesian language

API Documentation
=================

  * [Login](#login)
  * [Register](#register)
  * [Predict Claim 🔒](#predict-claim)
  * [Search Claim 🔒](#search-claim)

# Login
  
| ENDPOINT | METHOD | DESCRIPTION |
| --- | --- | --- |
|https://true-sight-ip6whebjsa-uc.a.run.app/api/|POST|Auth|

<details>
  <summary>Login Body</summary>
  
```json
{
    "type": "login",
    "username": "required",
    "password": "required"
}
```
</details>

# Register
  
| ENDPOINT | METHOD | DESCRIPTION |
| --- | --- | --- |
|https://true-sight-ip6whebjsa-uc.a.run.app/api/|POST|Reg|

<details>
  <summary>Register Body</summary>
  
```json
{
    "type": "registration",
    "username": "required",
    "email": "required",
    "password": "required"
}
```
</details>

# Predict Claim
🔒
| ENDPOINT | METHOD | DESCRIPTION |
| --- | --- | --- |
|https://true-sight-ip6whebjsa-uc.a.run.app/api/|POST|Predict claim|
<details>
  <summary>Predict Header, Body, Response</summary>

Predict Header
```
Content-Type: application/json
Authorization: Bearer <token>
```
Predict Body
```json
{
    "type": "predict",
    "content": "test",
}
```
Predict Expected Response
```json
{
    "fact": "0.9999",
    "user_id": "test",
}
```
</details>
 
 # Search Claim
🔒
| ENDPOINT | METHOD | DESCRIPTION |
| --- | --- | --- |
|https://true-sight-ip6whebjsa-uc.a.run.app/api/|POST|Search claim|
<details>
  <summary>Search Header, Body, Response</summary>

Search Header
```
Content-Type: application/json
Authorization: Bearer <token>
```
Search Body
```json
{
    "type": "search",
    "keyword": "title",
}
```
Search Claim Expected Response
```json
{
    "result": "title",
    "content": "description",
}
```
</details>
 
