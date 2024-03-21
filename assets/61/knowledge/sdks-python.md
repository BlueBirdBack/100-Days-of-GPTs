# [Python SDK](https://developers.deepgram.com/docs/python-sdk)

The Deepgram Python SDK can be found at the [Python SDK](https://github.com/deepgram/deepgram-python-sdk) repository on GitHub, along with more detailed documentation about getting up and running with the SDK.

Since Deepgram's Python SDK is an officially supported SDK, Deepgram actively works to keep the SDK up-to-date with our newest features, and as it is an open source project, we highly encourage contributions and feedback from the community.

> ## 🌈
>
> For those who prefer to work from a Jupyter notebook, check out our [Python Starter Notebooks](https://developers.deepgram.com/docs/python-notebooks).

> ## ℹ️ Python Version
>
> Currently, the Deepgram Python SDK v3.x supports Python 3.10 and higher.

Updated about 1 month ago



# [Python SDK V2 to V3 Migration Guide](https://developers.deepgram.com/docs/python-sdk-v2-to-v3-migration-guide)

Migrating from Deepgram Python SDK v2 to the Deepgram Python SDK v3

---

> ℹ This guide is for users with experience using the Deepgram Python SDK v2 who want to migrate to the Deepgram Python SDK v3. This is not an end-to-end guide, but a reference for people using our existing Python SDK to migrate to our newest version.

# Notable Changes

- Significant Restructure of the Python SDK
- Improved implementation for Live Client
- Implements both Sync(/Threaded) and Async(/Await) Classes and Functions
- Verbosity Logging Levels for Troubleshooting
- WebVTT and SRT captions [published as a standalone package](https://github.com/deepgram/deepgram-python-captions)
- Custom Header and Query Parameters for API calls
- Support for future products (APIs)
- Better error handling

# Migration Guide

This migration guide focuses primarily on the Sync/Threaded classes and methods in this SDK. The Async/Await classes and methods are very similar, where the class name will be prepended with "Async" and properties prepended with "async".

For example, the Prerecorded Client for Sync/Threaded would be `Prerecorded` and the Async/Await would be `AsyncPrerecorded`.

If accessing the Pre-recorded Client from the `deepgram.listen` properties, the Sync/Threaded property would be `deepgram.listen.prerecorded` and the Async/Await would be `deepgram.listen.asyncprerecorded`.

## Installation

```powershell
pip install deepgram-sdk==3.*
```

## Initialization

Before

```python
from deepgram import Deepgram

# Your Deepgram API Key
DEEPGRAM_API_KEY = 'YOUR_DEEPGRAM_API_KEY'

# Initialize the Deepgram SDK
deepgram = Deepgram(DEEPGRAM_API_KEY)
```

After

```python
from deepgram import DeepgramClient

# Create a Deepgram client using the DEEPGRAM_API_KEY from environment variables
deepgram = DeepgramClient()
```

## Transcription: Pre-recorded

We have separated the `callback` feature into its own method. The functionality below is **not** valid with the callback feature.

### Local File Transcription

Transcribe a local file on the same filesystem as the app is running.

Before

```python
FILE = 'interview_speech-analytics.wav'

# file is local
# Open the audio file
audio = open(FILE, 'rb')

# Set the source
source = {
	'buffer': audio,
}

# Send the audio to Deepgram and get the response
response = await asyncio.create_task(
  deepgram.transcription.prerecorded(
    source,
    {
      'smart_format': "true",
      'summarize': "v2",
    }
  )
)

# Write the response to the console
print(json.dumps(response, indent=4))
```

After

```python
AUDIO_FILE = "preamble.wav"

# Call the transcribe_file method on the prerecorded class
  with open(AUDIO_FILE, "rb") as file:
  buffer_data = file.read()

payload: FileSource = {
	"buffer": buffer_data,
}

options = PrerecordedOptions(
  smart_format=True,
  summarize="v2",
)
file_response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

json = file_response.to_json()
print(f"{json}")
```

### URL File Transcription

Transcribe a remote file by sending us a publicly accessible URL to it.

Before

```python
URL = 'https://static.deepgram.com/examples/interview_speech-analytics.wav'

# Set the source
source = {
    'url': URL,
}

# Send the audio to Deepgram and get the response
response = await asyncio.create_task(
  deepgram.transcription.prerecorded(
    source,
    {
      'smart_format': "true",
      'summarize': "v2",
    }
  )
)

# Write the response to the console
print(json.dumps(response, indent=4))
```

After

```python
AUDIO_URL = {
    "url": "https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav"
}

options = PrerecordedOptions(
    smart_format=True,
    summarize="v2",
)
url_response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)

json = url_response.to_json()
print(f"{json}")
```

## Transcription: Live

The Live Client abstracts the underlying Websocket implementation from the user. This in turn only requires that you deal with higher level functions like `start()`, `write()`, `finish()` methods.

### Live Transcription

Transcribe live audio streams. Previously only Async/Await class and methods were available. As of this release, both Sync/Threaded and Await/Await classes and methods are provided, but the prefered method of performing live transcription is Sync/Threaded.

Before

```python
try:
  deepgramLive = await deepgram.transcription.live({
    'smart_format': True,
    'interim_results': False,
    'language': 'en-US',
    'model': 'nova',
  })
except Exception as e:
  print(f'Could not open socket: {e}')
  return

# Listen for the connection to close
deepgramLive.registerHandler(deepgramLive.event.CLOSE, lambda c: print(
                             f'Connection closed with code {c}.'))

# Listen for any transcripts received from Deepgram and write them to the console
deepgramLive.registerHandler(deepgramLive.event.TRANSCRIPT_RECEIVED, print)

# Listen for the connection to open and send streaming audio from the URL to Deepgram
# IMPORTANT: This is a blocking call with no way to exit except through a Cntl-C,
# IMPORTANT: disconnecting your internet, or killing the streaming (assuming you control that)
async with aiohttp.ClientSession() as session:
  async with session.get(URL) as audio:
  while True:
    data = await audio.content.readany()
    deepgramLive.send(data)

# If no data is being sent from the live stream, then break out of the loop.
if not data:
	break

# Indicate that we've finished sending data by sending the customary zero-byte message to the Deepgram streaming endpoint, and wait until we get back the final summary metadata object
await deepgramLive.finish()
```

After

```python
try:
		# define callbacks for transcription messages
    def on_message(self, result, **kwargs):
        sentence = result.channel.alternatives[0].transcript
        if len(sentence) == 0:
            return
        print(f"speaker: {sentence}")

    dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)

    # connect to websocket
    options = LiveOptions(model="nova", interim_results=False, language="en-US")
    dg_connection.start(options)

    lock_exit = threading.Lock()
    exit = False

    # define a worker thread
    def myThread():
      with httpx.stream("GET", URL) as r:
        for data in r.iter_bytes():
          lock_exit.acquire()
          if exit:
            	break
          lock_exit.release()

          dg_connection.send(data)

    # start the worker thread
    myHttp = threading.Thread(target=myThread)
    myHttp.start()

    # signal finished
    input("Press Enter to stop recording...\n\n")
    lock_exit.acquire()
    exit = True
    lock_exit.release()

    # Wait for the HTTP thread to close and join
    myHttp.join()

    # Indicate that we've finished
    dg_connection.finish()

except Exception as e:
    print(f"Could not open socket: {e}")
    return
```

## Management API

This provides a transition guide from Async/Await to Sync/Threaded Manage APIs.

...

## On-prem APIs

**[NOTICE]** The on-prem APIs has not changed since the last release, but in `v4` these APIs will likely go through a breaking change. There was only so much we could do with this release and unfortunately, these APIs failed to make the cut off.

Updated about 2 months ago



# [Pre-Recorded Audio Transcription](https://developers.deepgram.com/docs/python-sdk-pre-recorded-transcription)

The Deepgram [`Prerecorded Client`](https://github.com/deepgram/deepgram-python-sdk/tree/main/deepgram/clients/prerecorded/v1) allows you to request transcripts for pre-recorded audio. To request a transcript for a pre-recorded particular audio file, you'll use one of the following functions depending on your audio source:

- [`transcribe_file`](https://github.com/deepgram/deepgram-python-sdk/blob/main/deepgram/clients/prerecorded/v1/client.py#L157-L197)
- [`transcribe_url`](https://github.com/deepgram/deepgram-python-sdk/blob/main/deepgram/clients/prerecorded/v1/client.py#L46C9-L85)

## Pre-recorded Transcription Parameters

| Parameter | Type        | Description                                |
| --------- | ----------- | ------------------------------------------ |
| source    | Buffer, Url | Provides the source of audio to transcribe |
| options   | Object      | Parameters to filter requests. See below.  |

You can pass a Buffer or URL to a file to transcribe. Here's how to construct each:

### Sending a URL

```python
source = {'url': URL_TO_AUDIO_FILE}
```

### Sending a Buffer

Open a file and send the buffer returned. You will also need to provide the MIMETYPE of the file.

```python
with open(PATH_TO_FILE, 'rb') as audio:
  source = {'buffer': audio}
```

### Pre-recorded Transcription Options

Additional transcription options can be provided for pre-recorded transcriptions. They are provided as an object as the second parameter of the `transcription.prerecorded` function. Each of these parameters map to a feature in the Deepgram API. Reference the [features documentation](https://developers.deepgram.com/docs/features-overview) to learn what features may be appropriate for your request.

## Pre-recorded Transcription Example Request

With the source you chose above, call the `transcription.prerecorded` function and provide any additional options as an object.

```python
try:
    # STEP 1 Create a Deepgram client using the DEEPGRAM_API_KEY from environment variables
    deepgram = DeepgramClient()

    # STEP 2 Call the transcribe_url method on the prerecorded class
    options = PrerecordedOptions(
        model="nova",
        smart_format=True,
        summarize="v2",
    )
    url_response = deepgram.listen.prerecorded.v("1").transcribe_url(
        AUDIO_URL, options
    )
    print(url_response)

except Exception as e:
    print(f"Exception: {e}")
```

## Where To Find Additional Examples

The repository has a good collection of live audio transcription examples. You can find links to them in the [README](https://github.com/deepgram/deepgram-python-sdk?tab=readme-ov-file#examples). Each example below will attempt to provide different options on how you might transcribe an audio source.

- From an Audio File - [examples/prerecorded/file](https://github.com/deepgram/deepgram-python-sdk/blob/main/examples/prerecorded/file/main.py)
- From an URL - [examples/prerecorded/url](https://github.com/deepgram/deepgram-python-sdk/blob/main/examples/prerecorded/url/main.py)

Updated about 2 months ago



# [Live Streaming Audio Transcription](https://developers.deepgram.com/docs/python-sdk-streaming-transcription)

The `listen.live` class creates a websocket connection to the Deepgram API.

## Parameters

Additional options can be provided for streaming transcriptions when the websocket `start()` function is called. They are provided by delcaring a `LiveOptions` object. Each of these parameters map to a feature in the Deepgram API. Reference the [features documentation](https://developers.deepgram.com/docs/features-overview) to learn what features may be appropriate for your request.

## Declaring a Deepgram Websocket

The `listen.live` function declares a websocket object to the Deepgram API.

```python
# Create a websocket connection using the DEEPGRAM_API_KEY from environment variables
dg_connection = deepgram.listen.live.v("1")
```

## Events and Callbacks

The following events are fired by the live transcription object:

| Event      | Description                                                  | Data                                                         |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `Metadata` | Metadata (or information) regarding the websocket connection | Metadata object                                              |
| `Error`    | An error occurred with the websocket connection              | Error object                                                 |
| `Results`  | Deepgram has responded with a transcription                  | [Transcription Response](https://developers.deepgram.com/reference/pre-recorded) |

### Listening to Events

Use the `on` function to listen for events fired by the websocket object.

Listen for any transcripts to be received and receive a callback to your declared function called `on_message`.

```python
def on_message(self, result, **kwargs):
  sentence = result.channel.alternatives[0].transcript
  if len(sentence) == 0:
    return
  print(f"Transcription: {sentence}")

dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
```

Listen for any errors/exceptions and receive a callback to your declared function called `on_error`

```python
def on_error(self, error, **kwargs):
  print(f"Error: {error}")

dg_connection.on(LiveTranscriptionEvents.Error, on_error)
```

## Connecting Your Websocket

After you have declared your callbacks, declare the `LiveOptions` or the transcription parameters you want to use for your websocket connection. These options are passed into the `start()` function, which will subsequently connect the websocket to the Deepgram API.

Please note that options can be declared in `LiveOptions`, such as `interim_results`, `language`, etc can be found XXX are passed in as key/value pairs.

```python
options = LiveOptions(
  punctuate=True,
  interim_results=False,
  language='en-GB'
)

dg_connection.start(options)
```

## Functions

There are several functions that the Deepgram websocket class provides to make using the Deepgram API easier. The most notable ones are `send` and `finish`.

### Sending Audio Stream Bytes

The `send` function sends raw audio data to the Deepgram API.

```python
dg_connection.send(SOME_STREAMING_DATA)
```

When transcription results are available, you will receive those messages via the callback function previously mentioned (as seen below).

```python
def on_message(self, result, **kwargs):
  sentence = result.channel.alternatives[0].transcript
  if len(sentence) == 0:
    return
  print(f"Transcription: {sentence}")

dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
```

### Closing the Connection

The `finish` function closes the Websocket connection to Deepgram.

```python
dg_connection.finish()
```

## Where To Find Additional Examples

The repository has a good collection of live audio transcription examples. You can find links to them in the [README](https://github.com/deepgram/deepgram-python-sdk?tab=readme-ov-file#examples). Each example below will attempt to provide different options on how you might transcribe a live-streaming source.

- From a Microphone - [examples/streaming/microphone](https://github.com/deepgram/deepgram-python-sdk/blob/main/examples/streaming/microphone/main.py)
- From a HTTP Endpoint - [examples/streaming/http](https://github.com/deepgram/deepgram-python-sdk/blob/main/examples/streaming/http/main.py)

Updated about 2 months ago



# [Python Notebooks](https://developers.deepgram.com/docs/python-notebooks)

Some users prefer the workflow of a Jupyter notebook. These Python starter notebooks can help those users get up and running quickly with Deepgram's Python SDK without having to copy or paste any code.

- [Prerecorded Audio Notebook](https://github.com/deepgram-devs/prerecorded-audio-notebook)
- [Livestream Audio Notebook](https://github.com/deepgram-devs/livestream-audio-notebook)

Updated 14 days ago



