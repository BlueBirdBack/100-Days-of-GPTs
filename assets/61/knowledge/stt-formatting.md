# Speech to Text - Formatting



# Smart Formatting

Smart Format formats transcripts to improve readability.

---

`smart_format` *boolean*. Default: `false`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

Deepgram's Smart Format feature applies additional formatting to transcripts to optimize them for human readability.

Smart Format capabilities vary between models. When Smart Format is turned on, Deepgram will always apply the best-available formatting for your chosen combination of model, model option and language.

At minimum, Smart Format applies:

- [Punctuation](https://developers.deepgram.com/docs/punctuation/)
- [Paragraphs](https://developers.deepgram.com/docs/paragraphs/) (for white space delineated languages, such as English or Spanish)

Smart Format has the broadest support for English-language models.

- When using the English Nova or Enhanced general models, Smart Format is capable of formatting things like dates, times, currency amounts, phone numbers, emails, and URLs.
- On other English models, Smart Format will format a smaller set of entities, including dates, times, and numbers.

On non-English models, Smart Format will apply all available formatters for that language. For the majority of languages, this is currently limited to [Punctuation](https://developers.deepgram.com/docs/punctuation/) and [Paragraphs](https://developers.deepgram.com/docs/paragraphs/).

## Enable Feature

To enable Smart Formatting, when you call Deepgram's API, add a `smart_format` parameter in the query string and set it to `true`:

```
smart_format=true
```

> ℹ Smart Format enables Deepgram's Punctuation feature. If you've set `smart_format=true`, no need to also set `punctuate=true`.

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?smart_format=true'
```

> ⚠ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Results

Once applied, results will appear in the transcript.

| Truth                                                        | Before Smart Format                                          | After Smart Format                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| i'm recording this at eight thirty seven pm on wednesday it's november second twenty twenty two i just ate thirty three grams of pasta and then drank fifty five milliliters of water at three hundred main street then i walked down to one two three southeast main street to get my package with tracking number one z five seven a two b | i'm recording this at eight thirty seven pm on wednesday it's november second twenty twenty two i just ate thirty three grams of pasta and then drank fifty five milliliters of water at three hundred main street then i walked down to one two three southeast main street to get my package with tracking number one z five seven a two b | I'm recording this at 8:37 PM on Wednesday, it's November 2 2022. I just ate 33 grams of pasta, and then drank 55 milliliters of water at 300 Main Street.  Then I walked down to 123 Southeast Main Street to get my package with tracking number 1Z57A2B. |

> ℹ When using Smart Format with live-streamed audio, if a speaker begins saying a number, Deepgram will wait to return a transcription until the speaker has finished and continues on to non-numerical speech. This behavior ensures numbers have the best possible formatting and are not broken up over multiple chunks. To override this behavior and return results immediately, add the parameter `no_delay=true` to your streaming API request.

## Use Cases

Examples of use cases for Smart Format include:

- Customers who want to improve transcript readability.
- Customers who want to search transcripts for specific types of entities to perform data analysis.
- Customers who want to build custom redaction functional that only operates on specific types of entities.

## Additional Formatters

These formatters are not included in Smart Formatting but may be enabled individually.

### Measurements

If Measurements is enabled, spoken measurements will be converted to their corresponding abbreviations.

To enable Measurements, when you call Deepgram's API, add `measurements=true` to your request.

The following units will be converted to their abbreviations.

| Unit          | Abbreviation |
| ------------- | ------------ |
| milligram(s)  | mg           |
| centigram(s)  | cg           |
| gram(s)       | g            |
| kilogram(s)   | kg           |
| milliliter(s) | ml           |
| centiliter(s) | cl           |
| liter(s)      | l            |
| kiloliter(s)  | kl           |
| millimeter(s) | mm           |
| centimeter(s) | cm           |
| meter(s)      | m            |
| kilometer(s)  | km           |

### Dictation

If Dictation is enabled, spoken dictation commands will be converted to their corresponding punctuation marks.

To enable Dictation, when you call Deepgram's API, add `dictation=true&punctuate=true` to your request. Punctuation must be enabled for Dictation to work.

The following commands will be converted.

| Command          | Converted Text |
| ---------------- | -------------- |
| period           | .              |
| comma            | ,              |
| colon            | :              |
| question mark    | ?              |
| exclamation mark | !              |
| new paragraph    | `<\n>`         |

Updated about 2 months ago



# [Diarization](https://developers.deepgram.com/docs/diarization)

Diarize recognizes speaker changes and assigns a speaker to each word in the transcript.

---

`diarize` *boolean*. Default: `false`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

To learn more about diarization and multichannel audio, and to learn when to use Deepgram's Diarization or Multichannel feature, see [Understanding when to Use the Multichannel and Diarization Features](https://developers.deepgram.com/docs/multichannel-vs-diarization).

## Enable Feature

To enable Diarization, use the following parameter in the query string when you call Deepgram’s `/listen` endpoint :

```
diarize=true
```

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?diarize=true'
```

> ⚠ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Analyze Response

> ℹ For this example, we use an MP3 audio file that contains the beginning of a customer call with Premier Phone Services. If you would like to follow along, you can [download it](https://res.cloudinary.com/deepgram/video/upload/v1680127025/dg-audio/nasa-spacewalk-interview_ljjahn.wav).

When the file is finished processing, you’ll receive a JSON response. Let's look more closely at the `words` object within the `alternatives` object within this response.

### Pre-Recorded

When using diarization for pre-recorded audio, both `speaker` and `speaker_confidence` values will be returned:

```json
...
"alternatives":[
  {
    ...
    "words": [
      {
        "word":"hello",
        "start":15.259043,
        "end":15.338787,
        "confidence":0.9721591,
        "speaker":0,
        "speaker_confidence":0.5853265
      },
    ...
    ]
  }
]
```

### Live Streaming

When using diarization for live streaming audio, only the `speaker` value will be returned:

```json
...
"alternatives":[
  {
    ...
    "words": [
      {
        "word":"hello",
        "start":15.259043,
        "end":15.338787,
        "confidence":0.9721591,
        "speaker":0
      },
    ...
    ]
  }
]
```

Use the [API reference](https://developers.deepgram.com/reference/pre-recorded) or the [API Playground](https://playground.deepgram.com/) to view the detailed response.

## Format Response

To improve readability, you can use a JSON processor to parse the JSON. In this example, we use [JQ](https://stedolan.github.io/jq/) and further improve readability by turning on Deepgram’s [punctuation](https://developers.deepgram.com/docs/punctuation/) and [utterances](https://developers.deepgram.com/docs/utterances/) features:

```shell
curl \
  --request POST \
  --url 'https://api.deepgram.com/v1/listen?diarize=true&punctuate=true&utterances=true' \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'content-type: audio/mp3' \
  --data-binary @Premier_broken-phone_numbers.mp3 | jq -r ".results.utterances[] | \"[Speaker:\(.speaker)] \(.transcript)\""
```

> ⚠ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

When the file is finished processing, you’ll receive the following response:

```
[Speaker:0] Hello, and thank you for calling premier phone service. Please be aware that this call may be recorded for quality and training purposes.
[Speaker:0] My name is Beth, and I will be assisting you today. How are you doing?
[Speaker:1] Not too bad. How are you today?
[Speaker:0] I'm doing well. Thank you. May I please have your name?
[Speaker:1] My name is Blake...
```

## Use Cases

An example of a use case for Diarization includes:

- Customers who have audio with multiple speakers and want to separate audio by speaker.

> ℹ By default, Deepgram applies its general AI [model](https://developers.deepgram.com/docs/model), which is a good, general purpose model for everyday situations. To learn more about the customization possible with Deepgram's API, check out the [Deepgram API Reference](https://developers.deepgram.com/api-reference/).

Updated about 2 months ago



# [Punctuation](https://developers.deepgram.com/docs/punctuation)

Punctuation adds punctuation and capitalization to your transcript.

---

`punctuate` *boolean*. Default: `false`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

> ## ℹ Using Smart Formatting?
>
> If you've set `smart_format=true` in your API request, Punctuation is automatically enabled.

## Enable Feature

To enable punctuation, use the following parameter in the query string when you call Deepgram’s `/listen` endpoint :

```
punctuate=true
```

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

Bash

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?punctuate=true'
```

![:eyes:](https://developers.deepgram.com/public/img/emojis/eyes.png) Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Results

Once applied, results will appear in the transcript.

| Truth                                                        | Before punctuate                                             | After punctuate                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| hello and thank you for calling premier services please be aware that this call may be recorded for quality training purposes my name is beth and i will be assisting you today | hello and thank you for calling premier services please be aware that this call may be recorded for quality training purposes my name is beth and i will be assisting you today | Hello, and thank you for calling Premier Services. Please be aware that this call may be recorded for quality training purposes. My name is Beth, and I will be assisting you today. |

## Use Cases

Some examples of use cases for punctuation include:

- Customers who want transcripts to be more readable.

> ## ℹ️
>
> By default, Deepgram applies its general AI [model](https://developers.deepgram.com/docs/model), which is a good, general purpose model for everyday situations. To learn more about the customization possible with Deepgram's API, check out the [Deepgram API Reference](https://developers.deepgram.com/reference/).

Updated 4 months ago



# [Utterances](https://developers.deepgram.com/docs/utterances)

Utterances segments speech into meaningful semantic units.

---

`utterances` *boolean*. Default: `false`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) Streaming [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

Deepgram’s Utterances feature allows the chosen model to interact more naturally and effectively with speakers' spontaneous speech patterns. For example, when humans speak to each other conversationally, they often pause mid-sentence to reformulate their thoughts, or stop and restart a badly-worded sentence.

> ℹ Looking for streaming support? Check out our [Endpointing](https://developers.deepgram.com/docs/endpointing) feature, which uses a Voice Activity Detector to indicate the end of speech.

## Enable Feature

To enable utterances, use the following parameter in the query string when you call Deepgram’s `/listen` endpoint :

```
utterances=true
```

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?utterances=true'
```

![:eyes:](https://developers.deepgram.com/public/img/emojis/eyes.png) Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Analyze Response

> ℹ For this example, we use a WAV audio file that contains the beginning of Abraham Lincoln’s Gettysburg Address. If you would like to follow along, you can [download it](https://res.cloudinary.com/deepgram/video/upload/v1682359638/devex/gettysburg_f1diph.wav).

When the file is finished processing, you’ll receive a JSON response. Let’s look more closely at the `utterances` object:

```json
...
"utterances":[
  {
    "start":0.41915998,
    "end":5.43012,
    "confidence":0.88172823,
    "channel":0,
    "transcript":"four score and seven years ago our fathers brought forth on this continent a new nation",
    "words":[
      {"word":"four","start":0.41915998,"end":0.85827994,"confidence":0.57893836},
 			...
    ],
    "id":"2d8211a4-3a5b-4053-8939-edf2b2b389fa"
  },
  ...
  }
]
...
```

In this response, we see that each utterance contains:

- `start`: Start time (in seconds) from the beginning of the audio stream.
- `end`: End time (in seconds) from the beginning of the audio stream.
- `confidence`: Floating point value between 0 and 1 that indicates overall transcript reliability. Larger values indicate higher confidence.
- `channel`: Audio channel to which the utterance belongs. When using multichannel audio, utterances are chronologically ordered by channel.
- `transcript`: Transcript for the audio segment being processed.
- `words`: Object containing each word in the transcript, along with its start time and end time (in seconds) from the beginning of the audio stream, and a confidence value.

> ℹ By default, Deepgram applies its general AI model, which is a good, general purpose model for everyday situations. To learn more about the customization possible with Deepgram's API, check out the [Deepgram API Reference](https://developers.deepgram.com/reference/).

## Advanced Processing

You may also want to enable speaker diarization, which will detect and identify speakers for utterances, and punctuation.

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @gettysburg.wav \
  --url 'https://api.deepgram.com/v1/listen?utterances=true&diarize=true&punctuate=true'
```

![:eyes:](https://developers.deepgram.com/public/img/emojis/eyes.png) Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

When the file is finished processing, you’ll receive a JSON response that has the same basic structure as before. Let’s take a closer look at the new `utterances` object:

```json
...
"utterances":[
  {
    "start":0.41874,
    "end":5.42518,
    "confidence":0.88211584,
    "channel":0,
    "transcript":"four score and seven years ago, our fathers brought forth on this continent a new nation",
    "words":[
      {"word":"four","start":0.41874,"end":0.85742,"confidence":0.5821198,"speaker":0,"punctuated_word":"four"},
      ...
    ],
    "speaker":0,
    "id":"ec11ce4b-2d5c-4b95-9183-ba102bea1d62"
  },
...
]
...
```

In this response, notice that the content of `transcript` in each utterance is now punctuated, and each `word` object in the `words` array contains two new parameters:

- `speaker`: Integer indicating the speaker who is saying the word being processed.
- `punctuated_word`: Word being processed with added punctuation, if any.

To improve readability, you can use a JSON processor to parse the JSON. In this example, we use [JQ](https://stedolan.github.io/jq/).

```shell
curl \
--request POST \
--header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
--header "Content-Type: audio/wav" \
--data-binary @gettysburg.wav \
--url "https://api.deepgram.com/v1/listen?utterances=true&diarize=true&punctuate=true" | jq -r '.results.utterances[] | "[Speaker:\(.speaker)] \(.transcript)"'
```

![:eyes:](https://developers.deepgram.com/public/img/emojis/eyes.png) Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

When the file is finished processing, you’ll receive the following response:

```
[Speaker:0] four score and seven years ago, our fathers brought forth on this continent a new nation
[Speaker:0] conceived liberty and dedicated to the proposition that all men are created equal.
[Speaker:0] Now we are engaged in a great civil war testing whether that nation or any nation so conceived and so dedicated can long endure. 
```

## Use Cases

Some examples of use cases for utterances include:

- Customers who would like to perform analysis on output by utterance. For example, their call center would like to track how the sentiment progresses throughout their customer calls, so they can determine whether their interactions with callers trend from negative to positive or vice versa.

Updated 4 months ago



# [Utterance Split](https://developers.deepgram.com/docs/utterance-split)

Utterance Split detects pauses between words in submitted audio. Used when the Utterances feature is enabled for pre-recorded audio.

---

`utt_split` *float*. Default: `0.8`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) Streaming [All available languages](https://developers.deepgram.com/docs/models-languages-overview)

Deepgram’s Utterance Split feature monitors incoming audio and detects when a sufficiently long pause is detected between words. By default, the length of time Deepgram uses for Utterance Split is 0.8 seconds, but you can configure this value using the `utt_split` parameter.

Utterance Split is used when the [Utterances](https://developers.deepgram.com/docs/utterances/) feature is enabled for pre-recorded audio.

## Enable Feature

To enable Utterance Split, when you call Deepgram’s API, add an `utt_split` parameter in the query string and set it to the length of time (in seconds) of silence between words after which Deepgram will decide that a new utterance should begin. The default values is 0.8 s.

```
utt_split=LENGTH-OF-TIME-IN-SECONDS
```

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client and define the utterance split value you'd wish to use:

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?utterances=true&utt_split=LENGTH-OF-TIME-IN-SECONDS'
```

![:eyes:](https://developers.deepgram.com/public/img/emojis/eyes.png) Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Results

To learn about the results, see [Utterances](https://developers.deepgram.com/docs/utterances#analyze-response).

## Use Cases

Some examples of use cases for Utterance Split include:

- Audio with speakers who pause longer while speaking than the average speaker.
- Audio with speakers who speak with shorter pauses than the average speaker.

Updated 4 months ago

