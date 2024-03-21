# Speech to Text - Pre-Recorded



# [Getting started](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio)

An introduction to getting transcription data from pre-recorded audio files using CURL and Deepgram's SDKs.

---

This guide will walk you through how to transcribe pre-recorded audio with the Deepgram API. We provide two scenarios to try: transcribe a remote file and transcribe a local file.

> ℹ Before you run the code, you'll need to follow the steps in the [Make Your First API Request](https://developers.deepgram.com/docs/make-your-first-api-request) guide to create a Deepgram account, get a Deepgram API key, and configure your environment if you are choosing to use a Deepgram SDK.

## CURL

First, try it with CURL. Add your own API key where it says `YOUR_DEEPGRAM_API_KEY` and then run the following examples in a terminal or your favorite API client.

If you run the "Local file CURL Example," be sure to change `@youraudio.wav` to the path/filename of an audio file on your computer. (Read more about supported audio formats [here](https://developers.deepgram.com/docs/supported-audio-formats)).

Remote File CURL Example

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"url":"https://dpgr.am/spacewalk.wav"}' \
  --url 'https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true'
```

Local File CURL Example

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true'
```

> ℹ The above example includes the parameter `model=nova-2`, which tells the API to use Deepgram's most powerful and affordable model. Removing this parameter will result in the API using the default model, which is currently `model=base`.
>
> It also includes Deepgram's [Smart Formatting](https://developers.deepgram.com/docs/smart-format) feature, `smart_format=true`. This will format currency amounts, phone numbers, email addresses, and more for enhanced transcript readability.

## Language Specific Implementations

If you would like to try out making a Deepgram speech-to-text request in a specific language (but not using Deepgram's SDKs), we offer a library of code-samples in this [Github repo](https://github.com/deepgram-devs/code-samples). However, we recommend trying out our SDKs, which you can do in the next section.

## SDKs

To transcribe pre-recorded audio using one of Deepgram's SDKs, follow these steps.

> ## 🌈
>
> For those who prefer to work from a Jupyter notebook, check out our [Python Starter Notebooks](https://developers.deepgram.com/docs/python-notebooks).

### Install the SDK

Open your terminal, navigate to the location on your drive where you want to create your project, and install the Deepgram SDK.

```shell
# Install the Deepgram Python SDK
# https://github.com/deepgram/deepgram-python-sdk

pip install deepgram-sdk
```

### Add Dependencies

```shell
# Install python-dotenv to protect your API key

pip install python-dotenv
```

## Transcribe a Remote File

This example shows how to analyze a **remote audio file** (a URL that hosts your audio file) using Deepgram's SDKs. In your terminal, create a new file in your project's location, and populate it with the code.

```python
# main.py (python example)

import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
)

load_dotenv()

# URL to the audio file
AUDIO_URL = {
    "url": "https://dpgr.am/spacewalk.wav"
}

API_KEY = os.getenv("DG_API_KEY")


def main():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # STEP 3: Call the transcribe_url method with the audio payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)

        # STEP 4: Print the response
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
```

## Transcribe a Local File

This example shows how to analyze a **local audio file** (an audio file on your computer) using Deepgram's SDKs. In your terminal, create a new file in your project's location, and populate it with the code. (Be sure to replace the audio filename with a path/filename of an audio file on your computer.)

```python
# main.py (python example)

import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

load_dotenv()

# Path to the audio file
AUDIO_FILE = "spacewalk.mp3"

API_KEY = os.getenv("DG_API_KEY")


def main():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        # STEP 4: Print the response
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
```

## Results

In order to see the results from Deepgram, you must run the application. Run your application from the terminal. Your transcripts will appear in your shell.

```shell
# Run your application using the file you created in the previous step
# Example: python main.py

python YOUR_PROJECT_NAME.py
```

> ⚠️ Deepgram does not store transcripts, so the Deepgram API response is the only opportunity to retrieve the transcript. Make sure to save output or [return transcriptions to a callback URL for custom processing](https://developers.deepgram.com/docs/callback/).

### Analyze the Response

When the file is finished processing (often after only a few seconds), you’ll receive a JSON response:

```json
{
  "metadata": {
    "transaction_key": "deprecated",
    "request_id": "2479c8c8-8185-40ac-9ac6-f0874419f793",
    "sha256": "154e291ecfa8be6ab8343560bcc109008fa7853eb5372533e8efdefc9b504c33",
    "created": "2024-02-06T19:56:16.180Z",
    "duration": 25.933313,
    "channels": 1,
    "models": [
      "30089e05-99d1-4376-b32e-c263170674af"
    ],
    "model_info": {
      "30089e05-99d1-4376-b32e-c263170674af": {
        "name": "2-general-nova",
        "version": "2024-01-09.29447",
        "arch": "nova-2"
      }
    }
  },
  "results": {
    "channels": [
      {
        "alternatives": [
          {
            "transcript": "Yeah. As as much as, it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal. And, I think if it signifies anything, It is, to honor the the women who came before us who, were skilled and qualified, and didn't get the the same opportunities that we have today.",
            "confidence": 0.99902344,
            "words": [
              {
                "word": "yeah",
                "start": 0.08,
                "end": 0.32,
                "confidence": 0.9975586,
                "punctuated_word": "Yeah."
              },
              {
                "word": "as",
                "start": 0.32,
                "end": 0.79999995,
                "confidence": 0.9921875,
                "punctuated_word": "As"
              },
              {
                "word": "as",
                "start": 0.79999995,
                "end": 1.04,
                "confidence": 0.96777344,
                "punctuated_word": "as"
              },
              {
                "word": "much",
                "start": 1.04,
                "end": 1.28,
                "confidence": 1,
                "punctuated_word": "much"
              },
              {
                "word": "as",
                "start": 1.28,
                "end": 1.5999999,
                "confidence": 0.9926758,
                "punctuated_word": "as,"
              },
              {
                "word": "it's",
                "start": 2,
                "end": 2.24,
                "confidence": 1,
                "punctuated_word": "it's"
              },
              {
                "word": "worth",
                "start": 2.24,
                "end": 2.74,
                "confidence": 1,
                "punctuated_word": "worth"
              },
              {
                "word": "celebrating",
                "start": 2.8,
                "end": 3.3,
                "confidence": 0.97143555,
                "punctuated_word": "celebrating,"
              },
              {
                "word": "the",
                "start": 4.4,
                "end": 4.64,
                "confidence": 0.9980469,
                "punctuated_word": "the"
              },
              {
                "word": "first",
                "start": 4.64,
                "end": 5.04,
                "confidence": 0.80200195,
                "punctuated_word": "first,"
              },
              {
                "word": "spacewalk",
                "start": 5.2799997,
                "end": 5.7799997,
                "confidence": 0.9468994,
                "punctuated_word": "spacewalk,"
              },
              {
                "word": "with",
                "start": 6.3199997,
                "end": 6.56,
                "confidence": 1,
                "punctuated_word": "with"
              },
              {
                "word": "an",
                "start": 6.56,
                "end": 6.72,
                "confidence": 0.99902344,
                "punctuated_word": "an"
              },
              {
                "word": "all",
                "start": 6.72,
                "end": 6.96,
                "confidence": 0.9980469,
                "punctuated_word": "all"
              },
              {
                "word": "female",
                "start": 6.96,
                "end": 7.3599997,
                "confidence": 1,
                "punctuated_word": "female"
              },
              {
                "word": "team",
                "start": 7.3599997,
                "end": 7.8599997,
                "confidence": 0.91625977,
                "punctuated_word": "team,"
              },
              {
                "word": "i",
                "start": 8.395,
                "end": 8.555,
                "confidence": 0.94384766,
                "punctuated_word": "I"
              },
              {
                "word": "think",
                "start": 8.555,
                "end": 8.875,
                "confidence": 0.99902344,
                "punctuated_word": "think"
              },
              {
                "word": "many",
                "start": 8.875,
                "end": 9.115001,
                "confidence": 0.9838867,
                "punctuated_word": "many"
              },
              {
                "word": "of",
                "start": 9.115001,
                "end": 9.3550005,
                "confidence": 1,
                "punctuated_word": "of"
              },
              {
                "word": "us",
                "start": 9.3550005,
                "end": 9.8550005,
                "confidence": 1,
                "punctuated_word": "us"
              },
              {
                "word": "are",
                "start": 9.995001,
                "end": 10.235001,
                "confidence": 0.9633789,
                "punctuated_word": "are"
              },
              {
                "word": "looking",
                "start": 10.235001,
                "end": 10.475,
                "confidence": 0.9980469,
                "punctuated_word": "looking"
              },
              {
                "word": "forward",
                "start": 10.475,
                "end": 10.795,
                "confidence": 1,
                "punctuated_word": "forward"
              },
              {
                "word": "to",
                "start": 10.795,
                "end": 10.955,
                "confidence": 1,
                "punctuated_word": "to"
              },
              {
                "word": "it",
                "start": 10.955,
                "end": 11.115001,
                "confidence": 0.99902344,
                "punctuated_word": "it"
              },
              {
                "word": "just",
                "start": 11.115001,
                "end": 11.3550005,
                "confidence": 0.9980469,
                "punctuated_word": "just"
              },
              {
                "word": "being",
                "start": 11.3550005,
                "end": 11.8550005,
                "confidence": 0.9980469,
                "punctuated_word": "being"
              },
              {
                "word": "normal",
                "start": 11.995001,
                "end": 12.495001,
                "confidence": 0.98535156,
                "punctuated_word": "normal."
              },
              {
                "word": "and",
                "start": 12.715,
                "end": 13.115,
                "confidence": 0.9555664,
                "punctuated_word": "And,"
              },
              {
                "word": "i",
                "start": 13.915001,
                "end": 13.995001,
                "confidence": 0.99902344,
                "punctuated_word": "I"
              },
              {
                "word": "think",
                "start": 13.995001,
                "end": 14.235001,
                "confidence": 1,
                "punctuated_word": "think"
              },
              {
                "word": "if",
                "start": 14.235001,
                "end": 14.395,
                "confidence": 0.9902344,
                "punctuated_word": "if"
              },
              {
                "word": "it",
                "start": 14.395,
                "end": 14.555,
                "confidence": 0.9892578,
                "punctuated_word": "it"
              },
              {
                "word": "signifies",
                "start": 14.555,
                "end": 15.055,
                "confidence": 1,
                "punctuated_word": "signifies"
              },
              {
                "word": "anything",
                "start": 15.115,
                "end": 15.615,
                "confidence": 0.98217773,
                "punctuated_word": "anything,"
              },
              {
                "word": "it",
                "start": 15.82,
                "end": 15.98,
                "confidence": 0.88671875,
                "punctuated_word": "It"
              },
              {
                "word": "is",
                "start": 15.98,
                "end": 16.38,
                "confidence": 0.9008789,
                "punctuated_word": "is,"
              },
              {
                "word": "to",
                "start": 16.779999,
                "end": 17.02,
                "confidence": 1,
                "punctuated_word": "to"
              },
              {
                "word": "honor",
                "start": 17.02,
                "end": 17.34,
                "confidence": 1,
                "punctuated_word": "honor"
              },
              {
                "word": "the",
                "start": 17.34,
                "end": 17.58,
                "confidence": 1,
                "punctuated_word": "the"
              },
              {
                "word": "the",
                "start": 17.58,
                "end": 17.74,
                "confidence": 0.99316406,
                "punctuated_word": "the"
              },
              {
                "word": "women",
                "start": 17.74,
                "end": 18.06,
                "confidence": 0.93603516,
                "punctuated_word": "women"
              },
              {
                "word": "who",
                "start": 18.06,
                "end": 18.22,
                "confidence": 1,
                "punctuated_word": "who"
              },
              {
                "word": "came",
                "start": 18.22,
                "end": 18.46,
                "confidence": 1,
                "punctuated_word": "came"
              },
              {
                "word": "before",
                "start": 18.46,
                "end": 18.7,
                "confidence": 1,
                "punctuated_word": "before"
              },
              {
                "word": "us",
                "start": 18.7,
                "end": 19.2,
                "confidence": 1,
                "punctuated_word": "us"
              },
              {
                "word": "who",
                "start": 19.42,
                "end": 19.82,
                "confidence": 0.8569336,
                "punctuated_word": "who,"
              },
              {
                "word": "were",
                "start": 20.22,
                "end": 20.46,
                "confidence": 0.97314453,
                "punctuated_word": "were"
              },
              {
                "word": "skilled",
                "start": 20.46,
                "end": 20.86,
                "confidence": 1,
                "punctuated_word": "skilled"
              },
              {
                "word": "and",
                "start": 20.86,
                "end": 21.18,
                "confidence": 0.99609375,
                "punctuated_word": "and"
              },
              {
                "word": "qualified",
                "start": 21.18,
                "end": 21.68,
                "confidence": 0.9848633,
                "punctuated_word": "qualified,"
              },
              {
                "word": "and",
                "start": 22.3,
                "end": 22.619999,
                "confidence": 1,
                "punctuated_word": "and"
              },
              {
                "word": "didn't",
                "start": 22.619999,
                "end": 22.86,
                "confidence": 0.9655762,
                "punctuated_word": "didn't"
              },
              {
                "word": "get",
                "start": 22.86,
                "end": 23.18,
                "confidence": 1,
                "punctuated_word": "get"
              },
              {
                "word": "the",
                "start": 23.18,
                "end": 23.42,
                "confidence": 0.7626953,
                "punctuated_word": "the"
              },
              {
                "word": "the",
                "start": 23.42,
                "end": 23.66,
                "confidence": 0.625,
                "punctuated_word": "the"
              },
              {
                "word": "same",
                "start": 23.66,
                "end": 23.98,
                "confidence": 0.99902344,
                "punctuated_word": "same"
              },
              {
                "word": "opportunities",
                "start": 23.98,
                "end": 24.46,
                "confidence": 1,
                "punctuated_word": "opportunities"
              },
              {
                "word": "that",
                "start": 24.46,
                "end": 24.619999,
                "confidence": 1,
                "punctuated_word": "that"
              },
              {
                "word": "we",
                "start": 24.619999,
                "end": 24.779999,
                "confidence": 1,
                "punctuated_word": "we"
              },
              {
                "word": "have",
                "start": 24.779999,
                "end": 25.02,
                "confidence": 1,
                "punctuated_word": "have"
              },
              {
                "word": "today",
                "start": 25.02,
                "end": 25.52,
                "confidence": 0.97680664,
                "punctuated_word": "today."
              }
            ],
            "paragraphs": {
              "transcript": "\nYeah. As as much as, it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal. And, I think if it signifies anything, It is, to honor the the women who came before us who, were skilled and qualified, and didn't get the the same opportunities that we have today.",
              "paragraphs": [
                {
                  "sentences": [
                    {
                      "text": "Yeah.",
                      "start": 0.08,
                      "end": 0.32
                    },
                    {
                      "text": "As as much as, it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal.",
                      "start": 0.32,
                      "end": 12.495001
                    },
                    {
                      "text": "And, I think if it signifies anything, It is, to honor the the women who came before us who, were skilled and qualified, and didn't get the the same opportunities that we have today.",
                      "start": 12.715,
                      "end": 25.52
                    }
                  ],
                  "num_words": 63,
                  "start": 0.08,
                  "end": 25.52
                }
              ]
            }
          }
        ]
      }
    ]
  }
}
```

In this default response, we see:

- `transcript`: the transcript for the audio segment being processed.

- `confidence`: a floating point value between 0 and 1 that indicates overall transcript reliability. Larger values indicate higher confidence.

- `words`: an object containing each `word` in the transcript, along with its `start` time and `end` time (in seconds) from the beginning of the audio stream, and a `confidence` value.

  Because we passed the `smart_format: true` option to the `transcription.prerecorded` method, each word object also includes its `punctuated_word` value, which contains the transformed word after punctuation and capitalization are applied.

> ℹ The `transaction_key` in the `metadata` field can be ignored. The result will always be `"transaction_key": "deprecated"`.

## Limits

There are a few limits to be aware of when making a pre-recorded speech-to-text request.

### File Size

The maximum file size is limited to 2 GB.

When transcribing a large video file, the audio stream should be extracted from the video and the audio should be uploaded to Deepgram for transcription. This will significantly reduce the file size.

### Rate Limits

Deepgram limits the maximum number of concurrent requests per project.

- For Nova, Base, and Enhanced, the rate limit is 100 concurrent requests.
- For Whisper, the rate limit is 15 concurrent requests with a paid plan and 5 concurrent requests with the pay-as-you-go plan.

A `429: Too Many Requests` error is returned when requests are made in excess of the rate limits.

### Maximum Processing Time

Nova, Base, and Enhanced provide extremely fast transcription. Deepgram limits the maximum processing time to 10 minutes for these models.

Whisper is much slower than the other models, and the maximum processing time is 20 minutes for Whisper.

If a request takes longer than the maximum processing time to complete, the request is cancelled and a `504: Gateway Timeout` error is returned.

## What's Next?

Now that you've transcribed pre-recorded audio, enhance your knowledge by exploring the following areas.

### Try the Starter Apps

Clone and run one of our [Starter App](https://developers.deepgram.com/docs/docs/stt-pre-recorded-starter-apps) repositories to see a full application with a frontend UI and a backend server sending audio to Deepgram.

### Read the Feature Guides

Deepgram's features help you to customize your transcripts. Do you want to transcribe audio in other languages? Check out the [Language](https://developers.deepgram.com/docs/language) feature guide. Do you want to remove profanity from the transcript or redact personal information such as credit card numbers? Check out [Profanity Filtering](https://developers.deepgram.com/docs/profanity-filter) or [Redaction](https://developers.deepgram.com/docs/redaction).

Take a glance at our [Feature Overview](https://developers.deepgram.com/docs/stt-pre-recorded-feature-overview) for pre-recorded speech-to-text to see the list of all the features available. Then read more about each feature in its individual guide.

### Explore Use Cases

Learn about the different ways you can use Deepgram products to help you meet your business objectives. [Explore Deepgram's use cases](https://developers.deepgram.com/use-cases/).

### Transcribe Streaming Audio

Now that you know how to transcribe pre-recorded audio, check out how you can use Deepgram to transcribe streaming audio in real time. To learn more, see [Getting Started with Streaming Audio](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio/).

Updated 1 day ago