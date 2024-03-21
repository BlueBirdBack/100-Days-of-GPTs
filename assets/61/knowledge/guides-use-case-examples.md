# Use Case Examples



# [Calculate Talk Time Analytics](https://developers.deepgram.com/docs/calculate-talk-time-analytics)



Analyzing the talk time of participants in a classroom, meeting, or phone
call can help you improve participant engagement, sales presentations,
and support response. Using Deepgram's Transcription API with diarization,
you can gather the data you need to make informed decisions about your
organization's interactions.

> ℹ The demo code in this guide uses an older version of our Node SDK. A new version of our SDK is now available. [A migration guide is available](https://developers.deepgram.com/docs/js-sdk-v2-to-v3-migration-guide).

## Before You Begin

The example provided is written in Node.js, and you can [find the code on GitHub](https://github.com/deepgram-devs/talk-time-analytics).

Before you run the code, you'll need to do a few things:

### Create a Deepgram Account

Before you can use Deepgram products, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes:

$200 in credit, which gives you access to:

- all base models
- pre-recorded and streaming functionality
- all features

### Create a Deepgram API Key

To access Deepgram's API, you'll need to [create a Deepgram API Key](https://developers.deepgram.com/documentation/getting-started/authentication/#create-an-api-key). Make note of your API Key; you will need it later.

## Getting Started

You can run this application by remixing it on Glitch or by running it on your local computer.

### Remix on Glitch

[Glitch](https://glitch.com/) comes with an online editor, so you'll have all the necessary tools to explore your own application instance. Actions taken in Glitch are subject to [Glitch's Terms of Service and Privacy Policy](https://glitch.com/legal) and are not covered by any Deepgram agreements.

To remix this application on Glitch, go to the following URL:

> https://glitch.com/edit/#!/remix/dg-uc-talk-time-analytics?PORT=3000

When accessing this URL in your browser, the project will be forked and deployed.

#### Configure the Settings

Your application will need to know more about you before it can run successfully. Edit the environment variables (`.env`) to reflect the settings you want to use:

- `PORT`: The port on which you want to run the application. We generally set this to port 3000.
- `DG_KEY`: The API Key you created earlier in this tutorial.

Once these variables are set, the application should run automatically.

### Run on localhost

You can also run this project on your local computer. To do so, you will need to clone the repository,
configure the settings, install the dependencies, and start the server.

#### Clone the Repository

Either clone or download the
[GitHub repository](https://github.com/deepgram-devs/talk-time-analytics) to your
local machine in a new directory:

```shell
# Clone this repo
git clone https://github.com/deepgram-devs/talk-time-analytics.git

# Move to the created directory
cd talk-time-analytics
```

#### Configure the Settings

Your application will need to know more about you before it can run. Copy the
`.env-example` file into a new file named `.env`, and edit the new file to
reflect the settings you want to use:

- `PORT`: The port on which you want to run the application. You can leave this as port 3000.
- `DG_KEY`: The API Key you created earlier in this tutorial.

#### Install the Dependencies

In the directory where you downloaded the code, run the following command to
bring in the dependencies needed for this project:

```shell
npm install
```

#### Start the Server

Now that you have configured your application and put the dependencies in place, your application
is ready to go! Run it with:

```shell
npm start
```

By default, the application runs on port 3000, which means you can access it at [http://localhost:3000](http://localhost:3000/).

## Code Walk-through

The application is an Express app that uses Chart.js to create a pie chart that displays calculated talk time. The key logic that calculates talk time lives in the `server.js` file.

### Sending Data to the Deepgram API

When a user uploads a file, we call the `requestDeepgramAPI` function. This
function calls the Deepgram API via an `https` request. The key parameter on this
request is `diarize=true`. This parameter tells the Deepgram API to recognize
speaker changes. When activated, the Deepgram API will assign a zero-based
speaker index to each word in the transcript.

```javascript
function requestDeepgramAPI({ res, filename, fileUrl, contentType, payload }) {
  try {
    const deepgram = new Deepgram(DG_KEY)
    let audioObj

    if (typeof payload === 'string') {
      audioObj = { url: fileUrl }
    } else {
      audioObj = { buffer: payload, mimetype: contentType }
    }

    const transcription = await deepgram.transcription.preRecorded(audioObj, {
      punctuate: true,
      diarize: true,
    })

    const speakers = computeSpeakingTime(transcription)
    res.render('analytics.ejs', {
      speakers,
      filename,
      fileUrl,
    })
  } catch (err) {
    error(res, err)
  }
}
```

### Calculating Talk Time

Once the response is returned from the Deepgram API, we pass the transcript
data to the `computeSpeakingTime` function. In that function, we create a
new `Map<number, number>` named `timePerSpeaker`.

The Deepgram API specifies the start, end, and duration of each word it
identifies. That information, paired with the indexed speaker returned
by the diarization feature of the API, allows us to iterate through each
word calculating the full length of time that speaker spoke.

```javascript
function computeSpeakingTime(transcript) {
	const words = transcript.results.channels[0].alternatives[0].words;

	if (words.length === 0) {
		return [];
	}

	// `timePerSpeaker` tracks speaker time. Keys
	// are speaker ID; values are speaking time.
	const timePerSpeaker = new Map();
	let wordAtLastSpeakerChange = words.shift();
	for (const word of words) {
		// If the speaker changes at this word
		if (wordAtLastSpeakerChange.speaker !== word.speaker) {
			addSpeakingTime(wordAtLastSpeakerChange.speaker, word.end - wordAtLastSpeakerChange.start, timePerSpeaker);
			wordAtLastSpeakerChange = word;
		}
	}

	const lastWord = words[words.length - 1];
	addSpeakingTime(wordAtLastSpeakerChange.speaker, lastWord.end - wordAtLastSpeakerChange.start, timePerSpeaker);

	return (
		// Convert the Map into an array
		[...timePerSpeaker.entries()]
			// Sort by speaker ID (keys of the Map)
			.sort((entryA, entryB) => entryA[0] - entryB[0])
			// Only keep the speaking times (the values of the Map)
			.map((entry) => entry[1])
	);
}

function addSpeakingTime(speaker, duration, timePerSpeaker) {
	const currentSpeakerDuration = timePerSpeaker.get(speaker) || 0;
	timePerSpeaker.set(speaker, currentSpeakerDuration + duration);
}
```

## Further Reading

- [Diarization](https://developers.deepgram.com/api-reference/transcription/#diarize-pr) in the Deepgram API reference

Updated 3 months ago



# [Transcribe Meetings in Realtime](https://developers.deepgram.com/docs/transcribe-meetings-in-realtime)



Real-time meeting transcription uses advanced voice technology for speech-to-text capture of what is discussed and decided in a meeting. With Deepgram’s API, you can add captions to live videos or display captions in real-time at conferences and events, and analyze spoken words for live content.

> ℹ The demo code in this guide uses an older version of our Node SDK. A new version of our SDK is now available. [A migration guide is available](https://developers.deepgram.com/docs/js-sdk-v2-to-v3-migration-guide).

## In This Tutorial

You will learn how to use Deepgram’s API and streaming endpoint to transcribe voice to text in real-time in a small video chat.

- [Before You Begin](https://developers.deepgram.com/docs/transcribe-meetings-in-realtime#before-you-begin): Set up your Deepgram account and API Key.
- [Getting Started](https://developers.deepgram.com/docs/transcribe-meetings-in-realtime#getting-started): Clone the repository and get the application running, or remix it on Glitch.
- [Code Walk-through](https://developers.deepgram.com/docs/transcribe-meetings-in-realtime#code-walk-through): Get a deeper understanding of how the application works.
- [Analyzing Results](https://developers.deepgram.com/docs/transcribe-meetings-in-realtime#analyzing-results): Learn about resources you might find helpful when analyzing results.

The example provided is written in Node.js, and you can [find the code on GitHub](https://github.com/deepgram-devs/video-chat).

> ⚠ This is an example application designed for use as a demonstration. We strongly discourage direct use of this code in a production environment.

## Before You Begin

Before you run the code, you'll need to do a few things:

### Create a Deepgram Account

Before you can use Deepgram products, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes:

$200 in credit, which gives you access to:

- all base models
- pre-recorded and streaming functionality
- all features

### Create a Deepgram API Key

To access Deepgram’s API, you'll need to [create a Deepgram API Key](https://developers.deepgram.com/documentation/getting-started/authentication/#create-an-api-key). Make note of your API Key; you will need it later.

## Getting started

You can run this application by remixing it on Glitch or by running it on your local computer.

### Remix on Glitch

[Glitch](https://glitch.com/) comes with an online editor, so you'll have all the necessary tools to
explore your own application instance. Actions taken in Glitch are subject to [Glitch’s Terms of Service and Privacy Policy](https://glitch.com/legal) and are not covered by any Deepgram agreements.

To remix this application on Glitch, go to the following URL:

> https://glitch.com/edit/#!/remix/dg-uc-video-chat?PORT=3000

When accessing this URL in your browser, the project will be forked and deployed.

#### Configure the Settings

Your application will need to know more about you before it can run successfully. Edit the environment variables (`.env`) to reflect the settings you want to use:

- `PORT`: The port on which you want to run the application. We generally set this to port 3000.
- `DG_KEY`: The API Key you created earlier in this tutorial.

Once these variables are set, the application should run automatically.

### Run on localhost

You can also run this project on your local computer. To do so, you will need to clone the repository,
configure the settings, install the dependencies, and start the server.

#### Clone the Repository

Either clone or download the [GitHub repository](https://github.com/deepgram-devs/video-chat) to your
local machine in a new directory:

```shell
# Clone this repo
git clone https://github.com/deepgram-devs/video-chat.git

# Move to the created directory
cd video-chat
```

#### Configure the Settings

Your application will need to know more about you before it can run. Copy the
`.env-example` file into a new file named `.env`, and edit the new file to
reflect the settings you want to use:

- `PORT`: The port on which you want to run the application. You can leave this as port 3000.
- `DG_KEY`: The API Key you created earlier in this tutorial.

#### Install the Dependencies

In the directory where you downloaded the code, run the following command to
bring in the dependencies needed for this project:

```shell
npm install
```

#### Start the Server

Now that you have configured your application and put the dependencies in place, your application
is ready to go! Run it with:

```shell
npm start
```

By default, the application runs on port 3000, which means you can access it at
[http://localhost:3000](http://localhost:3000/).

## Code Walk-through

The application is an Express app that uses `public/js/video_chat.js` to build a two-way video call using classic WebRTC technology. It uses an intermediate server (`server.js`) to establish a peer-to-peer connection between itself and another client. Your browser records your microphone using the [opus-recorder library](https://github.com/chris-rudmin/opus-recorder), then sends the audio stream to the server. In turn, the server forwards the audio stream to Deepgram’s API, using your Deepgram API Key to authenticate with the [real-time streaming endpoint](https://developers.deepgram.com/api-reference/transcription/#transcribe-live-streaming-audio). When the server receives the transcription back from the Deepgram API, it displays the transcription data in the browser. The key logic that connects to Deepgram and forwards any transcriptions it receives to the client application lives in the `server.js` file.

> ⚠ You could directly connect the browser to Deepgram API, but this would require you to disclose your Deepgram API Key to the browser. This is very insecure and we don't recommend this.

## Negotiating the Peer Connection

To negotiate the peer connection, we call the `createAndSetupPeerConnection` function in `public/js/video_chat.js`. This function works with the `setupWebRTCSignaling` function in `server.js` to set up the peer connection using WebRTC, which is a fully peer-to-peer technology for the real-time exchange of audio, video, and data.

> ## ℹ Learn More About WebRTC
>
> When using WebRTC, for two devices on different networks to locate each other, a form of discovery and media format negotiation must take place. This process is called signaling and involves both devices connecting to a third, mutually agreed-upon server. Through this third signaling server, the two devices can locate one another and exchange negotiation messages to resolve how to connect them over the internet.
>
> To negotiate the connection between them, the peers need to exchange Interactive Connectivity Establishment (ICE) candidates, each of which describes a method that the sending peer is able to use to communicate. Each peer sends candidates in the order they're discovered and keeps sending candidates until it runs out of suggestions, even if media has already started streaming.
>
> The content of the message going through the signaling server is, in effect, a black box. What matters is that when the ICE subsystem instructs you to send signaling data to the other peer, you do so, and that the other peer knows how to receive this information and deliver it to its own ICE subsystem. All you have to do is channel the information back and forth.

```javascript
function createAndSetupPeerConnection(peerSocketId, localStream, remoteVideoNode, socket, allPeerConnections) {
	// Create an RTC peer connection and add the connection to `allPeer Connections`.
	const peerConnection = new RTCPeerConnection({
		iceServers: [
			{
				urls: ["stun:stun.l.google.com:19302"],
			},
		],
	});
	allPeerConnections.set(peerSocketId, peerConnection);

	// Add the local stream as outgoing tracks to the peer connection so the
	// local stream can be sent to the peer.
	localStream.getTracks().forEach((track) => peerConnection.addTrack(track, localStream));

	// Forward ICE candidates to the peer through the socket. This is required
	// by the RTC protocol to make both clients agree on what video/audio
	// format and quality to use.
	peerConnection.onicecandidate = (event) => {
		if (event.candidate) {
			socket.emit("ice-candidate", peerSocketId, event.candidate);
		}
	};

	// Bind the incoming tracks to remoteVideoNode.srcObject, so we
	// can see the peer's stream.
	peerConnection.ontrack = (event) => {
		remoteVideoNode.srcObject = event.streams[0];
	};

	return peerConnection;
}
```

```javascript
function setupWebRTCSignaling(socket) {
	// Handle the WebRTC "signaling", which means forwarding the necessary data
	// to establish a peer-to-peer connection.
	socket.on("video-offer", (id, message) => {
		socket.to(id).emit("video-offer", socket.id, message);
	});

	socket.on("video-answer", (id, message) => {
		socket.to(id).emit("video-answer", socket.id, message);
	});

	socket.on("ice-candidate", (id, message) => {
		socket.to(id).emit("ice-candidate", socket.id, message);
	});
}
```

### Sending Data to the Deepgram API

When your browser sends the audio stream to the server, we call the `setupRealtimeTranscription` function. This function calls the Deepgram API via a `wss` request, which establishes a WebSocket over an encrypted TLS connection. Real-time streaming uses WebSockets, a communications protocol that enables full-duplex communication, which means that you can stream new audio to Deepgram at the same time the latest transcription results are streaming back to you.

When connecting to the Deepgram server, you can configure options by appending query string parameters to the URL. To learn more about available options, read [API Reference: Deepgram API](https://developers.deepgram.com/api-reference/transcription/#transcribe-live-streaming-audio).

```javascript
const { Deepgram } = require("@deepgram/sdk");
function setupRealtimeTranscription(socket, room) {
	/** The sampleRate must match what the client uses. */
	const sampleRate = 16000;

	const deepgram = new Deepgram(DG_KEY);

	const dgSocket = deepgram.transcription.live({
		punctuate: true,
	});

	/** We must receive the very first audio packet from the client because
	 * it contains some header data needed for audio decoding.
	 *
	 * Thus, we send a message to the client when the socket to Deepgram is ready,
	 * so the client knows it can start sending audio data.
	 */
	dgSocket.addListener("open", () => socket.emit("can-open-mic"));

	/**
	 * We forward the audio stream from the client's microphone to Deepgram's server.
	 */
	socket.on("microphone-stream", (stream) => {
		if (dgSocket.getReadyState() === WebSocket.OPEN) {
			dgSocket.send(stream);
		}
	});

	/** On Deepgram's server message, we forward the response back to all the
	 * clients in the room.
	 */
	dgSocket.addListener("message", (transcription) => {
		io.to(room).emit("transcript-result", socket.id, transcription);
	});

	/** We close the dsSocket when the client disconnects. */
	socket.on("disconnect", () => {
		if (dgSocket.getReadyState() === WebSocket.OPEN) {
			dgSocket.finish();
		}
	});
}
```

## Analyzing Results

When analyzing results, understand that real-time streaming returns a series of interim transcripts followed by a final transcript. To learn more about real-time streaming, see [Getting Started with Streaming Audio](https://developers.deepgram.com/documentation/getting-started/streaming/). To learn more about interim and final transcripts, see [Interim Results](https://developers.deepgram.com/documentation/features/interim-results/).

Updated 3 months ago



# [Transcribe Recorded Calls With Twilio](https://developers.deepgram.com/docs/transcribe-recorded-calls-with-twilio)



The wealth of knowledge in the conversations that happen during your sales and
support calls can be left untapped without automatic transcription. Using
Deepgram's Transcription API, you can gather the data you need to make informed
decisions about your organization's interactions.

> ℹ The demo code in this guide uses an older version of our Node SDK. A new version of our SDK is now available. [A migration guide is available](https://developers.deepgram.com/docs/js-sdk-v2-to-v3-migration-guide).

## In This Tutorial

You will see how to use the Deepgram API to calculate talk-time analytics for a
pre-recorded audio conversation:

- [Before You Begin](https://developers.deepgram.com/docs/transcribe-recorded-calls-with-twilio#before-you-begin): Set up your Deepgram account and API Key.
- [Getting Started](https://developers.deepgram.com/docs/transcribe-recorded-calls-with-twilio#getting-started): Clone the repository and get the application running, or remix it on Glitch.
- [Code Walk-through](https://developers.deepgram.com/docs/transcribe-recorded-calls-with-twilio#code-walk-through): Get a deeper understanding of how the application works.
- [Further Reading](https://developers.deepgram.com/docs/transcribe-recorded-calls-with-twilio#further-reading): Learn about other resources you might find helpful.

The example provided is written in Node.js, and you can [find the code
on GitHub](https://github.com/deepgram-devs/video-chat).

## Before You Begin

Before you run the code, you'll need to do a few things:

### Create a Deepgram Account

Before you can use Deepgram products, you'll need to [create a Deepgram account](https://console.deepgram.com/signup). Signup is free and includes:

$200 in credit, which gives you access to:

- all base models
- pre-recorded and streaming functionality
- all features

### Create a Deepgram API Key

To access Deepgram’s API, you'll need to [create a Deepgram API Key](https://console.deepgram.com/signup?jump=keys). Make note of your API Key; you will need it later.

### Gather Twilio Credentials

This application uses Twilio Voice to start a phone call that will be recorded
and transcribed. Before you can use Twilio products, you'll need to
[sign up for a Twilio account](https://twilio.com/).

To use the sample application, you'll need a Twilio Account SID
and Twilio Auth Token. These can both be found within your Twilio account
dashboard.

## Getting Started

You can run this application by remixing it on Glitch or by running it on
your local computer.

### Remix on Glitch

[Glitch](https://glitch.com/) comes with an online editor, so you'll have all the necessary tools to
explore your own application instance. Actions taken in Glitch are subject to [Glitch’s Terms of Service and Privacy Policy](https://glitch.com/legal) and are not covered by any Deepgram agreements.

To remix this application on Glitch, go to the following URL:

> https://glitch.com/edit/#!/remix/dg-uc-recorded-call-transcription

When accessing this URL in your browser, the project will be forked and deployed.

#### Configure the Settings

Your application will need to know more about you before it can run successfully. Edit the environment variables (`.env`) to reflect the settings you want to use:

- `YOUR_TWILIO_ACCOUNT_SID`: The Account SID from your Twilio Account Dashboard.
- `YOUR_TWILIO_AUTH_TOKEN`: The Auth Token from your Twilio Account Dashboard.
- `DG_KEY`: The API Key you created earlier in this tutorial.

Once these variables are set, the application should run automatically.

### Run on localhost

You can also run this project on your local computer. To do so, you will need
to clone the repository, configure the settings, install the dependencies, and
start the server.

#### Clone the Repository

Either clone or download the
[GitHub repository](https://github.com/deepgram-devs/recorded-call-transcription)
to your local machine in a new directory:

```shell
# Clone this repo
git clone https://github.com/deepgram-devs/recorded-call-transcription.git

# Move to the created directory
cd recorded-call-transcription
```

#### Configure the Settings

Your application will need to know more about you before it can run. Copy the
`.env-example` file into a new file named `.env`, and edit the new file to
reflect the settings you want to use:

- `DG_KEY`: The API Key you created earlier in this tutorial.
- `YOUR_TWILIO_ACCOUNT_SID`: The Account SID from your Twilio Account Dashboard.
- `YOUR_TWILIO_AUTH_TOKEN`: The Auth Token from your Twilio Account Dashboard.

#### Create a Virtual Environment (optional)

Create a virtual Python environment to run the server in isolation and prevent version collisions with other projects. (You can skip this part if you don't mind installing things system-wide.)

```shell
# Create the virtual environment
# (Must be run only once.)
python3 -m venv dg-twilio-ve

# Activate the virtual environment
# (Must be run every time you open a new terminal.)
source dg-twilio-ve/bin/activate
# Your prompt should start with `(dg-twilio-ve)`.

# python3 and pip3 will now run in this virtual environment.
# If you want to deactivate this environment, type `deactivate`.
```

#### Install the Dependencies

In the directory where you downloaded the code, run the following command to
bring in the dependencies needed for this project:

```shell
pip3 install -r requirements.txt
```

#### Start the Server

Now that you have configured your application and put the dependencies in place, your application
is ready to go! Run it with:

```shell
FLASK_APP=server.py FLASK_ENV=development flask run
```

## Code Walk-through

The application uses Flask to serve a website that generates a phone call to
a phone number you provide. Once the call has concluded, a recording is sent
to the Deepgram API for transcription. Once the transcription has been
returned, the website displays the results.

### Sending Recordings to the Deepgram API

When a call ends, the application calls the `/transcribe/` endpoint, passing a
URL that was provided by Twilio to the call's recording. The server then
sends that URL to Deepgram to transcribe. Once the transcription is complete,
the application returns it to the front-end as a JSON object.

Python

```python
@app.route('/transcribe/', methods=['POST'])
def transcribe() -> dict:
    body = json.loads(request.data)
    print("got request in transcribe:", body)
    print('sending recording to deepgram')
    # Submit the recording to Deepgram
    deepgram_req = requests.post(
        'https://api.deepgram.com/v1/listen?punctuate=true',
        headers={'Authorization': 'token ' + DEEPGRAM_API_KEY,
                 "content-type": "application/json"},
        json={"url": body["audio_url"]}
    )
    print('done processing request, sending deepgram response back to client',
          deepgram_req.text)
    return json.loads(deepgram_req.text)
```

Updated 3 months ago

