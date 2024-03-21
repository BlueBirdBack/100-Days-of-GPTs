# [Transcribe - Remote file](https://developers.deepgram.com/reference/listen-remote)

POST https://api.deepgram.com/v1/listen

Use Deepgram's speech-to-text API to transcribe and analyze pre-recorded audio.

High-speed transcription of either pre-recorded or live audio. For details on our live audio websocket server, please see our [streaming reference](https://developers.deepgram.com/reference/streaming).

> ℹ Deepgram does not store transcriptions. Make sure to save output or [return transcriptions to a callback URL for custom processing](https://developers.deepgram.com/docs/callback/).

#### REQUEST

```python
# Install the Deepgram Python SDK
# pip install deepgram-sdk

import os

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
)

load_dotenv()

AUDIO_URL = {
    "url": "https://dpgr.am/spacewalk.wav"
}


def main():
    try:
        deepgram = DeepgramClient("DEEPGRAM_API_KEY")
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )
        response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)
        return response

    except Exception as e:
        print(f"Exception: {e}")
        

if __name__ == "__main__":
    main()

```

#### RESPONSE

##### 200

##### 400

##### 401

##### 402

##### 403



#### QUERY PARAMS

**callback**

string

Callback URL to provide if you would like your submitted audio to be processed asynchronously. [Learn More](https://developers.deepgram.com/docs/callback)

**callback_method**

boolean

Enable a callback method. Default: `false`

**custom_intent**

string

Optional. A custom intent you want the model to detect within your input audio if present. Submit up to 100.

**custom_topic**

string

A custom topic you want the model to detect within your input audio if present. Submit up to one hundred topics.

**custom_intent_mode**

string

When `strict`, the model will only return intents submitted using the `custom_intent` param. When `extended`, the model will return its own detected intents in addition to those submitted using the `custom_intent` param. Default: `extended`

**custom_topic_mode**

string

When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param. Default: `extended`

extended          strict

**detect_language**

boolean

Detect the language of the provided audio. Default: `false`. [Learn More](https://developers.deepgram.com/docs/language-detection)

**detect_entities**

boolean

Entity Detection identifies and extracts key entities from content in submitted audio. Default: `false`

**detect_topics**

boolean

Identify and extract key topics. Default: `false`. [Learn More](https://developers.deepgram.com/docs/topic-detection)

**diarize**

boolean

Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0. Default: `false`. [Learn More](https://developers.deepgram.com/docs/diarization)

**dictation**

boolean

Spoken dictation commands will be converted to their corresponding punctuation marks. e.g., comma to , Default: `false`

**diarize_version**

string

Version of the diarization feature to use. Only used when the diarization feature is enabled (`diarize=true` is passed to the API). [Learn More](https://developers.deepgram.com/docs/diarization#enable-feature)

**extra**

string

To add an extra parameter in the query string and pass a key-value pair you would like to include in the response. [Learn More](https://developers.deepgram.com/docs/extra-metadata)

**filler_words**

boolean

Whether to include words like "uh" and "um" in transcription output. Default: `false`. [Learn More](https://developers.deepgram.com/docs/filler-words)

**intents**

boolean

Recognizes speaker intent throughout an entire transcript. Returns a list of text segments and the intents found within each segment. [Learn More](https://developers.deepgram.com/docs/intent-recognition)

**keywords**

string

Uncommon proper nouns or other words to transcribe that are not a part of the model's vocabulary. Can send multiple instances in query string (for example, `keywords=snuffalupagus:10&keywords=systrom:5.5`). [Learn More](https://developers.deepgram.com/docs/keywords)

**language**

string

The [BCP-47](https://tools.ietf.org/html/bcp47) language tag that hints at the primary spoken language. Default: `en`. [Learn More](https://developers.deepgram.com/docs/language)

da          en          en-AU          en-GB          en-IN          en-NZ          en-US          es          es-419          fr          fr-CA          hi          hi-Latn          id          it          ja          ko          nl          pl          pt          pt-BR          pt-PT          ru          sv          tr          uk          zh-CN          zh-TW

**measurements**

boolean

Spoken measurements will be converted to their corresponding abbreviations. e.g., milligram to mg. Default: `false`

**model**

string

AI model used to process submitted audio. Default: `nova-2-general`. [Learn More](https://developers.deepgram.com/docs/model)

nova-2-general          nova-2-meeting          nova-2-phonecall          nova-2-voicemail          nova-2-finance          nova-2-conversationalai          nova-2-video          nova-2-medical          nova-2-drivethru          nova-2-automotive          whisper          <custom_id>

**multichannel**

boolean

Transcribe each audio channel independently. Default: `false`. [Learn More](https://developers.deepgram.com/docs/multichannel)

**numerals**

boolean

Convert numbers from written format (e.g., one) to numerical format (e.g., 1). Default: `false`. [Learn More](https://developers.deepgram.com/docs/numerals)

**paragraphs**

boolean

Split audio into paragraphs. Default: `false`. [Learn More](https://developers.deepgram.com/docs/paragraphs)

**profanity_filter**

boolean

Remove profanity from the transcript. Default: `false`. [Learn More](https://developers.deepgram.com/docs/profanity-filter)

**punctuate**

boolean

Add punctuation and capitalization to the transcript. Default: `false`. [Learn More](https://developers.deepgram.com/docs/punctuation)

**redact**

string

Redact sensitive information, replacing redacted content with asterisks (*). Can send multiple instances in query string (for example, `redact=pci&redact=numbers`). Default: `false`. [Learn More](https://developers.deepgram.com/docs/redaction)

pci          numbers          true          ssn          false

**replace**

string

Terms or phrases to search for in the submitted audio and replace. Can send multiple instances in query string (for example, `replace=this:that&replace=thisalso:thatalso`). [Learn More](https://developers.deepgram.com/docs/find-and-replace)

**search**

string

Terms or phrases to search for in the submitted audio. Can send multiple instances in query string (for example, `search=speech&search=Friday`). [Learn More](https://developers.deepgram.com/docs/search)

**sentiment**

boolean

Recognizes the sentiment of the entire transcript and detects a shift in sentiment throughout the transcript. Returns a list of text segments and the sentiment found within each segment. [Learn More](https://developers.deepgram.com/docs/sentiment-analysis)

**smart_format**

boolean

Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability. Default: `false`. [Learn More](https://developers.deepgram.com/docs/smart-format)

**summarize**

string

Summarize content. Default: `v2`. [Learn More](https://developers.deepgram.com/docs/summarization)

v2

**tag**

string

Tag to associate with the request. [Learn More](https://developers.deepgram.com/docs/tagging)

**topics**

boolean

Detects topics throughout an entire transcript. Returns a list of text segments and the topics found within each segment. [Learn More](https://developers.deepgram.com/docs/topic-detection)

**utterances**

boolean

Segment speech into meaningful units based on gaps in speech. Default: `false`. [Learn More](https://developers.deepgram.com/docs/utterances)

**utt_split**

float

Length of time in seconds used to split utterances. Default: `0.8`. [Learn More](https://developers.deepgram.com/docs/utterance-split)

**version**

string

Version of the model to use. Default: `latest`. [Learn More](https://developers.deepgram.com/docs/version)

latest          <version_id>

#### BODY PARAMS

**url**

string

Public URL of a file to transcribe. For pre-signed URLs, please see [our guide](https://developers.deepgram.com/docs/using-aws-s3-presigned-urls-with-the-deepgram-api).

`https://dpgr.am/spacewalk.wav`

**HEADERS**

**Content-Type**

string

`application/json`

**Accept**

string

`application/json`

#### RESPONSES

##### 200

##### 400

##### 401

##### 402

##### 403

Updated 3 days ago



# [Transcribe - Local file](https://developers.deepgram.com/reference/listen-file)

POST https://api.deepgram.com/v1/listen

Use Deepgram's speech-to-text API to transcribe and analyze pre-recorded audio.

High-speed transcription of either pre-recorded or live audio. For details on our live audio websocket server, please see our [streaming reference](https://developers.deepgram.com/reference/streaming).

> ℹ Deepgram does not store transcriptions. Make sure to save output or [return transcriptions to a callback URL for custom processing](https://developers.deepgram.com/docs/callback/).

#### REQUEST

```python
# Install the Deepgram Python SDK
# pip install deepgram-sdk

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

AUDIO_FILE = "YOUR_LOCAL_FILE.mp3"


def main():
    try:
        deepgram = DeepgramClient("DEEPGRAM_API_KEY")

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
```

#### RESPONSE

##### 200

##### 400

##### 401

##### 402

##### 403



#### QUERY PARAMS

**callback**

string

Callback URL to provide if you would like your submitted audio to be processed asynchronously. [Learn More](https://developers.deepgram.com/docs/callback)

**callback_method**

boolean

Enable a callback method. Default: `false`

**custom_topic**

string

A custom topic you want the model to detect within your input audio if present. Submit up to one hundred topics.

**custom_topic_mode**

string

When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param. Default: `extended`

extended          strict

**diarize**

boolean

Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0. Default: `false`. [Learn More](https://developers.deepgram.com/docs/diarization)

**diarize_version**

string

Version of the diarization feature to use. Only used when the diarization feature is enabled (`diarize=true` is passed to the API). [Learn More](https://developers.deepgram.com/docs/diarization#enable-feature)

**dictation**

boolean

Spoken dictation commands will be converted to their corresponding punctuation marks. e.g., comma to , Default: `false`

**detect_entities**

boolean

Entity Detection identifies and extracts key entities from content in submitted audio. Default: `false`

**detect_language**

boolean

Detect the language of the provided audio. Default: `false`. [Learn More](https://developers.deepgram.com/docs/language-detection)

**detect_topics**

boolean

Identify and extract key topics. Default: `false`. [Learn More](https://developers.deepgram.com/docs/topic-detection)

**extra**

string

To add an extra parameter in the query string and pass a key-value pair you would like to include in the response. [Learn More](https://developers.deepgram.com/docs/extra-metadata)

**filler_words**

boolean

Whether to include words like "uh" and "um" in transcription output. Default: `false`. [Learn More](https://developers.deepgram.com/docs/filler-words)

**intents**

boolean

Recognizes speaker intent throughout an entire transcript. Returns a list of text segments and the intents found within each segment. [Learn More](https://developers.deepgram.com/docs/intent-recognition)

**keywords**

string

Uncommon proper nouns or other words to transcribe that are not a part of the model's vocabulary. Can send multiple instances in query string (for example, `keywords=snuffalupagus:10&keywords=systrom:5.5`). [Learn More](https://developers.deepgram.com/docs/keywords)

**language**

string

The [BCP-47](https://tools.ietf.org/html/bcp47) language tag that hints at the primary spoken language. Default: `en`. [Learn More](https://developers.deepgram.com/docs/language)

da          en          en-AU          en-GB          en-IN          en-NZ          en-US          es          es-419          fr          fr-CA          hi          hi-Latn          id          it          ja          ko          nl          pl          pt          pt-BR          pt-PT          ru          sv          tr          uk          zh-CN          zh-TW

**measurements**

boolean

Spoken measurements will be converted to their corresponding abbreviations. e.g., milligram to mg. Default: `false`

**model**

string

AI model used to process submitted audio. Default: `nova-2-general`. [Learn More](https://developers.deepgram.com/docs/model)

nova-2-general          nova-2-meeting          nova-2-phonecall          nova-2-voicemail          nova-2-finance          nova-2-conversationalai          nova-2-video          nova-2-medical          nova-2-drivethru          nova-2-automotive          whisper          <custom_id>

**multichannel**

boolean

Transcribe each audio channel independently. Default: `false`. [Learn More](https://developers.deepgram.com/docs/multichannel)

**numerals**

boolean

Convert numbers from written format (e.g., one) to numerical format (e.g., 1). Default: `false`. [Learn More](https://developers.deepgram.com/docs/numerals)

**paragraphs**

boolean

Split audio into paragraphs. Default: `false`. [Learn More](https://developers.deepgram.com/docs/paragraphs)

**profanity_filter**

boolean

Remove profanity from the transcript. Default: `false`. [Learn More](https://developers.deepgram.com/docs/profanity-filter)

**punctuate**

boolean

Add punctuation and capitalization to the transcript. Default: `false`. [Learn More](https://developers.deepgram.com/docs/punctuation)

**redact**

string

Redact sensitive information, replacing redacted content with asterisks (*). Can send multiple instances in query string (for example, `redact=pci&redact=numbers`). Default: `false`. [Learn More](https://developers.deepgram.com/docs/redaction)

pci          numbers          true          ssn          false

**replace**

string

Terms or phrases to search for in the submitted audio and replace. Can send multiple instances in query string (for example, `replace=this:that&replace=thisalso:thatalso`). [Learn More](https://developers.deepgram.com/docs/find-and-replace)

**smart_format**

boolean

Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability. Default: `false`. [Learn More](https://developers.deepgram.com/docs/smart-format)

**search**

string

Terms or phrases to search for in the submitted audio. Can send multiple instances in query string (for example, `search=speech&search=Friday`). [Learn More](https://developers.deepgram.com/docs/search)

**sentiment**

boolean

Recognizes the sentiment of the entire transcript and detects a shift in sentiment throughout the transcript. Returns a list of text segments and the sentiment found within each segment. [Learn More](https://developers.deepgram.com/docs/sentiment-analysis)

**summarize**

string

Summarize content. Default: `v2`. [Learn More](https://developers.deepgram.com/docs/summarization)

**tag**

string

Tag to associate with the request. [Learn More](https://developers.deepgram.com/docs/tagging)

**topics**

boolean

Detects topics throughout an entire transcript. Returns a list of text segments and the topics found within each segment. [Learn More](https://developers.deepgram.com/docs/topic-detection)

**utterances**

boolean

Segment speech into meaningful units based on gaps in speech. Default: `false`. [Learn More](https://developers.deepgram.com/docs/utterances)

**utt_split**

float

Length of time in seconds used to split utterances. Default: `0.8`. [Learn More](https://developers.deepgram.com/docs/utterance-split)

**version**

string

Version of the model to use. Default: `latest`. [Learn More](https://developers.deepgram.com/docs/version)

latest          <version_id>

#### BODY PARAMS

**RAW_BODY**

string

You can send RAW audio directly to this API endpoint.

#### HEADERS

**Content-Type**

string

audio/*

**Accept**

string

application/json

#### RESPONSES

##### 200

##### 400

##### 401

##### 402

##### 403

Updated 3 days ago



# [Transcribe - Live audio](https://developers.deepgram.com/reference/listen-live)

Use Deepgram's speech-to-text API to transcribe live-streaming audio.

---

Deepgram provides its customers with real-time, streaming transcription via its streaming endpoints. These endpoints are high-performance, full-duplex services running over the tried-and-true WebSocket protocol, which makes integration with customer pipelines simple due to the wide array of client libraries available.

To use this endpoint, connect to `wss://api.deepgram.com/v1/listen`. TLS encryption will protect your connection and data. We support a minimum of TLS 1.2.

All audio data is sent to the streaming endpoint as binary-type WebSocket messages containing payloads that are the raw audio data. Because the protocol is full-duplex, you can stream in real-time and still receive transcription responses while uploading data. Streaming buffer sizes should be between 20 milliseconds and 250 milliseconds of audio.

When you are finished, send a JSON message to the server: `{ "type": "CloseStream" }`. The server will interpret it as a shutdown command, which means it will finish processing whatever data is still has cached, send the response to the client, send a summary metadata object, and then terminate the WebSocket connection.

To learn more about working with real-time streaming data and results, see [Get Started with Streaming Audio](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio).

Deepgram does not store transcriptions. Make sure to save output or [return transcriptions to a callback URL for custom processing](https://developers.deepgram.com/docs/callback).

#### Query Params

**callback**

string

Callback URL to provide if you would like your submitted audio to be processed asynchronously. [Learn More](https://developers.deepgram.com/docs/callback)

**callback_method**

boolean

Enable a callback method. Default: false [Learn More](https://developers.deepgram.com/docs/callback#pre-recorded-audio)

**channels**

int32

Number of independent audio channels contained in submitted streaming audio. Only read when a value is provided for `encoding`. [Learn More](https://developers.deepgram.com/docs/channels)

**diarize**

boolean

Indicates whether to recognize speaker changes. When set to true, each word in the transcript will be assigned a speaker number starting at 0. [Learn More](https://developers.deepgram.com/docs/diarization)

**diarize_version**

string

Indicates the version of the diarization feature to use. Only used when the diarization feature is enabled (`diarize=true` is passed to the API). [Learn More](https://developers.deepgram.com/docs/diarization#enable-feature)

**encoding**

string

Expected encoding of the submitted streaming audio. If this parameter is set, `sample_rate` must also be specified. [Learn More](https://developers.deepgram.com/docs/encoding)

linear16          flac          mulaw          amr-nb          amr-wb          opus          speex         

**endpointing**

boolean

Indicates how long Deepgram will wait to detect whether a speaker has finished speaking (or paused for a significant period of time, indicating the completion of an idea). When Deepgram detects an endpoint, it assumes that no additional data will improve its prediction, so it immediately finalizes the result for the processed time range and returns the transcript with a `speech_final` parameter set to `true`. Endpointing may be disabled by setting `endpointing=false`. [Learn More](https://developers.deepgram.com/docs/endpointing)

**extra**

string

To add an extra parameter in the query string and pass a key-value pair you would like to include in the response. [Learn More](https://developers.deepgram.com/docs/extra-metadata)

**filler_words**

boolean

Indicates whether to include filler words like "uh" and "um" in transcript output. When set to true, these words will be included. Defaults to false. [Learn More](https://developers.deepgram.com/docs/filler-words)

**interim_results**

string

Indicates whether the streaming endpoint should send you updates to its transcription as more audio becomes available. When set to true, the streaming endpoint returns regular updates, which means transcription results will likely change for a period of time. By default, this flag is set to false. [Learn More](https://developers.deepgram.com/docs/interim-results)

**keywords**

string

Uncommon proper nouns or other words to transcribe that are not a part of the model's vocabulary. Can send multiple instances in query string (for example, `keywords=snuffalupagus:10&keywords=systrom:5.5`). [Learn More](https://developers.deepgram.com/docs/keywords)

**language**

string

The [BCP-47](https://tools.ietf.org/html/bcp47) language tag that hints at the primary spoken language. [Learn More](https://developers.deepgram.com/docs/language)

da          de          en          en-AU          en-GB          en-IN          en-NZ          en-US          es          es-419          fr          fr-CA          hi          hi-Latn          id          it          ja          ko          nl          no          pl          pt          pt-BR          pt-PT          ru          sv          ta          tr          uk          zh-CN          zh-TW         

**model**

string

AI model used to process submitted audio. [Learn More](https://developers.deepgram.com/docs/model)

nova-2-general          nova-2-meeting          nova-2-phonecall          nova-2-voicemail          nova-2-finance          nova-2-conversationalai          nova-2-video          nova-2-medical          nova-2-drivethru          nova-2-automotive          <custom_id>                  

**multichannel**

boolean

Indicates whether to transcribe each audio channel independently. [Learn More](https://developers.deepgram.com/docs/multichannel)

**numerals**

boolean

Indicates whether to convert numbers from written format (e.g., one) to numerical format (e.g., 1). [Learn More](https://developers.deepgram.com/docs/numerals)

**profanity_filter**

boolean

Indicates whether to remove profanity from the transcript. [Learn More](https://developers.deepgram.com/docs/profanity-filter)

**punctuate**

boolean

Indicates whether to add punctuation and capitalization to the transcript [Learn More](https://developers.deepgram.com/docs/punctuation)

**redact**

string

Indicates whether to redact sensitive information, replacing redacted content with asterisks (*). Can send multiple instances in query string (for example, `redact=pci&redact=numbers`). [Learn More](https://developers.deepgram.com/docs/redact)

pci          numbers          true          ssn         

**replace**

string

Terms or phrases to search for in the submitted audio and replace. Can send multiple instances in query string (for example, `replace=this:that&replace=thisalso:thatalso`). [Learn More](https://developers.deepgram.com/docs/find-and-replace)

**sample_rate**

int32

Sample rate of submitted streaming audio. Required (and only read) when a value is provided for `encoding`. [Learn More](https://developers.deepgram.com/docs/sample-rate)

**search**

string

Terms or phrases to search for in the submitted audio. Can send multiple instances in query string (for example, `search=speech&search=Friday`). [Learn More](https://developers.deepgram.com/docs/search)

**smart_format**

boolean

Indicates whether to apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability. [Learn More](https://developers.deepgram.com/docs/smart-format)

**tag**

string

Tag to associate with the request. [Learn More](https://developers.deepgram.com/docs/tagging)

**utterance_end_ms**

string

Indicates how long Deepgram will wait to send a `{"type": "UtteranceEnd"}` message after a word has been transcribed. [Learn More](https://developers.deepgram.com/docs/understanding-end-of-speech-detection-while-streaming)

**vad_events**

boolean

Indicates that speech has started. `{"type": "SpeechStarted"}` You'll begin receiving messages upon speech starting. [Learn More](https://developers.deepgram.com/docs/start-of-speech-detection)

**version**

string

Version of the model to use. [Learn More](https://developers.deepgram.com/docs/version)

latest          <version_id>         

#### Responses

| Status      | Description                        |
| ----------- | ---------------------------------- |
| 200 Success | Audio submitted for transcription. |

#### Response Schema

```json
{
  "metadata": {
    "transaction_key": "string",
    "request_id": "uuid",
    "sha256": "string",
    "created": "string",
    "duration": 0,
    "channels": 0,
    "models": [
      "string"
    ],
  },
  "type": "Results",
  "channel_index": [
    0,
    0
  ],
  "duration": 0.0,
  "start": 0.0,
  "is_final": boolean,
  "speech_final": boolean,
  "channel": {
    "alternatives": [
      {
        "transcript": "string",
        "confidence": 0,
        "words": [
          {
            "word": "string",
            "start": 0,
            "end": 0,
            "confidence": 0
          }
        ]
      }
    ],
    "search": [
      {
        "query": "string",
        "hits": [
          {
            "confidence": 0,
            "start": 0,
            "end": 0,
            "snippet": "string"
          }
        ]
      }
    ]
  }
}
```

#### Stream KeepAlive

By default, the Deepgram streaming connection will time out with a NET-0001 error code if no audio is sent by the client for 12 seconds. (See [Error Handling](https://developers.deepgram.com/reference/listen-live#error-handling) below for more information.)

To keep the websocket open without sending audio data, send the following JSON string:

```
{ "type": "KeepAlive" }
```

This will keep the streaming connection open for an additional 12 seconds. If no audio or additional KeepAlive messages are sent within the 12 second window, the streaming connection will close with a NET-0001. To avoid this error and keep the connection open, continue sending KeepAlive messages 3-5 seconds before the 12 second timeout window expires until you are ready to resume sending audio.

#### Close Stream

To gracefully close a streaming connection, send the following JSON string:

```
{ "type": "CloseStream" }
```

This tells Deepgram that no more audio will be sent. Deepgram will close the connection once all audio has finished processing.

#### Error Handling

If Deepgram encounters an error during real-time streaming, we will return a WebSocket Close frame (WebSocket Protocol specification, section 5.5.1]).

The body of the Close frame will indicate the reason for closing using one of the specification’s pre-defined status codes followed by a UTF-8-encoded payload that represents the reason for the error. Current codes and payloads in use include:

| Code | Payload   | Description                                                  |
| ---- | --------- | ------------------------------------------------------------ |
| 1008 | DATA-0000 | The payload cannot be decoded as audio. Either the encoding is incorrectly specified, the payload is not audio data, or the audio is in a format unsupported by Deepgram. |
| 1011 | NET-0000  | The service has not transmitted a Text frame to the client within the timeout window. This may indicate an issue internally in Deepgram's systems or could be due to Deepgram not receiving enough audio data to transcribe a frame. |
| 1011 | NET-0001  | The service has not received a Binary or Text frame from the client within the timeout window. This may indicate an internal issue in Deepgram's systems, the client's systems, or the network connecting them. |

To learn about debugging WebSocket errors, see [Troubleshooting WebSocket DATA and NET Errors When Live Streaming Audio](https://developers.deepgram.com/documentation/guides/troubleshoot-streaming/).

After sending a Close message, the endpoint considers the WebSocket connection closed and will close the underlying TCP connection.

Updated 9 days ago

