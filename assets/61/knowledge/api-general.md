# [Deepgram API Overview](https://developers.deepgram.com/reference/deepgram-api-overview)

The Deepgram API is a [RESTful](https://en.wikipedia.org/wiki/REST) API that allows you to interact with Deepgram programmatically. You can use our API to:

- Transcribe[ pre-recorded ](https://developers.deepgram.com/reference/pre-recorded)and [streaming](https://developers.deepgram.com/reference/streaming) audio.
- Transform [text to speech](https://developers.deepgram.com/reference/text-to-speech-api).
- Analyze [text](https://developers.deepgram.com/reference/analyze-text).
- Administer your Deepgram account:
  - Manage [projects](https://developers.deepgram.com/reference/get-projects) and project [members](https://developers.deepgram.com/reference/get-members)
  - Manage project [invitations](https://developers.deepgram.com/reference/list-invites)
  - Manage user[ scopes](https://developers.deepgram.com/reference/get-member-scopes)
  - Obtain billing [balances](https://developers.deepgram.com/reference/get-all-balances)
  - Obtain usage [summaries](https://developers.deepgram.com/reference/get-all-requests)
  - Manage [API keys](https://developers.deepgram.com/reference/list-keys)
  - Manage [On-Prem credentials](https://developers.deepgram.com/reference/list-credentials)

> ℹ To create your first API key refer to our Guide [Creating API Keys](https://developers.deepgram.com/docs/create-additional-api-keys).

Updated 9 days ago



# [Authentication](https://developers.deepgram.com/reference/authentication)

Authenticating requests made to the Deepgram API

Send requests to the API with an `Authorization` header that references your project's API Key:

```
Authorization: Token <YOUR_DEEPGRAM_API_KEY>
```

You can [create a Deepgram API Key in the Deepgram Console](https://console.deepgram.com/signup?utm_source=api-ref). You must create your first API Key using the Console.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests made without authentication will also fail.

|                            |               |
| :------------------------- | :------------ |
| **Security Scheme Type**   | API Key       |
| **Header parameter name:** | Authorization |

Updated 3 months ago



# [Errors](https://developers.deepgram.com/reference/errors)

Errors you might encounter when making requests to the Deepgram API

A record of errors and reasons you'll get them when using the Deepgram API.

## General API errors

Errors that could be returned on any endpoint.

### `400` Invalid JSON submitted

When making a `POST` request with JSON data, you must include all required fields. If required filed are missing, or the submitted JSON is invalid, a `400 Bad Request` will be returned. The response will be similar to the below, depending on the endpoint and how the JSON is malformed.

```json
{
  "category": "INVALID_JSON",
  "message": "Invalid JSON submitted.",
  "details": "Json deserialize error: missing field `xxx` at line 7 column 1",
  "request_id": "uuid"
}
---
{
  "err_code": "Bad Request",
  "err_msg": "Content-type was application/json, but we could not process the JSON payload.",
  "request_id": "uuid"
}
---
{
  "category": "INVALID_JSON",
  "message": "Invalid JSON submitted.",
  "details": "Json deserialize error: expected `:` at line 3 column 13",
  "request_id": "uuid"
}
```

### `400` Unknown request body format

If you receive the following error:

```json
{
  "err_code": "Bad Request",
  "err_msg": "Bad Request: failed to process audio: corrupt or unsupported data",
  "request_id": "uuid"
}
```

Often, this is caused by sending Deepgram a URL to transcribe, but failing to set a `Content-Type: application/json` header. When sending Deepgram a JSON payload containing a URL, the `Content-Type: application/json` must be set in the request.

If you are sending an audio file and not a URL, you may be sending corrupted audio. You can use tools such as `ffprobe` or Audacity to confirm that your audio file is valid.

### `401` Incorrect API key

Providing an invalid API key will return `401 Unauthorized` with the following error.

```json
{
  "err_code": "INVALID_AUTH",
  "err_msg": "Invalid credentials.",
  "request_id": "uuid"
}
```

### `401` Insufficient permissions

Making a request that you do not have sufficient permissions for will return `401 Unauthorized` with this error.

```json
{
 "err_code":"INSUFFICIENT_PERMISSIONS",
 "err_msg":"User does not have sufficient permissions.",
 "request_id":"uuid"
}
```

### `403` Insufficient permissions

Making a request for a model that you do not have access to will return `403 Forbidden` with this error.

```json
{
 "err_code":"INSUFFICIENT_PERMISSIONS",
 "err_msg":"Project does not have access to the requested model.",
 "request_id":"uuid"
}
```

### `404` UUID parsing failed

Providing an invalid Project ID will fail parsing and return `404 Not Found` and this response.

```text
UUID parsing failed: invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-zA-Z], found `p` at 1
```

### `404` Project not found

When a project isn't found it will result in `404 Not Found`. It may be because;

- the Project ID is incorrect
- the Project ID is for a project that has been deleted
- the Project ID is not associated with the API key used to make the request

```json
{
  "err_code": "PROJECT_NOT_FOUND",
  "err_msg": "Project not found."
}
```

## Transcription errors

Errors specific to making transcription requests.

### `402` Insufficient credits

When attempting to transcribe a file, you may not have sufficient funds to complete the request. This will result in a `402 Payment Required` error with this error.

```json
{
  "err_code": "ASR_PAYMENT_REQUIRED",
  "err_msg": "Project does not have enough credits for an ASR request and does not have an overage agreement.",
  "request_id": "uuid"
}
```

### `429` Rate limit exceeded

When requests are made in excess of Deepgram's [rate limits](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio#rate-limits), a `429 Too Many Requests` is returned with the following error. An exponential-backoff retry strategy is recommended to accommodate rate-limiting when submitting a large volume of concurrent requests.

```json
{
  "err_code": "TOO_MANY_REQUESTS",
  "err_msg": "Too many requests. Please try again later",
  "request_id": "uuid"
}
```

## Handling HTTP Errors

### Production

Some error codes, such as `400: Bad Request` errors, can be prevented in your production code by careful testing and development. However, others, such as `503: Service Unavailable`, can occur regardless of your implementation.

Below is a list of HTTP error codes that your production code should handle gracefully. Some of these errors may succeed if retried, while others (such as `414: URI Too Long`) need to be handled by modifying the request.

- **408 Request Timeout**: The server timed out waiting for the request.
- **411 Length Required**: The server refuses to accept the request without a defined Content-Length.
- **413 Request Entity Too Large**: The request is larger than the server is willing or able to process.
- **414 URI Too Long**: The server is refusing to service the request because the request-target is longer than the server is willing to interpret.
- **429 Too Many Requests**: The user has sent too many requests in a given amount of time.
- **499 Client Closed Request**: A non-standard status code indicating that the client closed the connection.
- **500 Internal Server Error**: A generic error message indicating that the server has encountered a situation it doesn't know how to handle.
- **502 Bad Gateway**: The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed in attempting to fulfill the request.
- **503 Service Unavailable**: The server is not ready to handle the request. Common causes include a server that is down for maintenance or is overloaded.
- **504 Gateway Timeout**: The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server or some other auxiliary server it needed to access in order to complete the request.

### Development

The following errors are more likely to be encountered in a development environment. You may want to add error handling in your production code to gracefully handle these error codes as well.

- **400 Bad Request**: The server could not understand the request due to invalid syntax.
- **401 Insufficient permissions**: The project does not have permissions to access the requested features or model.
- **401 Unauthorized**: The API key is invalid or unauthorized.
- **402 Payment Required**: The project has insufficient funds to complete the request.
- **403 Forbidden**: The server understood the request but refuses to authorize it.
- **404 Not Found**: The specified entity ID could not be found.

Updated 3 months ago

