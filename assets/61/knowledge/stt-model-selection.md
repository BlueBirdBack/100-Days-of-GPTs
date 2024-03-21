# Speech to Text - Model Selection



# [Models & Languages Overview](https://developers.deepgram.com/docs/models-languages-overview)

An overview of Deepgram's speech-to-text models and supported languages.

---

![Deepgram model evolution over time. Benchmarked in 2023.](https://files.readme.io/f96ccf9-image.png)

Deepgram model evolution over time. Benchmarked in 2023.

## Nova-2

> ℹ Recommended for readability and Deepgram's lowest word error rates. Recommended for most use cases.

Nova-2 expands on Nova-1's advancements with speech-specific optimizations to the underlying Transformer architecture, advanced data curation techniques, and a multi-stage training methodology. These changes yield reduced word error rate (WER) and enhancements to entity recognition (i.e. proper nouns, alphanumerics, etc.), punctuation, and capitalization.

[See the benchmarks](https://deepgram.com/learn/nova-2-speech-to-text-api).

**Examples**

The Nova-2 models can be called with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=nova-2
```

You can also call Nova-2 use case models with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=nova-2-phonecall
```

| Model                        | Language                                                     |
| :--------------------------- | :----------------------------------------------------------- |
| `nova-2` or `nova-2-general` | Czech: `cs` Danish: `da`, `da-DK` Dutch: `nl` English: `en`, `en-US`, `en-AU`, `en-GB`, `en-NZ`, `en-IN` Flemish: `nl-BE` French: `fr`, `fr-CA` German: `de` German (Switzerland):`de-CH` Greek: `el` Hindi: `hi`, `hi-Latn` Indonesian: `id` Japanese: `ja` Italian: `it` Korean: `ko`, `ko-KR` Norwegian: `no` Polish: `pl` Portuguese: `pt`, `pt-BR` Russian: `ru` Spanish: `es`, `es-419` Swedish: `sv`, `sv-SE` Turkish: `tr` Ukrainian: `uk` |
| `nova-2-meeting`             | English: `en`, `en-US`                                       |
| `nova-2-phonecall`           | English: `en`, `en-US`                                       |
| `nova-2-finance`             | English: `en`, `en-US`                                       |
| `nova-2-conversationalai`    | English: `en`, `en-US`                                       |
| `nova-2-voicemail`           | English: `en`, `en-US`                                       |
| `nova-2-video`               | English: `en`, `en-US`                                       |
| `nova-2-medical`             | English: `en`, `en-US`                                       |
| `nova-2-drivethru`           | English: `en`, `en-US`                                       |
| `nova-2-automotive`          | English: `en`, `en-US`                                       |
| `nova-2-<CUSTOM>`            | All available                                                |

## Nova

> ℹ Recommended for readability and low word error rates.

Nova is the predecessor to Nova-2. Training on this model spans over 100 domains and 47 billion tokens, making it the deepest-trained automatic speech recognition (ASR) model to date. Nova doesn't just excel in one specific domain — it is ideal for a wide array of voice applications that require high accuracy in diverse contexts. [See the benchmarks](https://deepgram.com/learn/nova-speech-to-text-whisper-api).

**Examples**

The Nova models can be called with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=nova
```

You can also call Nova use case models with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=nova-phonecall
```

| Model                    | Language                                                     |
| :----------------------- | :----------------------------------------------------------- |
| `nova` or `nova-general` | English: `en`, `en-US`, `en-AU`, `en-GB`, `en-NZ`, `en-IN` Spanish: `es`, `es-419` |
| `nova-phonecall`         | English: `en`, `en-US`                                       |
| `nova-medical`           | English: `en`, `en-US`                                       |
| `nova-<CUSTOM>`          | All available                                                |

## Enhanced

> ℹ Recommended for lower word error rates than Base, high accuracy timestamps, and use cases that require [keyword boosting](https://developers.deepgram.com/docs/keywords).

**Examples**

The Enhanced models can be called with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=enhanced
```

You can also call Enhanced use case models with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=enhanced-phonecall
```

| Model                            | Language                                                     |
| :------------------------------- | :----------------------------------------------------------- |
| `enhanced` or `enhanced-general` | Danish: `da` Dutch: `nl` English: `en`, `en-US` Flemish: `nl` French: `fr`, `fr-CA` German: `de` Hindi: `hi` Italian: `it` Japanese: `ja` Korean: `ko` Norwegian: `no` Polish: `pl` Portuguese: `pt`, `pt-BR` Spanish: `es`, `es-419`, `es-LATAM` Swedish: `sv` Tamasheq: `taq` Tamil: `ta` |
| `enhanced-meeting`               | English: `en`, `en-US`                                       |
| `enhanced-phonecall`             | English: `en`, `en-US`                                       |
| `enhanced-finance`               | English: `en`, `en-US`                                       |
| `enhanced-<CUSTOM>`              | All available                                                |

## Base

> ℹ Recommended for large transcription volumes and high accuracy timestamps.

**Examples**

The Base models can be called with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=base
```

You can also call Base use case models with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=base-phonecall
```

| Model               | Language                                                     |
| :------------------ | :----------------------------------------------------------- |
| `base` or `general` | Chinese: `zh`, `zh-CN`, `zh-TW` Danish: `da` Dutch: `nl` English: `en`, `en-US` Flemish: `nl` French: `fr`, `fr-CA` German: `de` Hindi: `hi`, `hi-Latn` Indonesian: `id` Italian: `it` Japanese: `ja` Korean: `ko` Norwegian: `no` Polish: `pl` Portuguese: `pt`, `pt-BR` Russian: `ru` Spanish: `es`, `es-419`, `es-LATAM` Swedish: `sv` Tamasheq: `taq` Turkish: `tr` Ukrainian: `uk` |
| `meeting`           | English: `en`, `en-US`                                       |
| `phonecall`         | English: `en`, `en-US`                                       |
| `finance`           | English: `en`, `en-US`                                       |
| `conversationalai`  | English: `en`, `en-US`                                       |
| `voicemail`         | English: `en`, `en-US`                                       |
| `video`             | English: `en`, `en-US`                                       |
| `base-<CUSTOM>`     | All available                                                |

## Deepgram Whisper Cloud

> ℹ Whisper models are less scalable than all other Deepgram models due to their inherent model architecture. All non-Whisper models will return results faster and scale to higher load.

Deepgram Whisper Cloud is a fully managed API that gives you access to Deepgram’s version of OpenAI’s Whisper model. Read our guide [Deepgram Whisper Cloud](https://developers.deepgram.com/docs/deepgram-whisper-cloud) for a deeper dive into this offering.

- Additional rate limits apply to Whisper due to poor scalability.
- Requests to Whisper are limited to 15 concurrent requests with a paid plan and 5 concurrent requests with the pay-as-you-go plan.
- Long audio files are supported up to a maximum of 20 minutes of processing time (the maximum length of the audio depends on the size of the Whisper model).

Deepgram's Whisper Cloud models can be called with the following syntax:

```text
https://api.deepgram.com/v1/listen?model=whisper
```

```text
https://api.deepgram.com/v1/listen?model=whisper-SIZE
```

| Model                         | Language                                                     |
| :---------------------------- | :----------------------------------------------------------- |
| `whisper-tiny`                | [See available](https://developers.deepgram.com/docs/deepgram-whisper-cloud#supported-languages) |
| `whisper-base`                | [See available](https://developers.deepgram.com/docs/deepgram-whisper-cloud#supported-languages) |
| `whisper-small`               | [See available](https://developers.deepgram.com/docs/deepgram-whisper-cloud#supported-languages) |
| `whisper-medium` OR `whisper` | [See available](https://developers.deepgram.com/docs/deepgram-whisper-cloud#supported-languages) |
| `whisper-large`               | [See available](https://developers.deepgram.com/docs/deepgram-whisper-cloud#supported-languages) |

Updated 14 days ago



# [Language](https://developers.deepgram.com/docs/language)

Language allows you to supply a BCP-47 language tag that specifies the primary spoken language of submitted audio.

---

`language` *string*. Default: `en`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio)

## Enable Feature

To enable Language, when you call Deepgram’s API, add a `language` parameter in the query string and set it to the language you would like to recognize:

```
language=OPTION
```

> ℹ For a full list of languages and compatible models see our [Model & Language Overview](https://developers.deepgram.com/docs/models-languages-overview).

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```sh
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?language=OPTION'
```

> ℹ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Results

Once the language option is applied, results will appear in the transcript.

## Use Cases

Some examples of use cases for Language include:

- Customers with employees who live in regions with specific dialects or accents.
- Customers who need to ensure a specific language in their dataset is transcribed.

Updated 3 months ago



# Language Detection

Language Detection identifies the dominant language spoken in submitted audio.

---

`detect_language` *boolean*. Default: `false`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) ~~Streaming~~

Deepgram’s Language Detection feature identifies the dominant language spoken in submitted audio, transcribes the audio in the identified language, and returns the detected language code in the JSON response.

If you are submitting multichannel audio, Language Detection identifies one language per channel. Language Detection is supported for the following languages:

- Spanish - `es`
- English - `en`
- Hindi - `hi`
- Japanese - `ja`
- Russian - `ru`
- Ukrainian - `uk`
- Swedish - `sv`
- Chinese - `zh`
- Portuguese - `pt`
- Dutch - `nl`
- Turkish - `tr`
- French - `fr`
- German - `de`
- Indonesian - `id`
- Korean - `ko`
- Italian - `it`

## Enable Feature

To enable Language Detection, when you call Deepgram’s API, add a `detect_language` parameter set to `true` in the query string:

```
detect_language=true
```

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?model=nova-2-general&detect_language=true'
```

> ⚠ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Analyze Response

When the file is finished processing (often after only a few seconds), you’ll receive a JSON response that has the following basic structure:

```json
{
  "metadata": {
    "transaction_key": "string",
    "request_id": "string",
    "sha256": "string",
    "created": "string",
    "duration": 0,
    "channels": 0
  },
  "results": {
    "channels": [
      {
        "alternatives":[],
        "detected_language": "fr",
        "language_confidence": 0.0
      }
    ]
  }
```

In this response, we see that each channel contains:

- `alternatives` object, which contains:
  - `transcript`: Transcript for the audio being processed.
  - `confidence`: Floating point value between 0 and 1 that indicates overall transcript reliability. Larger values indicate higher confidence.
  - `words`: Object containing each word in the transcript, along with its start time and end time (in seconds) from the beginning of the audio stream, a word confidence value, a speaker identifier, and a speaker confidence value.

- `detected_language`: [BCP-47](https://tools.ietf.org/html/bcp47) language tag for the dominant language identified in the channel.

- `language_confidence`: Floating point value between 0 and 1 that indicates the confidence of the language selection (see below for important details). `language_confidence` is not supported for Whisper models and will not be included in the API response for Whisper requests.

## Advanced Functionality

### Model Selection

If you specify both `detect_language=true` and a `model` in your query parameter, Deepgram will attempt to use the specified model for the language that is detected. However, if the detected language is not available for that model, Deepgram will automatically select the next highest model to complete the request.

To use the best Deepgram model available, use `model=nova-2-general&detect_language=true`. The order of preference will be Nova-2 -> Nova-1 -> Enhanced -> Base.

For example, you may send an ASR request with the parameters `detect_language=true&model=nova-2-general`. If the detected language is supported by Base and Enhanced models, but not a Nova-2 model, Deepgram will process the request with the Enhanced model since that is the next highest model available for that language.

### Interaction with `language` query parameter

If the `language` query parameter is set and `detect_language=true` is also present, the language detected by Deepgram will be used for inference instead of the language specified in the `language` parameter.

### Restricting the detectable languages

You can restrict the possible set of detectable languages. This is useful if, for example, you know your audio files only contain English or Spanish audio. To restrict the possible set of detectable languages, use a multivalued query parameter with the language codes as the values. For example, `detect_language=en&detect_language=es` will choose either English or Spanish as the detected language.

### How to use `language_confidence`

> ⚠ `language_confidence` is not supported when using Whisper models.

Deepgram outputs a `language_confidence` score that ranges between 0 and 1 with higher values indicating more confidence in the selected language.

The `language_confidence` score can be used as a metric to determine whether the transcript is accurate. For example, if the `language_confidence` falls below a certain threshold, you may want to default to another language or reject the transcript.

It is critical to know that the `language_confidence` score only takes into account the 16 supported languages. If the audio is in a language not supported by language detection, the value of `language_confidence` should be ignored.

## Use Cases

An example of a use case for Language Detection includes:

Customers with input audio files in different languages who need to automatically detect the dominant language in the audio data and transcribe the output in the detected language.

Updated 3 months ago



# [Model](https://developers.deepgram.com/docs/model)

Model allows you to supply a model to use to process submitted audio.

---

`model` *string*. Default: `base-general`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio)

Deepgram’s Model feature allows you to supply a model to use when processing submitted audio. To learn more about the pricing for our different models, see [Deepgram Pricing & Plans](https://deepgram.com/pricing/).

## Models & Model Options

Below are a list of all model and model options that can be used with the Deepgram API.

> ⚠ The concept of Tiers is now deprecated but still available in the Deepgram API. Please see our documentation on [Tiers](https://developers.deepgram.com/docs/tier) for how they still can be used.

### Nova-2

**Examples**

```text
https://api.deepgram.com/v1/listen?model=nova-2
```

```text
https://api.deepgram.com/v1/listen?model=nova-2-phonecall
```

Nova-2 expands on Nova-1's advancements with speech-specific optimizations to the underlying Transformer architecture, advanced data curation techniques, and a multi-stage training methodology. These changes yield reduced word error rate (WER) and enhancements to entity recognition (i.e. proper nouns, alphanumerics, etc.), punctuation, and capitalization.

> ℹ Nova-2 has the following model options which can be called by using the following syntax: `model=nova-2-option`

- `general`: Optimized for everyday audio processing.
- `meeting`: Optimized for conference room settings, which include multiple speakers with a single microphone.
- `phonecall`: Optimized for low-bandwidth audio phone calls.
- `voicemail`: Optimized for low-bandwidth audio clips with a single speaker. Derived from the phonecall model.
- `finance`: Optimized for multiple speakers with varying audio quality, such as might be found on a typical earnings call. Vocabulary is heavily finance oriented.
- `conversationalai`: Optimized for use cases in which a human is talking to an automated bot, such as IVR, a voice assistant, or an automated kiosk.
- `video`: Optimized for audio sourced from videos.
- `medical`: Optimized for audio with medical oriented vocabulary.
- `drivethru`: Optimized for audio sources from drivethrus.
- `automotive`: Optimized for audio with automative oriented vocabulary.

### Nova

**Examples**

```text
https://api.deepgram.com/v1/listen?model=nova
```

```text
https://api.deepgram.com/v1/listen?model=nova-phonecall
```

Nova is the predecessor to Nova-2. Training on this model spans over 100 domains and 47 billion tokens, making it the deepest-trained automatic speech recognition (ASR) model to date. Nova doesn't just excel in one specific domain — it is ideal for a wide array of voice applications that require high accuracy in diverse contexts.

> ℹ Nova has the following model options which can be called by using the following syntax: `model=nova-option`

- `general`: Optimized for everyday audio processing. Likely to be more accurate than any region-specific Base model for the language for which it is enabled. If you aren't sure which model to select, start here.
- `phonecall`: Optimized for low-bandwidth audio phone calls.

### Enhanced

**Examples**

```text
https://api.deepgram.com/v1/listen?model=enhanced
```

```text
https://api.deepgram.com/v1/listen?model=enhanced-phonecall
```

Enhanced models are still some of our most powerful ASR models; they generally have higher accuracy and better word recognition than our base models, and they handle uncommon words significantly better.

> ℹ Enhanced has the following model options which can be called by using the following syntax: `model=enhanced-option`

- `general`: Optimized for everyday audio processing. Likely to be more accurate than any region-specific Base model for the language for which it is enabled. If you aren't sure which model to select, start here.
- `meeting` *beta*: Optimized for conference room settings, which include multiple speakers with a single microphone.
- `phonecall`: Optimized for low-bandwidth audio phone calls.
- `finance` *beta*: Optimized for multiple speakers with varying audio quality, such as might be found on a typical earnings call. Vocabulary is heavily finance oriented.

The Enhanced models can be called with the following syntax:

### Base

**Examples**

```text
https://api.deepgram.com/v1/listen?model=base
```

```text
https://api.deepgram.com/v1/listen?model=base-phonecall
```

Base models are built on our signature end-to-end deep learning speech model architecture. They offer a solid combination of accuracy and cost effectiveness in some cases.

> ℹ Base has the following model options which can be called by using the following syntax: `model=base-option`

- `general`: (Default) Optimized for everyday audio processing.
- `meeting`: Optimized for conference room settings, which include multiple speakers with a single microphone.
- `phonecall`: Optimized for low-bandwidth audio phone calls.
- `voicemail`: Optimized for low-bandwidth audio clips with a single speaker. Derived from the phonecall model.
- `finance`: Optimized for multiple speakers with varying audio quality, such as might be found on a typical earnings call. Vocabulary is heavily finance oriented.
- `conversationalai`: Optimized for use cases in which a human is talking to an automated bot, such as IVR, a voice assistant, or an automated kiosk.
- `video`: Optimized for audio sourced from videos.

### Custom

You may also use a custom, trained model associated with your account by including its `custom_id`.

> ℹ Custom models are only available to Enterprise customers. See [Deepgram Pricing & Plans](https://deepgram.com/pricing/) for more details.

### Whisper

**Examples**

```text
https://api.deepgram.com/v1/listen?model=whisper
```

```text
https://api.deepgram.com/v1/listen?model=whisper-SIZE
```

> ⚠ Whisper models are less scalable than all other Deepgram models due to their inherent model architecture. All non-Whisper models will return results faster and scale to higher load.

Deepgram's Whisper Cloud is a fully managed API that gives you access to Deepgram's version of OpenAI’s Whisper model. Read our guide [Deepgram Whisper Cloud](https://developers.deepgram.com/docs/deepgram-whisper-cloud) for a deeper dive into this offering.

Deepgram's Whisper models have the following size options:

- `tiny`: Contains 39 M parameters. The smallest model available.
- `base`: Contains 74 M parameters.
- `small`: Contains 244 M parameters.
- `medium`: Contains 769 M parameters. The default model if you don't specify a size.
- `large`: Contains 1550 M parameters. The largest model available. Defaults to OpenAI’s Whisper large-v2.

> ⚠ Additional rate limits apply to Whisper due to poor scalability. Requests to Whisper are limited to 15 concurrent requests with a paid plan and 5 concurrent requests with the pay-as-you-go plan. Long audio files are supported up to a maximum of 20 minutes of processing time (the maximum length of the audio depends on the size of the Whisper model).

## Try it out

To transcribe audio from a file on your computer using a particular model, run the following curl command in a terminal or your favorite API client.

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?model=OPTION'
```

> ℹ Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

Updated 3 months ago



# [Version](https://developers.deepgram.com/docs/version)

Version allows you to specify the version of the model you want to use to process your submitted audio.

---

`version` *string*. Default: `latest`

[Pre-recorded](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio) [Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio)

Deepgram’s Version feature allows you to specify the version of the model you want to use to process your submitted audio.

## Enable Feature

To enable Version, when you call Deepgram’s API, add a `version` parameter in the query string and set it to the version of the model you want to use to process your submitted audio.

```
version=MODEL_VERSION
```

## Use the Latest Version

To use the latest version of your selected model, send `latest` in the `version` parameter:

```
version=latest
```

## Use an Earlier Version of a Standard Model

To use an earlier version of a selected Deepgram standard model, send the version number in the `version` parameter:

```
version=VERSION_NUMBER
```

**Example:**
`version=2021-03-17.0`

You can locate version numbers of Deepgram standard models in [our changelog](https://deepgram.com/changelog/). Select **Speech Model** to filter the updates.

## Use a Specific Version of a Custom Trained Model

To use a specific version of a custom model associated with your account, send the custom model's `version_id` in the `version` parameter:

```
version=VERSION_ID
```

**Example:**
`version=12345678-1234-1234-1234-1234567890ab`

## Get Early Access to an Updated Standard Model

When we release updated versions of Deepgram standard models, you may be able to try them out and provide feedback. To do so, send the version name of the selected model in the `version` parameter:

```
version=VERSION_NAME
```

**Example:**
`version=beta`

To learn about updated model availability and get relevant version names, [contact Support](https://developers.deepgram.com/support).

## Use Cases

Examples of use cases for Version include:

- Customers who want to make sure they are using the latest version of a given model.
- Customers who want to use an earlier version of Deepgram standard model.
- Customer who want to use a specific version of a custom model associated with their account.
- Customers who would like to receive early access to an updated Deepgram standard model.

Updated 4 months ago
