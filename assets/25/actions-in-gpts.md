# [Actions in GPTs](https://platform.openai.com/docs/actions/introduction/actions-in-gpts)

## [Introduction](https://platform.openai.com/docs/actions/introduction/introduction)

Learn how to build a GPT action that intelligently calls your API.

### [What is a GPT?](https://platform.openai.com/docs/actions/introduction/what-is-a-gpt)

[GPTs](https://openai.com/blog/introducing-gpts) provide the ability to deeply customize ChatGPT for specific use cases along with custom capabilities. You can create a GPT that:

- Has custom instructions which determine the way the GPT interacts with users
- Includes tools like browsing, DALL·E, and Code Interpreter
- Comes with preset starter prompts for new and returning users
- Has custom actions which allow you to connect the GPT to APIs

And more! If you want to explore what is possible, check out the deep dive on GPTs from OpenAI Developer Day 2023:

<iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/pq34V_V5j18?si=q4ZPUe-dS8Ii8YX0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" style="box-sizing: border-box; color: rgb(53, 55, 64); font-family: Söhne, helvetica, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"></iframe>

### [What is an action in a GPT?](https://platform.openai.com/docs/actions/introduction/what-is-an-action-in-a-gpt)

In addition to using our built-in capabilities (browsing, DALL·E, and Code Interpreter), you can also define custom actions by making one or more APIs available to the GPT. Actions allow GPTs to integrate external data or interact with the real-world, such as connecting GPTs to databases, plugging them into your emails, or making them your shopping assistant, all through APIs.

The design of actions builds upon insights from our plugins beta, granting developers greater control over the model and how their APIs are called. Actions are defined using the [OpenAPI specification](https://swagger.io/specification/), which is a standard for describing APIs.

### [GPT action flow](https://platform.openai.com/docs/actions/introduction/gpt-action-flow)

To build a GPT with an action, it is important to understand the end-to-end flow.

1. Create a GPT in the ChatGPT UI
   - Manually configure or use the GPT builder to create a GPT
   - Identify the API(s) you want to use
2. Go to the "Configure" tab in the GPT editor and select "Create new action"
   - You will be presented with 3 main options: selecting the authentication schema for the action, inputting the schema itself, and setting the privacy policy URL
   - The Schema follows the OpenAPI specification format (not to be confused with OpenAI) to define how the GPT can access an external API
3. Fill in the details for the schema, authentication, and privacy policy.
   - When selecting an authentication method, you will have 3 options, "None", "API Key", and "OAuth", we will explore these in depth later on
   - For the schema, you can take an existing OpenAPI specification you have for your API or create a new one. If you have already published an OpenAPI specification online, you can import it via the "Import from URL" button
   - The privacy policy URL is displayed to the user when they open a GPT and select the drop down in the top left corner showing the name of the GPT
4. Determine the visibility of your GPT
   - By default, GPTs are not accessible to everyone
   - When you go to save a GPT, you will have the option to "Publish to" a certain audience: "Only me", "Anyone with a link", or "Everyone"
     - Each of these visibility options comes with different constraints and requirements. For example the naming of a GPT has more restrictions if you share it with someone else
5. User(s) engage with your GPT
   - Depending on the visibility of your GPT, users might try it via a link you shared, or find it in the GPT store
   - If OAuth is required, users will be prompted to login during the session
   - Behind the scenes, the GPT injects the information on how you configured the GPT (including any available actions, tools, or instructions) into the context of the model
   - Each time a user makes a request, the model sees the available tools, actions, and instructions which determine how the GPT will respond to the request
   - If the user request is to check the weather in a specific location and you made a "Check weather" action available, the model will follow the OpenAPI specification you provided to send a request to that API and return the response to the user

## [Next steps](https://platform.openai.com/docs/actions/introduction/next-steps)

Now that you know the basics of how a GPT works and where actions can be used, you might want to:

- Get started building a [GPT with an action](https://platform.openai.com/docs/actions/getting-started)
- Learn how we [built the GPT builder](https://help.openai.com/en/articles/8770868-gpt-builder) itself as a custom GPT with actions
- Familiarize yourself with our [GPT polices](https://openai.com/policies/usage-policies#:~:text=or educational purposes.-,Building with ChatGPT,-Shared GPTs allow)
- Explore the [differences between GPTs and Assistants](https://help.openai.com/en/articles/8673914-gpts-vs-assistants)
- Check out the [GPT data privacy FAQ's](https://help.openai.com/en/articles/8554402-gpts-data-privacy-faqs)
- Find answers to [common GPT questions](https://help.openai.com/en/articles/8554407-gpts-faq)