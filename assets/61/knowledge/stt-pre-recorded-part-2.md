# Speech to Text - Pre-Recorded



# [Feature Overview](https://developers.deepgram.com/docs/stt-pre-recorded-feature-overview)

Below is a list of Deepgram's Speech-to-Text Pre-Recorded features. Please refer to the corresponding documentation for more details.

---

> ℹ To learn how to get up and running with Pre-Recorded Speech-to-Text, read the [Pre-Recorded Speech-to-Text](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) getting started guide.

## Model selection

| Feature                                                      | Language(s)                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Model](https://developers.deepgram.com/docs/model)          | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Language](https://developers.deepgram.com/docs/language)    | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Language Detection](https://developers.deepgram.com/docs/language-detection) | [All not in beta](https://developers.deepgram.com/docs/models-overview) |
| [Version](https://developers.deepgram.com/docs/version)      | [All available](https://developers.deepgram.com/docs/models-overview) |

## Formatting

| Feature                                                      | Language(s)                                                  |
| :----------------------------------------------------------- | ------------------------------------------------------------ |
| [Smart Formatting](https://developers.deepgram.com/docs/smart-format) | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Diarization](https://developers.deepgram.com/docs/diarization) | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Filler words](https://developers.deepgram.com/docs/filler-words) | [English (all available regions)](https://developers.deepgram.com/docs/models-overview) |
| [Numerals](https://developers.deepgram.com/docs/numerals)    | [English (all available regions)](https://developers.deepgram.com/docs/models-overview) |
| [Punctuation](https://developers.deepgram.com/docs/punctuation) | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Paragraphs](https://developers.deepgram.com/docs/paragraphs) | [All in which words are delimited by spaces](https://developers.deepgram.com/docs/models-overview) |
| [Profanity Filter](https://developers.deepgram.com/docs/profanity-filter) | [English (all available regions)](https://developers.deepgram.com/docs/models-overview) |
| [Redaction](https://developers.deepgram.com/docs/redaction)  | [English (all available regions)](https://developers.deepgram.com/docs/models-overview) |
| [Utterances](https://developers.deepgram.com/docs/utterances) | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Utterance Split](https://developers.deepgram.com/docs/utterance-split) | [All available](https://developers.deepgram.com/docs/models-overview) |

## Custom vocabulary

| Feature                                                      | Language(s)                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Find and Replace](https://developers.deepgram.com/docs/find-and-replace) | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Keywords](https://developers.deepgram.com/docs/keywords)    | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Search](https://developers.deepgram.com/docs/search)        | [All available](https://developers.deepgram.com/docs/models-overview) |

## Media input settings

| Feature                                                      | Language(s)                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Multichannel](https://developers.deepgram.com/docs/multichannel) | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Channels](https://developers.deepgram.com/docs/channels)    | [All available](https://developers.deepgram.com/docs/models-overview) |

## Result processing

| Feature                                                      | Language(s)                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Callback](https://developers.deepgram.com/docs/callback)    | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Tagging](https://developers.deepgram.com/docs/tagging)      | [All available](https://developers.deepgram.com/docs/models-overview) |
| [Extra Metadata](https://developers.deepgram.com/docs/extra-metadata) | [All available](https://developers.deepgram.com/docs/models-overview) |

## Intelligence

| Feature                                                      | Language(s)                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Sentiment Analysis](https://developers.deepgram.com/docs/sentiment-analysis) | [English (all available regions)](https://developers.deepgram.com/docs/languages-overview) |
| [Intent Recognition](https://developers.deepgram.com/docs/intent-recognition) | [English (all available regions)](https://developers.deepgram.com/docs/languages-overview) |
| [Topic Detection](https://developers.deepgram.com/docs/topic-detection) | [English (all available regions)](https://developers.deepgram.com/docs/languages-overview) |
| [Summarization](https://developers.deepgram.com/docs/summarization) | [English (all available regions)](https://developers.deepgram.com/docs/languages-overview) |
| [Entity Detection](https://developers.deepgram.com/docs/detect-entities) | [English (all available regions)](https://developers.deepgram.com/docs/languages-overview) |

Updated 15 days ago



# [Starter Apps](https://developers.deepgram.com/docs/stt-pre-recorded-starter-apps)

Get up and running fast with our suite of pre-recorded starter applications which come fully integrated with Deepgram out-of-the-box

---

# Pre-Recorded Audio Quickstarts

[Node.js Starter](https://github.com/deepgram-starters/prerecorded-node-starter)
[Flask Starter](https://github.com/deepgram-starters/prerecorded-flask-starter)
[.NET Starter](https://github.com/deepgram-starters/deepgram-csharp-starters/tree/main/Starter-01)
[Go Starter](https://github.com/deepgram-starters/deepgram-go-starters/tree/main/Starter-01)
[Sinatra Starter](https://github.com/deepgram-starters/prerecorded-sinatra-starter)
[Java Starter](https://github.com/deepgram-starters/deepgram-java-starters/tree/main/Starter-01)
[PHP Starter](https://github.com/deepgram-starters/deepgram-php-starters/tree/main/Starter-01)
[Django Starter](https://github.com/deepgram-starters/prerecorded-django-starter)

Updated 1 day ago



# [Automatically Generating WebVTT & SRT Captions](https://developers.deepgram.com/docs/automatically-generating-webvtt-and-srt-captions)

Learn how to create ready-to-upload caption files for the web and broadcast.

---

One use for the Deepgram API includes providing captions for audio and video, which is critical for accessibility. In this guide, you'll learn how to automatically generate WebVTT and SRT captions for an audio file. We will provide two sets of code samples--one without using the Deepgram SDK so you can see the technique, and one using Deepgram's SDKs to make it even easier.

> ℹ️ If you'd like to learn more about inclusive design and accessibility, we recommend checking out [Microsoft's Inclusive Toolkit](https://www.microsoft.com/design/inclusive/).

## Before You Begin

Before you run the code, you'll need to do a few things.

### Create a Deepgram Account

Before you can use Deepgram products, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes:

- $200 in credit, which gives you access to:
  - all base [models](https://developers.deepgram.com/docs/model/)
  - pre-recorded and [live streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) functionality
  - all [features](https://developers.deepgram.com/docs/features-overview)

### Create a Deepgram API Key

To access Deepgram’s API, you'll need to [create a Deepgram API Key](https://console.deepgram.com/signup?jump=keys). Make note of your API Key; you will need it later.

### Configure the Environment

We assume you have already configured a Node.js or Python development environment on your machine. [Download Node.js](https://nodejs.org/en/).

> ℹ️ If you get stuck at any point, you can find help in our [Github community discussions](https://github.com/orgs/deepgram/discussions)!

## Getting Familiar with Captioning Formats

In this tutorial, we are going to work with two common and similar caption formats: WebVTT and SRT. Both formats contain only subtitle information, which must be added to video for a final product. When the caption files are loaded into a compatible video platform, captions will be displayed in the foreground of media, as per the information contained in that file.

### WebVTT Files

Web Video Text Track (WebVTT) files generally consist of a sequence of text segments associated with a time-interval, called a cue. It is mainly used to mark up external text track resources in connection with the HTML `<track>` element. WebVTT files provide captions or subtitles for video content, and also text video descriptions [MAUR], chapters for content navigation, and more generally any form of metadata that is time-aligned with audio or video content. To learn more, visit W3C's [WebVTT: The Web Video Text Tracks Format](https://www.w3.org/TR/webvtt1/).

An example WebVTT file:

```vtt
WEBVTT

NOTE
Transcription provided by Deepgram
Request Id: 686278aa-d315-4aeb-b2a9-713615544366
Created: 2023-10-27T15:35:56.637Z
Duration: 25.933313
Channels: 1

00:00:00.080 --> 00:00:03.220
Yeah. As as much as, it's worth celebrating,

00:00:04.400 --> 00:00:05.779
the first, spacewalk,

00:00:06.319 --> 00:00:07.859
with an all female team,

00:00:08.475 --> 00:00:10.715
I think many of us are looking forward

00:00:10.715 --> 00:00:13.215
to it just being normal and

00:00:13.835 --> 00:00:16.480
I think if it signifies anything, It is

00:00:16.779 --> 00:00:18.700
to honor the the women who came before

00:00:18.700 --> 00:00:21.680
us who, were skilled and qualified,

00:00:22.300 --> 00:00:24.779
and didn't get the same opportunities that we

00:00:24.779 --> 00:00:25.439
have today.
```

### SRT Files

SubRip Text (SRT) files also generally consist of a sequence of text segments associated with a time-interval. To learn more, visit the open source [Matroska multimedia container format website](https://www.matroska.org/technical/subtitles.html#srt-subtitles).

An example SRT file:

```srt
1
00:00:00,080 --> 00:00:03,220
Yeah. As as much as, it's worth celebrating,

2
00:00:04,400 --> 00:00:07,859
the first, spacewalk, with an all female team,

3
00:00:08,475 --> 00:00:10,715
I think many of us are looking forward

4
00:00:10,715 --> 00:00:14,235
to it just being normal and I think

5
00:00:14,235 --> 00:00:17,340
if it signifies anything, It is to honor

6
00:00:17,340 --> 00:00:19,820
the the women who came before us who,

7
00:00:20,140 --> 00:00:23,580
were skilled and qualified, and didn't get the

8
00:00:23,580 --> 00:00:25,439
same opportunities that we have today.
```

> ℹ Note that both WebVTT and SRT are similar in their basic forms--the difference is that the millisecond separator is `.` in WebVTT and `,` in SRT.

## Transcribing Captions

Now that you understand the basics of the WebVTT and SRT captioning formats, you can start transcribing your captions.

> ℹ This article covers creating subtitle files from files submitted to the Deepgram pre-recorded audio API. For an example of creating subtitle files with the Deepgram live streaming API, check out the [streaming test suite](https://github.com/deepgram/streaming-test-suite).

### Choose an Audio File

Locate a hosted audio file that you would like to caption and make note of its URL. If you can't find one, you can use `<https://static.deepgram.com/examples/deep-learning-podcast-clip.wav>`.

### Install the SDK

Open your terminal, navigate to the location on your drive where you want to create your project, and install the Deepgram SDK.

```shell
pip install deepgram-sdk
```

### Write the Code

In your terminal, create a new `index.js` or `index.py` file in your project's location, open it in your code editor, and populate it with code.

#### Set Up Dependencies

Initialise your dependencies:

```python
from deepgram import Deepgram
deepgram = Deepgram("YOUR_API_KEY")
```

> ⚠️ Be sure to replace `YOUR_API_KEY`with your Deepgram API Key.

#### Get the Transcript

To receive timestamps of phrases to include in your caption files, ask Deepgram to include [utterances](https://developers.deepgram.com/docs/utterances/) (a chain of words or, more simply, a phrase):

```python
response = deepgram.response = transcription.sync_prerecorded({"url": "YOUR_FILE_LOCATION"}, {'smart_format': True, 'utterances': True})
```

> ⚠️ Be sure to replace `YOUR_FILE_LOCATION` with the URL of the file you would like to caption.

#### Create a Write Stream

With JavaScript, open a writable stream, so you will be able to insert text directly into your file. When you open your stream, you should pass in the `a` flag, so that any time you write data to the stream, it will be appended to the end. Add inside the `.then()` block.

JavaScript

```javascript
// WebVTT Filename
const stream = fs.createWriteStream("output.vtt", { flags: "a" });

// SRT Filename
const stream = fs.createWriteStream("output.srt", { flags: "a" });
```

#### Write the Captions

The WebVTT and SRT formats are very similar, and each requires a block of text per utterance.

```python
deepgram.extra.to_WebVTT(response)
```

Deepgram provides seconds back as a number (`15.4` means 15.4 seconds), but both formats require times as `HH:MM:SS.milliseconds` and getting the end of a `Date().toISOString()` will achieve this for us.

```python
deepgram.extra.to_SRT(response)
```

> ⚠️ The differences between the non-SDK WebVTT and SRT code include:
>
> - The WebVTT code has a `WEBVTT` line at the top, whereas the SRT code does not.
> - The millisecond separator is `.` for WebVTT whereas it is `,` for SRT.
> - In the WebVTT file, there is a `-` before the utterance, whereas in the SRT code, there is not.

Updated 3 months ago



# [Using Callbacks to Return Transcripts to Your Server](https://developers.deepgram.com/docs/using-callbacks-to-return-transcripts-to-your-server)

Learn how to return transcripts to a callback URL sent to Deepgram's API.

---

When working with the Deepgram API, you can use a [callback](https://developers.deepgram.com/docs/callback/) to return your transcription to a URL on your server.

In this guide, you will learn how to use Deepgram's webhook to return a transcript generated by Deepgram's API to a callback URL that you provide.

## What is a Webhook?

When using a web application, you often change the information being displayed on the web page you're on. For example, while browsing a list of blog posts, you may click on a link to show more posts. When you do this, the web application's UI on your machine (client) sends an HTTP request to the application's server. The server then sends a response back to your device, which then triggers a change in the UI of the web application.

But when a web application’s server wants to trigger an event based on something that’s happening on a remote server instead of a user action, we use webhooks.

A webhook is a 'reverse HTTP request' between servers rather than between a client and a server. A remote server (Deepgram) sends an HTTP POST request to a public URL on your application’s server every time an event occurs on their end, so you can trigger an event in your own application based on that update.

## Waiting for a Transcript

When requesting a transcript from Deepgram, you can wait for it to be generated, but this can take a few more seconds than you might be able to wait for larger files. Instead, you can access Deepgram's webhook by including the [callback](https://developers.deepgram.com/docs/callback/) feature in your request, which will allow you to redirect any transcription results to the URL of your choice.

### Use Cases

Because you control the application that receives the webhook payload, you can build any additional business logic to run once you have data. You might:

- Send an email to your client to let them know that their transcript is complete with the results.
- Translate the transcript provided to your server to be displayed on your application’s UI.
- Send an SMS text to the user's phone with a brief preview of the results.

### Prepare to Receive Incoming Transcripts on Your Server

To receive incoming transcripts on your server, you need to create an webhook consumer in your application. Your webhook consumer is basically a route handler, but instead of receiving requests from a user action, it is triggered by the service emitting webhooks--in this case Deepgram.

Since webhooks send a `POST` request to your application, your webhook consumer will need to create a `POST` route handler in your application. So the webhook consumer receiving transcripts on your server might look something like this:

```javascript
// Require, initialize, and configure Express
const express = require("express");
const app = express();
app.use(express.json());

// This is the route handler our webhook will POST data to
app.post("/hook", (req, res) => {
	/*
        You could do anything here, such as:
        Add data to a database
        Trigger an email or SMS
        Automatically schedule an event on your application's UI
    */

	console.log(req.body); // See the data
	res.status(200).end(); // Return empty response to server
});

// Start express server
app.listen(3000);
```

For this example, assume that your application's URL is [https://exampleco.com](https://exampleco.com/), which means your webhook consumer’s URL is https://exampleco.com/hook, based on how the route handler is configured in the sample code.

### Send a Request to Deepgram

To send a request to Deepgram and receive the transcript on your server, you need to provide your webhook consumer's URL in the request to Deepgram. You do that by using Deepgram's Callback feature.

To transcribe audio from a file on your computer, for example, run the following cURL command in a terminal or your favorite API client:

> ℹ Be sure to replace the placeholder `YOUR_DEEPGRAM_API_KEY` with your Deepgram API Key. You can [create an API Key](https://developers.deepgram.com/docs/authenticating#create-an-api-key) in the [Deepgram Console](https://console.deepgram.com/).

```sh
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?callback=https://exampleco.com/hook'
```

### See Results

When you supply a callback URL in your request to Deepgram's API, we will immediately respond with a `request_id`:

```json
{ "request_id": "c22bea24-ecd3-4b53-bcbf-8ef087d905a5" }
```

We will then process your audio asynchronously and return the transcript to your server through the callback URL you provided.
If the HTTP status code of the response to the callback POST request is unsuccessful (not 200-299), Deepgram will retry the callback up to 10 times with a 30 second delay between attempts.

To learn more about the response returned to your server, see our API reference for [Transcribe Pre-recorded Audio: Responses](https://developers.deepgram.com/reference/pre-recorded) or [Transcribe Streaming Audio: Responses](https://developers.deepgram.com/reference/streaming), and the [Feature documentation](https://developers.deepgram.com/docs/features-overview) for the features you enabled in your request.

Updated 3 months ago



# [When Callback Is Not Received](https://developers.deepgram.com/docs/payload-too-large)

More often than not, requests that include a callback URL should receive an asynchronous response, even if the callback receives an error.

When attempting to transcribe a large audio file, there are multiple reasons you may not receive your transcription.

> ℹ As of the moment of publishing this guide, you cannot **yet** see whether a callback errored from the Deepgram Console usage logs.

## Express.js bodyParser / Next.js API Routes

Some serverless, including popular architecture like Express.s, use `bodyParser` to understand the body of the request being passed to your application.

By default, `bodyParser` includes a small default maximum payload size of **100kb**, to responsibly limit impact of memory allocation on the server running your application. Essentially, you knowingly need to increase this, and hopefully understand what that would mean for the architecture you're working on. Especially for serverless environments.

If this limit is reached when Deepgram attempts a callback request, `bodyParser` will return a `413 Request Entity Too Large` response. Your server will most likely log the errors occurance, as it rejects the request from Deepgram.

### bodyParser Solution

For bodyParser being used as middleware, you need to configure the parser with a new limit.

```javascript
// parse application/json
jsonParser = bodyParser.json({
  limit: '1mb' // raise from 100kb to 1mb
})

// parse raw
rawParser = bodyParser.raw({
  limit: '1mb' // raise from 100kb to 1mb
})
```

### Next.js API Routes Solution

To resolve this error in in Next.js API Routes, you need to configure the parser with a new limit. At the top of your API Routes file, include additional config.

```javascript
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '1mb', // raise from 100kb to 1mb
    },
  }
}
```

## NGINX

Many hosted servers, particularly NGINX based servers, have a maximum payload size for incoming requests. For example, NGINX has a default maximum payload size of `1 MB`, which could be insufficient for larger transcripts.

A server will reject a callback due to the transcript size exceeding the payload limit, returning a `413` code and the message `Request entity too large`/`Content too large`/`Payload too large`, depending on which server receives the large payload.

### NGINX Solution

To resolve the "Payload too large" issue for NGINX, follow these steps:

1. Confirm the server's maximum payload size: Determine if the server you are using has a maximum payload size limit. NGINX servers, for example, typically have a maximum payload size of `1 MB` by default.
2. Adjust NGINX server configuration: You can modify the NGINX configuration to increase the maximum payload size. Locate and edit the NGINX configuration file, typically named `nginx.conf,` and find the `client_max_body_size` directive (or add it, if it's missing). Adjust its value to accommodate your transcript size. For example, if your transcript is 5 MB, you may set the value to `5m` or higher.
3. Restart the server: **After modifying the server configuration, save the changes and restart the server** to apply the new settings. If you are running a Linux server, the command `service nginx reload` will restart the NGINX server.
4. Retry the transcription request: Once the server is restarted, attempt the transcription again. Ensure the transcript size now falls within the updated maximum payload limit. If successful, the `413: Payload too large` error should no longer occur.

Updated 3 months ago

