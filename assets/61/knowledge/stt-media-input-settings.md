# Speech to Text - Media Input Settings



# [Channels](https://developers.deepgram.com/docs/channels)

Channels allows you to specify the number of independent audio channels your submitted audio contains. Used when the Encoding feature is also being used to submit streaming raw audio.

[Suggest Edits](https://developers.deepgram.com/edit/channels)

```
channels` *int32*. Default: `1
```

~~Pre-recorded~~ [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

The default value is `1`.

The Channels feature is used when the [Encoding](https://developers.deepgram.com/docs/encoding/) feature is also being used to submit streaming raw audio. It is not read at any other time.

## Enable Feature

To enable Channels, when you call Deepgram’s API, add a `channels` parameter in the query string and set it to the number of channels in your submitted audio.

```
channels=NUMBER_OF_CHANNELS
```

Updated 22 days ago



# [Encoding](https://developers.deepgram.com/docs/encoding)

Encoding allows you to specify the expected encoding of your submitted audio.

---

`encoding` *string*.

~~Pre-recorded~~ [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

Encoding is required when raw, headerless audio packets are sent to the streaming service. If containerized audio packets are sent to the streaming service, this feature should not be used.

If using the Encoding feature, the [Sample Rate](https://developers.deepgram.com/docs/sample-rate/) feature is also required.

## Enable Feature

To enable Encoding, when you call Deepgram’s API, add an `encoding` parameter in the query string and set it to the audio coding algorithm of your submitted audio:

```
encoding=OPTION
```

Deepgram supports the following audio coding algorithms:

- `linear16`: 16-bit, little endian, signed PCM WAV data
- `flac`: Free Lossless Audio Codec (FLAC) encoded data
- `mulaw`: Mu-law encoded WAV data
- `amr-nb`: Adaptive Multi-Rate (AMR) narrowband codec
- `amr-wb`: Adaptive Multi-Rate (AMR) wideband codec
- `opus`: Ogg Opus
- `speex`: Speex

For an example of audio streaming, see [Getting Started with Streaming Audio](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio/).

For help determining your audio format and sample rate, see [Determining Your Audio Format for Live Streaming Audio](https://developers.deepgram.com/docs/determining-your-audio-format-for-live-streaming-audio/).

## Use Cases

Some examples of use cases for Encoding include:

- Customers who need to stream raw audio data. Not sure if you need to stream raw audio data? Check out [Determining Your Audio Format for Live Streaming Audio](https://developers.deepgram.com/docs/determining-your-audio-format-for-live-streaming-audio/).

Updated 4 months ago



# [Multichannel](https://developers.deepgram.com/docs/multichannel)

Multichannel transcribes each channel in submitted audio independently.

---

`multichannel` *boolean*. Default: `false`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

When set to `true`, you will receive separate transcripts for each channel.

To learn more about multichannel audio and to learn when to use Deepgram's Multichannel or Diarization feature, see [Understanding when to Use the Multichannel and Diarization Features](https://developers.deepgram.com/docs/multichannel-vs-diarization/).

> ℹ When processing pre-recorded audio, you can apply a different model to each channel using the `model` parameter. For example, set `model=general:phonecall`, which applies the `general` model to channel 0 and the `phonecall` model to channel 1 (`multichannel=true&model=general:phonecall`).

## Enable Feature

To enable Multichannel, when you call Deepgram’s API, add a `multichannel` parameter set to `true` in the query string:

```
multichannel=true
```

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/mp3' \
  --data-binary @youraudio.mp3 \
  --url 'https://api.deepgram.com/v1/listen?multichannel=true'
```

![:eyes:](https://developers.deepgram.com/public/img/emojis/eyes.png) Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Analyze Response

> ℹ For this example, we use an MP3 split stereo audio file that contains the first 10 seconds of a customer call with a florist. If you would like to follow along, you can [download it](https://res.cloudinary.com/deepgram/video/upload/v1682106551/devex/florist_altodz.mp3).

When the file is finished processing (often after only a few seconds), you’ll receive a JSON response.

Note that the response structure differs depending on whether audio is submitted to our pre-recorded endpoint or our streaming endpoint.

### Pre-Recorded Response

```json
{
	"metadata": {
		...
		"channels": 0
	},
	"results": {
		"channels": [
			{
				"alternatives": []
			}
		]
	}
}
```

For this response, the `channels` property under `metadata` will be set to `2` because our sample audio track has two channels.

Let's look more closely at the `channels` object under `results`:

```json
...
"channels":[
  {
    "alternatives":[
      {
        "transcript":"thank you for calling marcus flowers how history i'd be happy to take care of your order may i have your name please",
        "confidence":0.98221713,
        "words":[
          {"word":"thank","start":0.94,"end":1.06,"confidence":0.9963781},
					...
        ]
      }
    ]
  },
  {
    "alternatives":[
      {
        "transcript":"hello i'd like to order flowers and i think you have what i'm looking for",
        "confidence":0.99148595,
        "words":[
          {"word":"hello","start":4.0095854,"end":4.049482,"confidence":0.9823143},
					...
        ]
      }
    ]
  }
]
...
```

In this response, we see that the `channels` object contains two sub-objects, one for each channel identified in the audio. Within each channel, each alternative contains multiple objects, each of which includes:

- `transcript`: Transcript for the audio being processed.
- `confidence`: Floating point value between 0 and 1 that indicates overall transcript reliability. Larger values indicate higher confidence.
- `words`: Object containing each word in the transcript, along with its start time and end time (in seconds) from the beginning of the audio stream, and a confidence value.

In the first channel object, notice that the word `history` has an `end` time of `3.5`, while the word `i'd` has a `start` time of `7.93305`; this is a considerable gap in audio within this channel. Now, notice that in the second channel object, the first word has a `start` time of `4.0095854` and the last word has an `end` time of `7.3209844`. This time frame falls directly in the middle of the gap in the first channel object.

This makes sense because our sample audio file is a split stereo file with speakers separated on different channels. We can see that one speaker greets another in the first audio channel, waits for a response from the speaker recorded in the second audio channel, and then responds in the first audio channel.

### Streaming Response

```json
{
	"metadata": {
		...
	},
   "channel_index": [
    0,
    2
  ],
	"channel": {
		"alternatives": []
	}
}
```

For this response, the `channel_index` property will be set to `[0, 2]` . The second number in the array is the number of channels (in this case, 2). The first number is the channel that the transcript in the message belongs to. In our example, you will see messages with `[0, 2]` representing transcription of the first channel, and `[1, 2]` for transcription of the second channel.

Let's look more closely at the results of the stream. Deepgram will send back separate messages for each channel, like so:

```json
{
  "metadata": {
    ...
  },
  "channel_index": [
    0,
    2
  ],
  "duration": 3.58,
  "start": 0,
  "is_final": true,
  "speech_final": true,
  "channel": {
    "alternatives": [
      {
        "transcript": "thank you for calling martha flores how may i assist you",
        "confidence": 0.99853516,
        "words": [
          {
            "word": "thank",
            "start": 0.64,
            "end": 0.79999995,
            "confidence": 0.99853516
          },
          {
            "word": "you",
            "start": 0.79999995,
            "end": 1.04,
            "confidence": 1
          },
          {
            "word": "for",
            "start": 1.04,
            "end": 1.1999999,
            "confidence": 0.9995117
          },
          {
            "word": "calling",
            "start": 1.1999999,
            "end": 1.5999999,
            "confidence": 1
          },
          {
            "word": "martha",
            "start": 1.5999999,
            "end": 2,
            "confidence": 0.97216797
          },
          {
            "word": "flores",
            "start": 2,
            "end": 2.48,
            "confidence": 0.73010254
          },
          {
            "word": "how",
            "start": 2.48,
            "end": 2.6399999,
            "confidence": 0.9926758
          },
          {
            "word": "may",
            "start": 2.6399999,
            "end": 2.8,
            "confidence": 0.99853516
          },
          {
            "word": "i",
            "start": 2.8,
            "end": 2.8799999,
            "confidence": 0.9995117
          },
          {
            "word": "assist",
            "start": 2.8799999,
            "end": 3.1999998,
            "confidence": 1
          },
          {
            "word": "you",
            "start": 3.1999998,
            "end": 3.58,
            "confidence": 0.9963379
          }
        ]
      }
    ]
  }
}
```

This first message represents the transcription of the first channel. It will be followed by another message representing the transcription of the second channel, marked with `channel_index: [1, 2]`

```json
{
  "metadata": {
    ...
  },
  "channel_index": [
    1,
    2
  ],
  "duration": 4.43,
  "start": 3.02,
  "is_final": true,
  "speech_final": true,
  "channel": {
    "alternatives": [
      {
        "transcript": "hello i'd like to order flowers and i think you have what i'm looking for",
        "confidence": 0.99902344,
        "words": [
          {
            "word": "hello",
            "start": 3.6599998,
            "end": 4.06,
            "confidence": 0.9436035
          },
          {
            "word": "i'd",
            "start": 4.06,
            "end": 4.3,
            "confidence": 0.99902344
          },
          {
            "word": "like",
            "start": 4.3,
            "end": 4.46,
            "confidence": 0.9995117
          },
          {
            "word": "to",
            "start": 4.46,
            "end": 4.7,
            "confidence": 0.9975586
          },
          {
            "word": "order",
            "start": 4.7,
            "end": 5.02,
            "confidence": 1
          },
          {
            "word": "flowers",
            "start": 5.02,
            "end": 5.5,
            "confidence": 0.8449707
          },
          {
            "word": "and",
            "start": 5.5,
            "end": 5.74,
            "confidence": 0.9995117
          },
          {
            "word": "i",
            "start": 5.74,
            "end": 5.8199997,
            "confidence": 0.99902344
          },
          {
            "word": "think",
            "start": 5.8199997,
            "end": 6.06,
            "confidence": 0.9980469
          },
          {
            "word": "you",
            "start": 6.06,
            "end": 6.22,
            "confidence": 0.9916992
          },
          {
            "word": "have",
            "start": 6.22,
            "end": 6.46,
            "confidence": 0.9995117
          },
          {
            "word": "what",
            "start": 6.46,
            "end": 6.62,
            "confidence": 0.9995117
          },
          {
            "word": "i'm",
            "start": 6.62,
            "end": 6.7799997,
            "confidence": 0.9992676
          },
          {
            "word": "looking",
            "start": 6.7799997,
            "end": 7.18,
            "confidence": 0.9995117
          },
          {
            "word": "for",
            "start": 7.18,
            "end": 7.45,
            "confidence": 0.9416504
          }
        ]
      }
    ]
  }
}
```

## Use Cases

An example of a use case for Multichannel includes:

Customers who use audio with multiple speakers on independent channels and want transcripts to identify each speaker individually.

> ℹ By default, Deepgram applies its general AI [model](https://developers.deepgram.com/docs/model), which is a good, general purpose model for everyday situations. To learn more about the customization possible with Deepgram's API, check out the [Deepgram API Reference](https://developers.deepgram.com/reference/).

Updated 4 months ago



# [Sample Rate](https://developers.deepgram.com/docs/sample-rate)

Sample Rate allows you to specify the sample rate of your submitted audio. Required when the Encoding feature is also being used to submit streaming raw audio. It is not read at any other time.

---

`sample_rate` *int32*

Pre-recorded [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

## Enable Feature

To enable Sample Rate, when you call Deepgram’s API, add a `sample_rate` parameter in the query string and set it to the sample rate of your submitted audio.

```
sample_rate=SAMPLE_RATE_VALUE
```

> ⚠ When submitting audio encoded with the Adaptive Multi-Rate (AMR) codec, you must submit specific Sample Rate values:
>
> - `amr-nb`: AMR narrowband codec. When using this option, you must specify `sample_rate=8000` (`encoding=amr-nb&sample_rate=8000`).
> - `amr-wb`: AMR wideband codec. When using this option, you must also specify `sample_rate=16000` (`encoding=amr-wb&sample_rate=16000`).

Updated 23 days ago

