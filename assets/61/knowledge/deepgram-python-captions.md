# [Deepgram Python Captions](https://github.com/deepgram/deepgram-python-captions)

[![Discord](https://camo.githubusercontent.com/0152dcd7530befa712f5aae5f02f968bee82bf8ad12225a132be69854e71667e/68747470733a2f2f646362616467652e76657263656c2e6170702f6170692f7365727665722f785752614344427457343f7374796c653d666c6174)](https://discord.gg/xWRaCDBtW4) [![PyPI version](https://camo.githubusercontent.com/f15bcdc814f00dc52ae7106b0484e7df84f936ca58d1f83fa069a4e780ba659e/68747470733a2f2f62616467652e667572792e696f2f70792f646565706772616d2d63617074696f6e732e737667)](https://badge.fury.io/py/deepgram-captions)

This package is the Python implementation of Deepgram's WebVTT and SRT formatting. Given a transcription, this package can return a valid string to store as WebVTT or SRT caption files.

The package is not dependent on Deepgram, but it is expected that you will provide a JSON response from a transcription request from either Deepgram or one of the other supported speech-to-text APIs.



## Installation

```sh
pip install deepgram-captions
```



## How it works

The converter takes in a JSON object response (see examples in the `./test` folder.) Depending on which API you use, the converter will turn that into a shape that can be handled by the `webvtt` and `srt` scripts.

You provide the JSON object; then select the converter needed such as `DeepgramConverter`, `WhisperTimestampedConverter`, `AssemblyAIConverter` and so on. (If the API you want to use is not supported, please reach out to `devrel@deepgram.com` and we will do our best to add it.)



## WebVTT from Deepgram Transcriptions

```python
from deepgram_captions import DeepgramConverter, webvtt

transcription = DeepgramConverter(dg_response)
captions = webvtt(transcription)
```



## SRT from Deepgram Transcriptions

```python
from deepgram_captions import DeepgramConverter, srt

transcription = DeepgramConverter(dg_response)
captions = srt(transcription)
```



### Line length

Add an optional integer parameter to set the line length of the caption.

```python
line_length = 10

deepgram = DeepgramConverter(dg_speakers)
captions = webvtt(deepgram, line_length)
```



## Other Converters

### Whisper

Open AI's Whisper (through their API) does not provide timestamps, so a JSON response directly from OpenAI cannot be used with this package. However, there are a couple other options you can try:



#### Deepgram's Whisper Cloud

Use Deepgram's fully hosted Whisper Cloud, which gives you Whisper transcriptions along with the features that come with Deepgram's API such as timestamps. Use `model=whisper` when you make your request to Deepgram. Then use the `DeepgramConverter` to create the captions.

```python
from deepgram_captions import DeepgramConverter, srt

transcription = DeepgramConverter(whisper_response)
captions = srt(transcription)
```



#### Whisper Timestamped

[Whisper Timestamped](https://github.com/linto-ai/whisper-timestamped) adds word-level timestamps to OpenAI's Whisper speech-to-text transcriptions. Word-level timestamps are required for this package to create captions, which is why we have created the captions converter for Whisper Timestamped (and not OpenAI's Whisper).

```python
from deepgram_captions import WhisperTimestampedConverter, webvtt

transcription = WhisperTimestampedConverter(whisper_response)
captions = webvtt(transcription)
```



### Assembly AI

AssemblyAI is another popular speech-to-text API.

```python
from deepgram_captions import AssemblyAIConverter, webvtt

transcription = AssemblyAIConverter(assembly_response)
captions = webvtt(transcription)
```



## Output

### Output WebVTT

When transcribing https://dpgr.am/spacewalk.wav, and running it through our library, this is the WebVTT output.

```python
from deepgram_captions.converters import DeepgramConverter
from deepgram_captions.webvtt import webvtt

transcription = DeepgramConverter(dg_response)
captions = webvtt(transcription)
print(captions)
```



This is the result:

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



## Output SRT

When transcribing https://dpgr.am/spacewalk.wav, and running it through our library, this is the SRT output.

```python
from deepgram_captions import DeepgramConverter, srt

transcription = DeepgramConverter(dg_response)
captions = srt(transcription)
print(captions)
```



This is the result:

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



## Documentation

You can learn more about the Deepgram API at [developers.deepgram.com](https://developers.deepgram.com/docs).



## Development and Contributing

Interested in contributing? We ❤️ pull requests!

To make sure our community is safe for all, be sure to review and agree to our [Code of Conduct](https://github.com/deepgram/deepgram-python-captions/blob/main/.github/CODE_OF_CONDUCT.md). Then see the [Contribution](https://github.com/deepgram/deepgram-python-captions/blob/main/.github/CONTRIBUTING.md) guidelines for more information.



## Getting Help

We love to hear from you so if you have questions, comments or find a bug in the project, let us know! You can either:

- [Open an issue in this repository](https://github.com/deepgram/[reponame]/issues/new)
- [Join the Deepgram Github Discussions Community](https://github.com/orgs/deepgram/discussions)
- [Join the Deepgram Discord Community](https://discord.gg/xWRaCDBtW4)