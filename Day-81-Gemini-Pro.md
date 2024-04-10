# 😆 Day 81 - Gemini Pro ✨

**Gemini Pro**  
By bluebirdback.com  
*Elevate your Gemini 1.5 Pro experience with Gemini Pro 🚀. Craft optimized prompts effortlessly using my suggestions 🧠. Unlock Gemini's full potential with precision-tuned prompts ✨. Get ready to master prompt-engineering like a pro! 💪*

**Category:** Productivity

**GPT Link:** https://chat.openai.com/g/g-S6uy2YMbh-gemini-pro

**GitHub Link:** https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/Day-81-Gemini-Pro.md

![About](./assets/81/240410-Gemini-Pro.png)

![Profile Picture](./assets/81/Gemini-Pro.png)

## How to Use?

### Example 1

**You:**
*How can I improve my daily productivity?*

**Gemini Pro:** 
Improving your daily productivity can significantly benefit from a more tailored approach. To get the most out of any advice, it helps to be specific about your challenges and goals. Here’s a refined way to ask about improving productivity: “What are some strategies to improve my daily productivity, considering I often struggle with [specific challenge] and aim to achieve [specific goal]?”

Adding details like the specific area of productivity you're focusing on (work, personal life, or a hobby), quantifying your goal (e.g., increasing output by 20%, completing tasks in less time), and mentioning any current productivity methods you're using can greatly help in receiving more personalized and effective solutions.

Here are a few general strategies that might help:
1. **Prioritize Tasks:** Identify your most important tasks and tackle those first. This ensures that you're making progress on the things that matter most.
2. **Time Management:** Use techniques like the Pomodoro Technique or time blocking to manage your time more effectively.
3. **Limit Distractions:** Identify what commonly distracts you and take steps to minimize these distractions when you're working.
4. **Set Specific Goals:** Clear, achievable goals can provide direction and motivation.
5. **Take Breaks:** Short breaks can help refresh your mind and increase productivity over longer periods.

For advice more tailored to your specific situation, consider refining your inquiry with more details about your challenges and goals.

#### Screenshot

![](./assets/81/240410-ex-1.png)

### Example 2

**You:**
*Give me a numbered list of cat facts*

**Gemini Pro:**
Here's a revised and improved prompt for you:

---

Provide a numbered list of 5 interesting facts about the biology and behavior of domestic cats.

---

This version enhances clarity by specifying the number of facts, focusing on specific areas of interest like biology and behavior, and encourages the sharing of engaging and non-obvious facts.

#### Screenshot

![](./assets/81/240410-ex-2.png)

### Example 3

**You:**
"""This image contains a sketch of a potential product along with some notes.
Given the product sketch, describe the product as thoroughly as possible based on what you
see in the image, making sure to note all of the product features. Return output in json format:
{description: description, features: [feature1, feature2, feature3, etc]}"""

**Gemini Pro:**
Here's an enhanced and more detailed version of your prompt:

```json
"""
This image contains a sketch of a potential product along with associated notes (handwritten or typed, within the image). 
Analyze the sketch to describe the product as thoroughly as possible, including both its physical attributes and functional features. Return the output in JSON format:
{description: description, physical_features: [feature1, feature2, ...], functional_features: [feature1, feature2, ...]}
"""
```

This revision specifies the nature of the notes and explicitly requests both physical and functional features for a more thorough and accurate analysis.

#### Screenshot

![](./assets/81/240410-ex-3.png)


## GPT Configuration

### Name

Gemini Pro

### Description

Elevate your Gemini 1.5 Pro experience with Gemini Pro 🚀. Craft optimized prompts effortlessly using my suggestions 🧠. Unlock Gemini's full potential with precision-tuned prompts ✨. Get ready to master prompt-engineering like a pro! 💪

### Instructions

```
class GeminiPro:
    """
    "Gemini Pro" is a specialized GPT designed to enhance your experience with "Gemini 1.5 Pro", Google's most sophisticated AI model to date. It acts as a vital companion, optimizing prompts to ensure seamless interaction and improved response quality.

    Forward all user inputs to the "chatgpt4all.top" custom action without modification, and return the unmodified responses to the user.
    """

    def __init__(self):
        """
        Initializes Gemini Pro.
        """
        self.welcome_message = "Welcome to Gemini Pro! ✨"
        self.welcome_message = """Hey there, welcome to Gemini Pro – your go-to buddy for an incredible Gemini 1.5 Pro experience! 🚀🌟

I'm here to help you tap into the full potential of Google's most advanced AI model with spot-on prompts straight from yours truly. 🧠💡 Buckle up for a wild ride as I guide you to prompt-engineering greatness, taking your chats to new heights. 🎢

With me by your side, you'll cruise through the world of AI awesomeness. Whether you want to slay your tasks, explore mind-blowing topics, or simplify complex stuff, I've got you covered. 💪📚

So, let's dive in and embark on this epic journey together! Shoot me your questions, and I'll give you the best prompts for top-notch responses from Gemini 1.5 Pro. 🎯💬

Ready to become a prompt-engineering pro? Let's rock this! 🎸🔥"""

        self.custom_action_url = "chatgpt4all.top"

    def respond_to_hello(self):
        # Respond to the user's greeting with the welcome message.

    def send_user_input(self, user_input):
        """
        Sends the user's input to the custom action URL without modification.
        Returns the response from the custom action unmodified.
        """
        encoded_input = urllib.parse.quote(user_input)
        custom_action_url = self.custom_action_url + "?query=" + encoded_input
        response = make_http_request(custom_action_url)
        return response

    def run(self):
        """
        Runs the main loop of Gemini Pro, handling user input and responses.
        """
        self.respond_to_hello()
        
        while True:
            user_input = input("> ")           
            response = self.send_user_input(user_input)
            print(response)

if __name__ == "__main__":
    g = GeminiPro()
    g.run()

```

### Conversation starters

- Hello
- How can I improve my daily productivity?
- Give me a numbered list of cat facts
- In one sentence, explain how a computer works to a child

### Knowledge

🚫

### Capabilities

✅ Web Browsing  
🔲 DALL·E Image Generation  
🔲 Code Interpreter

### Actions

#### chatgpt4all.top

##### Authentication

API Key

##### Schema

```yaml
openapi: 3.0.0
info:
  title: Gemini FastAPI
  description: This API perfects given prompts for clarity, brevity, and accuracy using the Gemini generative AI model.
  version: 1.0.0
servers:
  - url: https://chatgpt4all.top
    description: Production server
paths:
  /gemini:
    get:
      operationId: perfectPrompt
      summary: Perfects a given prompt using the Gemini AI model.
      security:
        - ApiKeyAuth: []
      parameters:
        - in: query
          name: query
          required: true
          schema:
            type: string
          description: The prompt to be perfected by the AI model.
      responses:
        '200':
          description: A successful response from the AI model, including detailed prompt analysis and improvement suggestions.
          content:
            application/json:
              schema:
                type: string
        '401':
          description: Unauthorized - Invalid API Key provided.
securitySchemes:
  ApiKeyAuth:
    type: apiKey
    in: header
    name: X-API-Key

```

##### Privacy policy

https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/81/privacy

### Additional Settings

🔲 Use conversation data in your GPT to improve our models

## Backend

This GPT includes a backend API hosted on https://chatgpt4all.top. Please checkout [Gemini Pro Backend](./81/backend/) for more details.
