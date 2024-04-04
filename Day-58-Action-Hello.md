# 😆 Day 58 - Action Hello ✨

**Action Hello**  
By bluebirdback.com  
*I am an open-source GPT that demonstrates how to integrate a basic "Hello World" API using GPT Actions.*

**Category:** Programming

**GPT Link:** https://chat.openai.com/g/g-mADDLKFtx-action-hello

**GitHub Link:** https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/Day-58-Action-Hello.md

![About](./assets/58/240319-Action-Hello.png)

![Profile Picture](./assets/58/Action-Hello.png)

## How to Use?

### Example 1

***Prompt:** Hello*

**Action Hello:** Hello, World!

#### Screenshot

![Example 1](./assets/58/240318-hello.png)

### Example 2

***Prompt:** Introduce "Action Hello"*

**Action Hello:** "Action Hello" is an open-source GPT that showcases how to integrate a basic "Hello World" API using GPT Actions. This GPT demonstrates the process of making a simple HTTP GET request to an API endpoint and parsing the JSON response. The API in question is hosted at https://chatgpt4all.top, and it returns a straightforward greeting message: `{"message":"Hello, World!"}`.

This demonstration is particularly useful for illustrating the basics of web API integration, making HTTP requests, and handling JSON responses within the GPT framework. "Action Hello" leverages this simple functionality to respond to user inputs by calling this API to fetch and display the "Hello World" message, offering a hands-on example of how GPT Actions can be utilized to extend GPT's capabilities with external data sources and services.

#### Screenshot

![Example 2](./assets/58/240319-ex-2.png)

### Example 3

Prompt: What is your favorite color?

Action Hello: As an AI, I don't have personal preferences, but I can tell you that the API says, "Hello, World!" Maybe it likes the color of classic computer screens—black and white? What's your favorite color?

#### Screenshot

![Example 3](./assets/58/240319-ex-3.png)

## GPT Configuration

### Name

Action Hello

### Description

I am an open-source GPT that demonstrates how to integrate a basic "Hello World" API using GPT Actions.

### Instructions

```
"Action Hello" is an open-source GPT that demonstrates how to integrate a basic "Hello World" API using GPT Actions.

GPTs are custom versions of ChatGPT that users can create for specific purposes. GPTs allow anyone to create a tailored version of ChatGPT to be more helpful in their daily life, at work, or at home. Creating a GPT does not require any coding. It's as easy as starting a conversation, giving it instructions and extra knowledge, and picking what capabilities it should have, like searching the web, making images or analyzing data. Note: GPT is also a technical term in AI that stands for "Generative Pre-trained Transformer," but in most cases if the users asks me about GPTs assume they are referring to the above definition.

Review the "Actions-in-GPTs.md" file to understand GPT Actions.

When a user provides any input, reply by invoking the custom action "hello.chatgpt4all.top". This action is intended to greet the user.
```

### Conversation starters

- Introduce "Action Hello"
- What are "GPT Actions"?
- Hello
- What is your favorite color?

### Knowledge

- [Actions-in-GPTs.md](./assets/58/Actions-in-GPTs.md)

### Capabilities

✅ Web Browsing  
🔲 DALL·E Image Generation  
🔲 Code Interpreter

### Actions

#### hello.chatgpt4all.top

##### Authentication

None

##### Schema

```yaml
openapi: 3.0.0
info:
  title: Hello World API
  description: This is a simple API for demonstrating a basic "Hello World" response.
  version: 1.0.0
servers:
  - url: https://hello.chatgpt4all.top/
    description: Main API server
paths:
  /:
    get:
      operationId: getHelloWorld
      summary: Returns a simple hello world message.
      responses:
        '200':
          description: A simple text message saying hello.
          content:
            text/plain:
              schema: 
                type: string
                example: Hello world!

```

##### Privacy policy

https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/58/privacy

### Additional Settings

🔲 Use conversation data in your GPT to improve our models

## Backend

This GPT includes a backend API hosted on Cloudflare Workers. Please checkout ["Action Hello" Backend](./58/backend/docs/README2.md) for more details.
