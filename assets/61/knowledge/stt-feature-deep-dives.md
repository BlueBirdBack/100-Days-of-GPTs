# Speech to Text - Feature Deep Dives



# [When To Use Multichannel and Diarization](https://developers.deepgram.com/docs/multichannel-vs-diarization)

Compare Deepgram's Multichannel and Diarization features to better understand when to use each feature.

---

When using Deepgram's API, you have access to our [Multichannel](https://developers.deepgram.com/docs/multichannel/) and [Diarization](https://developers.deepgram.com/docs/diarization/) features, which are useful in different scenarios.

## Comparing Multichannel and Diarization

Multichannel and Diarization are terms that are usually known to people who work in the field of Automatic Speech Recognition (ASR), but which may be new to you.

### Multichannel Audio

Multichannel audio is audio that has multiple separate audio channels, and the audio in each channel is distinct.

You may have heard of stereo sound, which is sound produced from two different audio channels--one channel for the left and one channel for the right--and which causes audio to sound wider and as having more depth than mono sound. Stereo sound can be multichannel sound if the left and right channels contain different audio. This could consist of one channel for voices and one for sound effects, one channel for each person's voice (for example, in a telemedicine visit between a patient and their doctor), or one channel for multiple speakers and another channel for other speakers (for example, in a podcast where multiple interviewers are on one channel and multiple guests are on a second channel).

Multichannel sound can also have more than two channels. When recording multiple people speaking (for example, on a company-wide conference call), separating different speakers' voices into individual audio channels can make it easier to focus on one speaker when reviewing the audio file.

### Diarization

Diarization is the process of separating an audio stream into segments according to speaker identity, regardless of channel. Your audio may have two speakers on one audio channel, one speaker on one audio channel and one on another, or multiple speakers on one audio channel and one speaker on multiple other channels--diarization will identify the speakers regardless of audio channel.

In short, diarization focuses on giving information about different speakers, while multichannel focuses on identifying different audio channels.

### Deepgram's Multichannel Feature

You can use Deepgram's Multichannel feature by sending `multichannel=true` in a request via the [API](https://developers.deepgram.com/reference/) or an [SDK](https://developers.deepgram.com/docs/deepgram-sdks/). When you do so, you are telling Deepgram to transcribe each audio channel independently, and Deepgram will return a response that contains separate channels for each channel from the audio:

```json
"channels": [
  {
    alternatives: [
      {
        transcript: "parker scarves how may i help you",
        confidence: ...,
        words: ...
      }
    ]
  },
  {
    alternatives: [
      {
        transcript: "i got a scarf online for my wife",
        confidence: ...,
        words: ...
      }
    ]
  }
]
```

### Deepgram's Diarization Feature

You can use Deepgram's Diarization feature by sending `diarize=true` in a request via the [API](https://developers.deepgram.com/reference/) or an [SDK](https://developers.deepgram.com/docs/deepgram-sdks/). When you do so, you are telling Deepgram that you want to know which unique person spoke each word in the transcript, and Deepgram will return a response that identifies each word as having been spoken by a different person by labelling it with a `speaker` property: `speaker: 0`, `speaker: 1`, and so on.

```json
[
  {
    alternatives: [
      {
        transcript: "parker scarves how may i help you i got a scarf online for my wife",
        confidence: 0.94873047,
        words: [
          {
            word: 'parker',
            start: 1.1770647,
            end: 1.4563681,
            confidence: 0.7792969,
            speaker: 0
          },
          {
            word: 'scarves',
            start: 1.6558706,
            end: 1.8553731,
            confidence: 0.5029297,
            speaker: 0
          },
          {
            word: 'how',
            start: 2.0548756,
            end: 2.174577,
            confidence: 0.99902344,
            speaker: 0
          },
          {
            word: 'may',
            start: 2.174577,
            end: 2.254378,
            confidence: 0.9995117,
            speaker: 0
          },
          {
            word: 'i',
            start: 2.3341792,
            end: 2.4538805,
            confidence: 0.9980469,
            speaker: 0
          },
          {
            word: 'help',
            start: 2.4538805,
            end: 2.733184,
            confidence: 1,
            speaker: 0
          },
          {
            word: 'you',
            start: 2.733184,
            end: 2.892786,
            confidence: 0.9838867,
            speaker: 0
          },
          {
            word: 'i',
            start: 4.089801,
            end: 4.209502,
            confidence: 0.54589844,
            speaker: 1
          },
          {
            word: 'got',
            start: 4.209502,
            end: 4.329204,
            confidence: 0.6279297,
            speaker: 1
          },
          {
            word: 'a',
            start: 4.329204,
            end: 4.6883082,
            confidence: 0.9580078,
            speaker: 1
          },
          {
            word: 'scarf',
            start: 4.6883082,
            end: 5.1883082,
            confidence: 0.9760742,
            speaker: 1
          },
          {
            word: 'online',
            start: 5.2469153,
            end: 5.526219,
            confidence: 0.6933594,
            speaker: 1
          },
          {
            word: 'for',
            start: 5.526219,
            end: 5.6459203,
            confidence: 0.7602539,
            speaker: 1
          },
          {
            word: 'my',
            start: 5.6459203,
            end: 5.8454227,
            confidence: 0.98876953,
            speaker: 1
          },
          {
            word: 'wife',
            start: 5.8454227,
            end: 6.044925,
            confidence: 0.7709961,
            speaker: 1
          },
```

## Combining Multichannel with Diarization

Combining Deepgram's Multichannel and Diarization features can provide very specific, useful information about the people speaking in multiple audio channels. For example, if your audio contains two audio channels with several people speaking on one channel and several other people speaking on the second channel, using Multichannel will allow you to split the audio by channel, while Diarization will allow you to identify the different people speaking on each channel.

Before you combine Multichannel and Diarization, it's important to understand how each feature works individually. Otherwise, you may have difficulty understanding your returned transcript.

For example, if your audio has two different people speaking, each on a different audio channel, using both Multichannel and Diarization will return two distinct transcripts for each channel with both speakers identified as the first speaker. Having both speakers identified as the first speaker may seem unusual, but it is correct--because only one person is speaking on each distinct audio channel, each person is the one speaker (`speaker: 0`) on their channel.

Another example: You may have an audio file that you believe is multichannel, so you expect Deepgram to return multiple different transcripts, but you receive a response that contains separate channels with identical transcripts. In this case, you may have encountered a joint stereo audio file. Sometimes, to save file space when creating or converting an audio file, multichannel audio will undergo a process that mixes the channels into one main channel. Deepgram will still identify that the audio contains two channels, but the returned transcript for each channel will be the same (all speaking parts, regardless of how many speakers the audio contains, will be combined as one transcript).

## Use Cases

To really understand when to use Multichannel and when to use Diarization, let's explore some possible scenarios.

### Two audio channels with the same person speaking on each channel

**A person is doing a sound check to see whether sound is coming from two different inputs**

```json
transcript: "hello and welcome to the sound test we're starting from the left channel then follows right channel left channel right channel left channel right channel and once again let channel know alright thank you so much listening to me and have a nice day"
```

In this scenario, because the same person is speaking on both audio channels, Diarization would not be useful. However, it could be useful to break the transcript into separate audio channels using Deepgram's Multichannel feature. If you do so, you should see the following transcript returned:

```json
"channels": [
  {
    alternatives: [
      {
        transcript: "hello and welcome to sound test we're starting from the left channel and follows left channel left channel and once again let channel know thank you so much for listening to me and have a nice day",
        confidence: 0.9472656,
        words: [Array]
      }
    ]
  },
  {
    alternatives: [
      {
        transcript: "hello and welcome to the sound test we're starting from there then follows right channel right channel right channel and once again right channel thank you so much and have a nice day",
        confidence: 0.9326172,
        words: [Array]
      }
    ]
  }
]
```

### Two audio channels with one person on each channel

**A florist is taking an order from a customer**

```json
transcript: "thank you for calling marcus flowers hello i'd like to order flowers and i think you have what i'm looking for i'd be happy to take care of your order may i have your name please",
```

In this scenario, because only one individual is on each channel, Diarization would not be useful (each speaker would be returned as `speaker: 0` since they are on separate channels). However, it could be useful to break the transcript into separate audio channels using Deepgram's Multichannel feature. If you do so, you should see the following transcript returned:

```json
"channels": [
  {
    alternatives: [
      {
        transcript: "thank you for calling marcus flowers i'd be happy to take care of your order may i have your name please",
        confidence: 0.9819336,
        words: [{
            word: 'thank',
            start: 0.94,
            end: 1.06,
            confidence: 0.99658203,
            speaker: 0
          },
          ...
          ]
      }
    ]
  },
  {
    alternatives: [
      {
        transcript: "hello i'd like to order flowers and i think you have what i'm looking for",
        confidence: 0.9916992,
        words: [{
            word: 'hello',
            start: 4.0095854,
            end: 4.049482,
            confidence: 0.9897461,
            speaker: 0
          },
          ...
          ]
      }
    ]
  }
]
```

### One audio channel with two people

**A news broadcast has multiple presenters**

```json
transcript: "from npr news this is all things considered i'm robert siegel and i'm michelle norris"
```

In this scenario, because only one audio channel exists, Multichannel will probably not provide you with enough information. However, Diarization could provide information to help you identify each person speaking. In particular, analyzing both `start` and `end` properties alongside the speaker information can help you find sections of audio where people talk over each other, which commonly occurs in natural conversation. If you use Diarization, you should see the following transcript returned:

```json
"channels": [
  {
    alternatives: [
      {
        transcript: "from npr news this is all things considered i'm robert siegel and i'm michelle norris",
        confidence: 0.9794922,
        words: [
          {
            word: 'from',
            start: 0.81824785,
            end: 0.8980769,
            confidence: 0.99658203,
            speaker: 0
          },
          {
            word: 'npr',
            start: 1.2573076,
            end: 1.3770512,
            confidence: 0.95947266,
            speaker: 0
          },
          {
            word: 'news',
            start: 1.4967948,
            end: 1.736282,
            confidence: 0.99609375,
            speaker: 0
          },
          {
            word: 'this',
            start: 1.9358547,
            end: 2.0555983,
            confidence: 0.9897461,
            speaker: 0
          },
          {
            word: 'is',
            start: 2.0555983,
            end: 2.2152565,
            confidence: 0.9814453,
            speaker: 0
          },
          {
            word: 'all',
            start: 2.2152565,
            end: 2.414829,
            confidence: 0.9902344,
            speaker: 0
          },
          {
            word: 'things',
            start: 2.414829,
            end: 2.853889,
            confidence: 0.9941406,
            speaker: 0
          },
          {
            word: 'considered',
            start: 2.853889,
            end: 3.2929487,
            confidence: 0.9785156,
            speaker: 0
          },
          {
            word: "i'm",
            start: 3.452607,
            end: 3.532436,
            confidence: 0.9863281,
            speaker: 0
          },
          {
            word: 'robert',
            start: 3.6521795,
            end: 3.8916667,
            confidence: 0.98876953,
            speaker: 0
          },
          {
            word: 'siegel',
            start: 4.01141,
            end: 4.210983,
            confidence: 0.49243164,
            speaker: 0
          },
          {
            word: 'and',
            start: 4.370641,
            end: 4.45047,
            confidence: 0.9794922,
            speaker: 1
          },
          {
            word: "i'm",
            start: 4.570214,
            end: 5.049188,
            confidence: 0.4260254,
            speaker: 1
          },
          {
            word: 'michelle',
            start: 5.049188,
            end: 5.208846,
            confidence: 0.69384766,
            speaker: 1
          },
          {
            word: 'norris',
            start: 5.32859,
            end: 5.82859,
            confidence: 0.9379883,
            speaker: 1
          },
```

### Two channels with three people on one channel and one person on the other channel

In this scenario, you could combine Multichannel and Diarization to provide useful information. Here, Multichannel would separate the transcript by audio input channels, and Diarization would help you identify which person was speaking on the first channel.

## Troubleshooting

Read on for explanations to some common scenarios that may seem unusual.

### When using both the Multichannel and Diarization features with two people, both people are marked as the same speaker

If your audio has two different people speaking, each on a different audio channel, using both Multichannel and Diarization will return two distinct transcripts for each channel with both speakers identified as the first speaker. Having both speakers identified as the first speaker may seem unusual, but it is correct--because only one person is speaking on each distinct audio channel, each person is the one speaker (`speaker: 0`) on their specific channel:

```json
"channels": [
  {
    alternatives: [
      {
        transcript: "thank you for calling marcus flowers i'd be happy to take care of your order may i have your name please",
        confidence: 0.9819336,
        words: [{
            word: 'thank',
            start: 0.94,
            end: 1.06,
            confidence: 0.99658203,
            speaker: 0
          },
          ...
          ]
      }
    ]
  },
  {
    alternatives: [
      {
        transcript: "hello i'd like to order flowers and i think you have what i'm looking for",
        confidence: 0.9916992,
        words: [{
            word: 'hello',
            start: 4.0095854,
            end: 4.049482,
            confidence: 0.9897461,
            speaker: 0
          },
          ...
          ]
      }
    ]
  }
]
```

### When using the Multichannel feature, Deepgram returns the same transcript on each channel

Sometimes when you believe an audio file is multichannel and expect Deepgram to return multiple different transcripts, you receive a response that contains separate channels with identical transcripts. In this case, you may have encountered a joint stereo audio file. Sometimes, to save file space when creating or converting an audio file, multichannel audio will undergo a process that mixes the channels into one main channel. Deepgram will still identify that the audio contains two channels, but the returned transcript for each channel will be the same (all speaking parts, regardless of how many speakers the audio contains, will be combined as one transcript):

```json
"channels": [
  {
    alternatives: [
      {
        transcript:
          'parker scarves how may i help you i got a scarf online for my wife',
        confidence: 0.9453125,
        words: [Array],
      },
    ],
  },
  {
    alternatives: [
      {
        transcript:
          'parker scarves how may i help you i got a scarf online for my wife',
        confidence: 0.9453125,
        words: [Array],
      },
    ],
  },
]
```

Updated 3 months ago



# [When To Use Keywords and Search](https://developers.deepgram.com/docs/keywords-vs-search)

Compare Deepgram's Keywords and Search features to better understand when to use each feature.

---

When using Deepgram's API, you have access to our Keywords and Search features, which are named similarly, but work in very different ways.

## Comparing Keywords and Search

Keywords are words that you would like Deepgram to pay more attention to, so it can transcribe those words more accurately. If you send a list of keywords with your request to the Deepgram API, Deepgram can better understand the context of what it is transcribing because it can train itself to better identify those words.

Search also expects you to add a word or list of words to your request to the Deepgram API. But in this case, Deepgram looks for these words in the transcription, returning a response that includes the start time and end time of any matching words it identifies.

| Keywords                                                     | Search                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Handles words that you want Deepgram to pay more attention to transcribing successfully. Providing Deepgram with a list of words gives the technology more context, so the ASR can transcribe the specified words more accurately. | Handles words that you want Deepgram to search for and provide a best guess at the start time and end time at which the word was said. |
| Cannot accept multiple-word phrases, such as "no problem", to be boosted as a unit; if you send words with URL-encoding, Deepgram will boost words individually. | Can accept multiple-word phrases, such as "no problem", but you must URL-encode the phrase. |
| Can accept up to 100 words.                                  | Can accept up to 25 words.                                   |
| Accepts multiple instances in the query string (`keywords=medicine&keywords=prescription`). | Accepts multiple instances in the query string (`search=speech&search=Friday`). |
| Does not return additional data in the response; just improves the transcription. | Returns an additional data object that contains possible matches for your search terms and identifies an estimated start and end time for each word. |

## Use Cases

To really understand when to use Keywords and when to use Search, let's explore some possible scenarios.

### Compliance

**Your company employs people in a customer service role, and they are required to say at the start of every phone call, "This call is being recorded." To ensure compliance, you want to check that they are actually saying this phrase.**

In this scenario, you can use Search to find phrases that match "This call is being recorded." Deepgram's AI will do its best to find phrases that match and will return a list of possible matches with a confidence rating.

Once you receive your results, you should analyze the data and decide for yourself which confidence rating is more likely to return an accurate match. As you practice and gain experience, you will start to see a pattern forming between confidence numbers and accurate matches.

### Discovery

**Your company is participating in litigation, and as part of the eDiscovery phase, you are tasked with producing electronic documents (including audio and video) that are relevant to the case.**

In this situation, instead of searching for a single word or phrase, you would search for language that suggests that conversation in an audio or video file is relevant to your court case. So you would use Search to point you to valuable *sections* of your audio.

Since Deepgram's Search feature returns a confidence level in the response rather than just being a yes/no check, you can analyze its results to identify a combination of words and phrases that might help you find more nuanced relevant language.

### Demos

**You are planning an important demo for the upcoming week, and you want to use Deepgram's speech-to-text API, but you haven't trained a language model yet. The demo is crucial to your business, so you want to give an added boost to Deepgram's transcription technology to improve accuracy for certain words.**

In this scenario, you can use Keywords to get a more accurate transcription without training a custom model, which would be a more powerful option. To improve the transcription, you would include a list of keywords that are more difficult for Automatic Speech Recognition (ASR) to recognize (such as jargon, names, and scientific words) in the query parameters of your request to Deepgram.

Using the Keywords feature requires practice and thoughtful implementation. The best approach is to benchmark the transcription results without any keywords, and then add words one by one to notice the effect. Until you get a feel for how the Keywords feature works with your chosen use case models and unique language context, you may find that providing keywords seems to have no effect or even lower the quality of the transcription.

This is because:

- the better Deepgram's off-the-shelf models get at transcribing on their own, the less powerful the Keywords feature becomes because Deepgram gives an increasing confidence level to the transcription itself. If you are using an extremely powerful off-the-shelf model, using keywords might not have an effect.
- the Keywords feature works differently depending on whether the provided words are 'in-vocabulary', meaning they already exist in whatever model you are using, or 'out-of-vocabulary', meaning they do not already exist in the model. (To learn more about in-vocabulary and out-of-vocabulary keywords, see [Features: Keywords](https://developers.deepgram.com/docs/keywords/#in-vocabulary--out-of-vocabulary-keywords).) If the keywords you provide are in-vocabulary (regardless of whether you are using an off-the-shelf model or your own trained model), Deepgram will place even more emphasis on them, telling the AI to boost the confidence that those words were spoken. This can affect the quality of your transcript, so adjust your boost values slowly and carefully.
- boost values for keywords are exponential. If you add really high [intensifiers](https://developers.deepgram.com/docs/keywords/#intensifiers) to your keywords, you may cause Deepgram's AI to overuse those keywords. You need to find the right balance, which comes with trial and error.
- the Keywords feature cannot boost phrases, so if you are searching for a combination of words (for example, *first name* + *last name*), each word will be boosted individually, which may result in one showing up correctly while the other does not.

Some other behaviors that can affect performance of the Keywords feature:

- Sending a very large number of keywords may affect the speed at which Deepgram is able to create a transcription. You may not be concerned about speed if you are batch-processing audio files, but you should pay special attention to speed if you are performing real-time transcription. We recommend limiting your submission to no more than 100 keywords, understanding that 100 is really pushing the limits.
- Providing out-of-vocabulary keywords can cause Deepgram to take longer to return a response.

> ⚠ The Keywords feature is still in beta at this time, so please factor this into your usage. We are actively working to improve this feature.

### Other Common Scenarios

Some other possible scenarios for the Search feature include:

- Searching captions of real-time streams or pre-recorded videos (that your product provides using Deepgram) to locate a discussed topic or point of interest.
- Searching for competitor or brand names in various types of media recordings, so you can gather information to help strategize.
- Searching for specific phrases that imply dissatisfaction (such as profanity), so you can identify and analyze situations in which customers were unhappy.

Some other possible scenarios for the Keywords feature include:

- Improving a transcription when you haven't yet had the opportunity to train a custom model but know a number of context-unique words that you can identify.
- Improving the real-time transcription of a meeting by making sure names of participants and specialized company terminology that will be used during the meeting are identified.

Updated 3 months ago

