# Speech to Text - Results Processing



# [STT Callback](https://developers.deepgram.com/docs/callback)

Speech-to-Text Callback allows you to have your submitted audio processed asynchronously.

---

`callback` *string*

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

Deepgram’s Callback feature allows you to supply a callback URL to which transcriptions can be returned. When passed, Deepgram will immediately respond with a `request_id` before processing your audio asynchronously.

## Enable Feature

To enable Callback, when you call Deepgram’s API, add a `callback` parameter in the query string and set it to the URL to which you would like transcriptions sent:

```
callback=URL
```

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?callback=URL'
```

## URL Structure

An example URL is `https://example.com/callback`.

Your callback URLs may reference the following protocols:

- For pre-recorded audio: `http` or `https`
- For streaming audio, `http`, `https`, `ws`, or `wss:`

## Authenticating Callback Requests

Authentication ensures the security and integrity of callback requests. There are two main methods for authenticating callback requests: using Basic Auth and utilizing the dg-token request header.

### Using Basic Auth

You may embed username-password authentication credentials in the callback URL in the format `https://username:password@host.example.com`. However, it's important to note that only ports 80, 443, 8080, and 8443 are permitted for callbacks.

> ⚠ Only ports 80, 443, 8080, and 8443 are permitted for callbacks.

### Using the `dg-token` Request Header

Alternatively, the callback request itself contains a header named dg-token. This header is automatically set to the API Key Identifier associated with the API Key used to submit the original request. This method provides a secure and straightforward means of authentication.

## Results

Depending on the type of submitted audio, the response will vary.

### Pre-recorded Audio

When Deepgram has finished analyzing the audio, it will send a `POST` request to the provided callback URL with an appropriate HTTP status code.

If the HTTP status code of the response to the callback `POST` request is unsuccessful (not 200-299), Deepgram will retry the callback up to 10 times with a 30 second delay between attempts.

If you would like Deepgram to make a `PUT` request rather than a `POST` request to your callback URL, you can add the `callback_method=put` query parameter in addition to `callback=URL`. Refer to the [Using AWS S3 Presigned URLs with the Deepgram API](https://developers.deepgram.com/docs/using-aws-s3-presigned-urls-with-the-deepgram-api#uploading-transcripts-directly-to-s3) guide for more information.

### Streaming Audio

As Deepgram analyzes the audio, the way in which it sends requests back to the provided callback URL varies:

- If your callback URL begins with `http://` or `https://`, then Deepgram will send `POST` requests to the callback server for each streaming response.
- If your callback URL begins with `ws://` or `wss://`, then Deepgram will establish a WebSocket connection with the callback server and send WebSocket text messages that contain the streaming responses.

> ⚠ If a WebSocket callback connection is disconnected at any point, the entire real-time transcription stream is killed; this maintains the strong guarantee of a one-to-one relationship between incoming real-time connections and outgoing WebSocket callback connections.

## Use Cases

Some examples of use cases for Callback include:

- Customers with large amounts of audio that may be slow to process.
- Customers who don't require immediate results.

Updated 15 days ago



# Tagging

Tagging allows you to label your requests for the purpose of identification during usage reporting.

[Suggest Edits](https://developers.deepgram.com/edit/tagging)

`tag` *string*.

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

Deepgram’s Tagging feature allows you to label your API requests for the purpose of identification during usage reporting. You can also apply tags to API Keys; if you do, any tags applied to the API Key running the API request will also be applied to the request itself.

Tags are limited to 128 characters per tag.

## Enable Feature

To enable Tagging, when you call Deepgram’s API, add a `tag` parameter in the query string and set it to the tag you would like to recognize:

```
tag=VALUE
```

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client. Please be aware that once you have set a tag, you cannot modify it.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?tag=VALUE'
```

> ⚠ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Filter Requests by Tag

Once applied, you can identify tags associated with API requests returned by the [Get All Requests](https://developers.deepgram.com/reference/get-all-requests), [Get Request](https://developers.deepgram.com/reference/get-request), and [Get Fields](https://developers.deepgram.com/reference/get-fields) endpoints.

You can also directly query requests by tag at the [Summarize Usage](https://developers.deepgram.com/reference/summarize-usage) endpoint.

```shell
curl \
  --request GET \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'content-type: application/json'
  --url 'https://api.deepgram.com/v1/projects/PROJECT_ID/usage?tag=VALUE'
```

> ⚠ Replace the placeholder `PROJECT_ID` with your Deepgram Console Project ID, `VALUE` with your tag, and `YOUR_DEEPGRAM_API_KEY` with your Deepgram API Key.

## Special Considerations

### White Space or Special Characters

If your tag or extra metadata includes spaces or special characters, be sure to URL encode it:

```
tag=marketing%20team` or `tag=marketing+team
```

### Apply Multiple Instances

To apply multiple tags or multiple extra key-value pairs, submit the query parameter multiple times in your API request:

```
tag=marketing&tag=legal
```

## Comparison to Extra Metadata

[Extra Metadata](https://developers.deepgram.com/docs/extra-metadata) is a similar feature to Tagging. Where Tagging is primarily intended for tracking and filtering usage, Extra Metadata is useful for passing data to downstream processing steps.

Below is a comparison table summarizing the main differences between the two features:

|                                                           | Tagging   | Extra Metadata |
| :-------------------------------------------------------- | :-------- | :------------- |
| Primarily for passing data to downstream processing steps | ❌         | ✅              |
| Primarily for tracking usage                              | ✅         | ❌              |
| Configurable per request                                  | ✅         | ✅              |
| Configurable per API key                                  | ✅         | ❌              |
| Character limit per value                                 | 128 chars | 2048 chars     |
| Can be used to filter usage                               | ✅         | ❌              |
| Can specify a key in a key-value pair                     | ❌         | ✅              |
| Can specify a value in a key-value pair                   | ✅         | ✅              |

## Use Cases

Some examples of use cases for Tagging include:

- Customers who have multiple, related business projects and need to track separate usage.
- Customers who have projects managed by different business teams or under different cost centers.
- Customers who operate a business-to-business (B2B) model that focuses on selling products and services to other companies. Rather than creating separate projects to track usage data, you can create a separate API Key for each company and tag it with the their information. Any requests run using the API Key will also be tagged with that company's information.

Updated 3 months ago



# [Extra Metadata](https://developers.deepgram.com/docs/extra-metadata)

Extra Metadata allows you to label your requests for the purpose of identification in downstream processing.

---

`extra` *string*.

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

Deepgram’s Extra Metadata feature allows you to attach arbitrary key-value pairs to your API requests that are attached to the API response for usage in downstream processing.

Extra metadata is limited to 2048 characters per key-value pair.

## Enable Feature

To enable Extra Metadata, when you call Deepgram’s API, add an `extra` parameter in the query string and pass a key-value pair you would like to include in the response.

```
extra=KEY:VALUE
```

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```sh
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?extra=KEY:VALUE'
```

> ⚠ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://developers.deepgram.com/docs/🔗).

## Response

If you included `extra=myKey:someValue` in your request, the key-value pair would be passed through to the response in the following format:

```json
{
  "metadata": {
    "extra": {
      "myKey": "someValue"
    }
    ...
  }
  ...
}
```

## Special Considerations

### White Space or Special Characters

If your extra metadata includes spaces or special characters, be sure to URL encode it:

```
extra=dataflow:marketing%20team` or `extra=dataflow:marketing+team
```

### Apply Multiple Instances

To apply multiple extra key-value pairs, submit the query parameter multiple times in your API request:

```
extra=team:marketing&extra=purpose:legal
```

> ## ⚠ Duplicate Keys
>
> If you request contains multiple instances of `extra` with the same key, the corresponding values will *not* be merged. Instead, the last value will overwrite any previous values.
>
> For example, `extra=team:marketing&extra=team:gtm` will return `"extra": { "team": "gtm" }` in the response.

## Comparison to Tagging

[Tagging](https://developers.deepgram.com/docs/tagging) is a similar feature to Extra Metadata. Where Extra Metadata is primarily intended for passing data to downstream processing steps, Tagging is useful for tracking and filtering usage.

Below is a comparison table summarizing the main differences between the two features:

|                                                           | Extra Metadata | Tagging   |
| :-------------------------------------------------------- | :------------- | :-------- |
| Primarily for passing data to downstream processing steps | ✅              | ❌         |
| Primarily for tracking usage                              | ❌              | ✅         |
| Configurable per request                                  | ✅              | ✅         |
| Configurable per API key                                  | ❌              | ✅         |
| Character limit per value                                 | 2048 chars     | 128 chars |
| Can be used to filter usage                               | ❌              | ✅         |
| Can specify a key in a key-value pair                     | ✅              | ❌         |
| Can specify a value in a key-value pair                   | ✅              | ✅         |
|                                                           |                |           |

## Use Cases

Some examples of use cases for Extra Metadata include:

- Customers who have downstream processing steps after Deepgram's API response that need to be aware of specific data values from upstream processing steps.
- Customers who have an internal ID associated with data that is being sent to Deepgram, and need to persist this ID throughout their data pipeline. This may be especially relevant when using message brokers, such as Kafka or RabbitMQ.

Updated 3 months ago

