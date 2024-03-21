# Fundamentals



# [Make Your First API Request](https://developers.deepgram.com/docs/make-your-first-api-request)

Follow these steps to get started with Deepgram and make your first request.

---

## Create a Deepgram Account

Before you can use Deepgram products, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes:

- $200 in credit, which gives you access to:
  - All public [models](https://developers.deepgram.com/docs/model/)
  - Pre-recorded and [Live Streaming](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio) functionality
  - All other features of Deepgram

## Create a Deepgram API Key

To access Deepgram’s API, you'll need to [create a Deepgram API Key](https://console.deepgram.com/signup?jump=keys). Make note of your API Key; you will need it later.

## Make a Request to the API

Here are several options for trying out the Deepgram API. These examples are meant to help you make a first request to Deepgram; we encourage you to try out one of our Getting Started guides to learn more.

### Deepgram Playground

Make a request without writing any code! Head to the [Deepgram Playground](https://playground.deepgram.com/?smart_format=true&language=en&model=nova-2) to try out the API. No sign-up required!

### CURL

Run the following CURL command in your shell. Be sure to replace the `DEEPGRAM_API_KEY` with your own key.

Shell

```shell
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"url":"https://static.deepgram.com/examples/interview_speech-analytics.wav"}' \
  --url 'https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true'
```

For more examples using CURL, check out the [Transcribing Pre-Recorded Audio](https://developers.deepgram.com/docs/transcribing-pre-recorded-audio) guide.

### Deepgram SDKs

This section will help you get set up to use Deepgram's SDKs. Then you can continue on to one of the Getting Started guides, which demonstrate how to make common API requests with Deepgram's officially supported SDKs.

#### Configure Environment

We provide sample scripts throughout our documentation in the languages of our SDKs and assume you have already configured your development environment. System requirements will vary depending on the programming language you use:

- **Node.js**: node >= 14.14.37
- **Python**: python >= 3.10
- **.NET**: dotnet >= 6.0
- **GO**: Go >= 1.18

> ℹ If you get stuck at any point, help is just a click away! [Contact Support](https://developers.deepgram.com/support/).

#### Install the SDK

If you intend to use one of Deepgram's SDKs to make your request, you must install it.

Open your terminal, navigate to the location on your drive where you want to create your project, and install the Deepgram SDK.

PythonJavaScript.NETGo

```shell
# Install the Deepgram Python SDK
# https://github.com/deepgram/deepgram-python-sdk
pip install deepgram-sdk==3.*
```

#### Make a Request with the SDKs

Continue on to one of our quickstart guides where you will find language-specific code samples that show you how to make requests to Deepgram with the SDK of your choice.

- [Pre-Recorded Speech-to-Text Quickstart](https://developers.deepgram.com/docs/getting-started-with-pre-recorded-audio)
- [Streaming Speech-to-Text Quickstart](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio)
- [Audio Intelligence Quickstart](https://developers.deepgram.com/docs/audio-intelligence)

Updated about 1 month ago



# [Authenticating](https://developers.deepgram.com/docs/authenticating)

Learn how to authenticate with Deepgram's API.

---

Deepgram's API uses API keys to authenticate requests. You can view and manage your API keys in the [Deepgram Console](https://console.deepgram.com/) or through the [Deepgram API](https://developers.deepgram.com/reference/).

Your API keys grant many privileges, so be sure to keep them secure. Do not share your secret API keys in publicly accessible areas such as GitHub or client-side code.

For best results, use different API keys for testing and production. To help filter usage, you can also use different API keys for different consumers or teams at your organization.

If you still need an API key, you can [sign up to Deepgram today for free](https://console.deepgram.com/signup)!

## Authenticating with the API Key

Once you have created an API key, you can use it as credentials to call Deepgram's API.

Send requests to the API with an `Authorization` header that references your project's API key:

```text
Authorization: Token YOUR_DEEPGRAM_API_KEY
```

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests made without authentication will also fail.

## Test Request

A quick test to see if your key is validating correctly, is to make a request to the `/auth/token` endpoint on our API. This will return an `invalid credentials` error if your key is invalid, and a `JSON` response with details about your key if it's valid.

```shell
curl https://api.deepgram.com/v1/auth/token \
  -H 'Authorization: Token dc43fc74612ec2cb065315663f25c34a958aa895'
```

## Additional Keys

To create additional API keys, be sure that the API key you are using to authenticate your request has been assigned either the `administrator` role or the following permissions: `keys:read`, `keys:write`.

Make sure you are sending API requests over HTTPS. Calls made over plain HTTP will fail. API requests made without authentication will also fail.

Updated 10 months ago



# [Supported Audio Formats](https://developers.deepgram.com/docs/supported-audio-formats)

Learn about audio formats and encoding supported by Deepgram.

---

Deepgram supports over 100 different audio formats and encodings. Some of the most common audio formats and encodings we support include:

- MP3
- MP4
- MP2
- AAC
- WAV
- FLAC
- PCM
- M4A
- Ogg
- Opus
- WebM
- And more...

Because audio format is largely unconstrained, we always recommend to ensure compatibility by testing small sets of audio when first operating with new audio sources.

> ℹ For more information about audio formats and our real-time API, check out [Determining Your Audio Format for Live Streaming Audio](https://developers.deepgram.com/docs/determining-your-audio-format-for-live-streaming-audio).

If you're interested in learning about how Deepgram works with a specific format or would like more information about working with your audio, please [contact Support](https://developers.deepgram.com/support/).

Updated 3 months ago



# [Creating API Keys](https://developers.deepgram.com/docs/create-additional-api-keys)

Fundamentals of creating API keys with the Deepgram Console or the Deepgram API.

---

API keys are associated with Deepgram [Projects](https://developers.deepgram.com/docs/managing-projects), which organize all of your Deepgram resources and consist of a set of users, a set of API keys, and billing and monitoring settings.

When you create an API key, you assign it a Role, which determines which actions it can be used to perform in the associated Project. Deepgram uses a tiered system of access control to provide granular access to its endpoints. To learn more about roles, see [Working with Roles](https://developers.deepgram.com/docs/working-with-roles).

> ℹ When you sign up, we automatically create your 1st Project for you.

### Create an API key using the Deepgram Console

You must create your first API key using the [Deepgram Console](https://console.deepgram.com/signup?jump=keys). Thereafter, you can continue to add additional API keys using the Console, or you can [create additional API Keys using the Deepgram API](https://developers.deepgram.com/docs/create-additional-api-keys#create-an-api-key-using-the-deepgram-api).

1. Log in to the [Deepgram Console](https://console.deepgram.com/).

2. Locate the **Projects** drop down on the top-left, select the project to which you want to add an API Key.

3. Select **Settings**.

4. Select the **API Keys** view.

5. Select **Create a New API Key**.

6. Enter settings, and select **Create Key**:

   | Name                        | Description                                                  |
   | --------------------------- | ------------------------------------------------------------ |
   | **Friendly Name (Comment)** | Name or comment to help you identify and differentiate between your keys. |
   | **Permissions**             | Role to assign to the API Key. The API Key may perform only the actions allowed by the permissions associated with this role. To learn more about roles, see [Working with Roles](https://developers.deepgram.com/docs/working-with-roles/). |
   | **Expiration**              | Expiration date to assign to the API Key. You can enter a specific date, select a duration of time to keep the key valid, or set the key to never expire. |
   | **Tag**                     | Labels to associate with the API Key. Any requests sent using the key will also be tagged with the associated labels. Once set, tags cannot be changed. To learn more about managing multiple projects using tags, see [Using Multiple Projects](https://developers.deepgram.com/docs/using-multiple-projects/). |

7. Copy the **key secret** and save it somewhere safe, then select **Got it**. For security reasons, we won't be able to show you the key again.

### Create an API Key using the Deepgram API

Once you created your first API key using the Deepgram Console you can now use the API to create additional keys as needed.

> ℹ Refer to the API Reference [Create Key](https://developers.deepgram.com/reference/create-key) for more information.

**Example Request**

```Text
curl --request POST \
     --url https://api.deepgram.com/v1/projects/your_project_id/keys \
     --header 'Authorization: Token YOUR_TOKEN' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "comment": "a nice comment",
  "scopes": [
    "usage:read",
    "usage:write",
    "keys:write"
  ]
}
'
```

Updated 3 months ago



# Logs & Usage Data

Learn how to use Deepgram's Log and Usage features.

---

> ℹ You can obtain up to 90 days of log usage data from Deepgram. If you need log usage data for a longer period of time you can use our [Usage API ](https://developers.deepgram.com/reference/get-all-requests)to programmatically fetch usage data on an interval and store it for retrieval as needed.

# Using Console Logs & Usage

Within the [Deepgram Console](https://console.deepgram.com/) you can view your API usage and API log activity of all your requests.

### To view your Summarized Usage

> Not limited to 90 days.

1. Login to the [Deepgram Console](https://console.deepgram.com/)
2. Click on the Usage Tab in the left navigation panel.
3. On the Overview Tab, select your filter options.
4. View the results.

### To view your Logs

> Limited to 90 days.

1. Login to the [Deepgram Console](https://console.deepgram.com/)
2. Click on the Usage Tab in the left navigation panel.
3. On the Logs Tab, select your filter options.
4. View the results.

# Obtaining Usage via the API

You can use the Deepgram API to programmatically fetch usage data. Please refer to our [API documentation](https://developers.deepgram.com/reference/get-all-requests) for more details.

> ⚠ Be sure to replace the placeholder `YOUR_DEEPGRAM_API_KEY` with your actual Deepgram API Key.

### Get All Requests

Replace `YOUR_PROJECT_ID`with your Deepgram project id.

```curl
curl --request GET \
     --url 'https://api.deepgram.com/v1/projects/YOUR_PROJECT_ID/requests?start=2023-10-01&end=2023-10-05&status=succeeded' \
     --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
     --header 'accept: application/json'
```

A response will be returned as such:

```json
{   
    "page": 0,
    "limit": 1,
    "requests": [
        {
            "request_id": "a758d58d-e3ec-xxx",
            "created": "2023-10-05T22:49:03.509654Z",
            "path": "/v1/listen?-xxx",
            "api_key_id": "f54158f4-xxx-xxx",
            "response": null,
            "callback": null
        }
    ]
}
```

### Summarize Usage

> ℹ Summarized usage data is not limited to 90 days.

Replace `YOUR_PROJECT_ID`with your Deepgram project id.

```curl
curl --request GET \
     --url 'https://api.deepgram.com/v1/projects/YOUR_PROJECT_ID/usage?start=2023-10-01&end=2023-10-05' \
     --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
     --header 'accept: application/json'
```

A response will be returned:

```json
{
    "start": "2023-10-01",
    "end": "2023-10-05",
    "resolution": {
        "units": "day",
        "amount": 1
    },
    "results": [
        {
            "start": "2023-10-01",
            "end": "2023-10-01",
            "hours": 865.7331186111111,
            "total_hours": 867.6975186111111,
            "requests": 54105
        },
        {
            "start": "2023-10-02",
            "end": "2023-10-02",
            "hours": 1188.9926763888889,
            "total_hours": 1191.5563763888888,
            "requests": 56081
        },
        {
            "start": "2023-10-03",
            "end": "2023-10-03",
            "hours": 1473.9747994444444,
            "total_hours": 1477.5771794444445,
            "requests": 56456
        },
        {
            "start": "2023-10-04",
            "end": "2023-10-04",
            "hours": 999.2419933333333,
            "total_hours": 1001.2063933333334,
            "requests": 54548
        },
        {
            "start": "2023-10-05",
            "end": "2023-10-05",
            "hours": 11447.164485833333,
            "total_hours": 11449.0443075,
            "requests": 196209
        }
    ]
}
```

Updated 23 days ago