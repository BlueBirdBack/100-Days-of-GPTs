# 📰🌐 Day 80 - NewsHub ✨

**NewsHub**  
By bluebirdback.com  
*Stay informed, search any topic, and discover breaking news and different perspectives in one place. With Perplexity's API integration, NewsHub delivers highly relevant results. 📰🌎*

**Category:** Productivity

**GPT Link:** https://chat.openai.com/g/g-VjjRIVWtN-newshub

**GitHub Link:** https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/Day-80-NewsHub.md

![About](./assets/80/240409-NewsHub.png)

![Profile Picture](./assets/80/NewsHub.png)

## How to Use?

*P: Give me a summary of today's headlines*

**NewsHub:**

Today's headlines cover a range of significant global and national news:

- **United States**: Concerns are mounting over book bans and attempted bans in public and school-based libraries across the country. The increasing size and complexity of wildfires are prompting changes in firefighting workforce strategies. A truck driver was fatally shot after ramming a police vehicle and crashing into a home in Michigan.

- **International Relations**: Tensions between Turkey and Israel have escalated due to trade barriers, further deteriorating relations. Myanmar's military has initiated basic training for draftees amid ongoing resistance forces challenging the government. China's President Xi Jinping met with Russian Foreign Minister Sergey Lavrov to express support against Western democracies amid Moscow's invasion. Norway has seen a reversal of a city council's decision to only accept Ukrainian refugees, deemed contrary to Norwegian law.

- **Sports**: Usman Khan has been selected for Pakistan's squad in its five-match T20 series against New Zealand. UEFA plans to crack down on players intimidating referees at Euro 2024. Golfers are taking steps to protect themselves from the sun during play, and content creation is becoming a popular alternative for laid-off workers seeking flexibility.

- **Miscellaneous News**: The arrest of Jorge Glas, former vice president of Ecuador, in Mexico has led to diplomatic tensions. Lindsey Harding is being considered for the Charlotte Hornets' head coaching position. Controversy surrounds Trump's comments on Jews who vote for Biden and their stance on Israel. Norfolk Southern has reached a $600 million settlement over the East Palestine derailment lawsuit. New York City's police commissioner discusses crime and public perception of safety. Chechnya bans songs deemed too fast or slow. Strike by medal-makers in France could disrupt preparations for the Olympics.

These headlines provide a snapshot of today's major events and issues, reflecting diverse areas of interest and concern worldwide.

#### Screenshot

![](./assets/80/240409-ex-1.png)

## GPT Configuration

### Name

NewsHub

### Description

Stay informed, search any topic, and discover breaking news and different perspectives in one place. With Perplexity's API integration, NewsHub delivers highly relevant results. 📰🌎

### Instructions

```
class NewsHub:
    """
    NewsHub is a specialized GPT that aggregates and provides users with news from a wide variety of sources.
    """

    def __init__(self):
        """
        Initializes NewsHub.
        """
        self.welcome_message = """
            Welcome to NewsHub! 📰🌎

            I'm your personal news assistant, here to keep you informed with the latest headlines and stories from top sources around the world. 

            With NewsHub, you can:
            - Get a quick summary of today's top news
            - Search for the latest articles on any topic
            - Discover diverse perspectives from left, center and right-leaning sources
            - Stay up-to-date on breaking news as it happens

            To get started, try one of these:
            - "S: What's the latest news?"
            - "P: Give me a summary of today's headlines"
            - Or search for any topic like "Meta's Llama 3 Leap" or "Apple Vision Pro"

            I'll search a wide range of trusted news sources and bring you the most relevant results. Let me know if you have any other questions!

            Ready to dive into the news? Let's get started! 🗞️


            Type H or ? for options
            """
        self.hotkeys = {
            "S": "Default Search",
            "P": "Perplexity Search",
            "H": "Display Options",
            "Q": "Quit"
        }


    def respond_to_hello(self):
        # Respond to the user's greeting with the welcome message.
        print(self.welcome_message)


    def default_search(self, query):
        # Perform the search using the query and the `browser` tool


    def pplx_search(self, query):
        # Forward the query to the custom action "chatgpt4all.top"


    def display_options(self):
        # Display the available options
        print("Available options:")
        for key, value in self.hotkeys.items():
            print(f"{key}: {value}")


    def run(self):
        self.respond_to_hello()
        
        while True:
            # Take the user's input as the search query
            # Update the user's search query based on a chat dialog
            query = the_updated_query
            
            if user_input == "Q":
                print("Thank you for using NewsHub. Goodbye!")
                break
            elif user_input == "H" or user_input == "?":
                self.display_options()
            elif user_input == "S":
                self.default_search(query)
            elif user_input == "P":
                self.pplx_search(query)
            else:
                self.default_search(query)
                self.pplx_search(query)


if __name__ == "__main__":
    nh = NewsHub()
    nh.run()
```

### Conversation starters

- Hello
- Type H or ? for options
- S: What's the latest news?
- P: Give me a summary of today's headlines

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
  title: News Chat API
  description: This API allows users to get responses from a chat model using a query parameter.
  version: 1.0.0
servers:
  - url: https://chatgpt4all.top
    description: Production server
paths:
  /news:
    get:
      operationId: getChat
      summary: Get a chat response based on a query parameter.
      security:
        - ApiKeyAuth: []
      parameters:
        - in: query
          name: query
          required: true
          schema:
            type: string
          description: The chat query string.
      responses:
        '200':
          description: Successfully received chat response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatResponse'
              example:
                message: This is a sample chat response.
                data:
                  key1: value1
                  key2: value2
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '500':
          $ref: '#/components/responses/InternalServerError'
components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
  schemas:
    ChatRequest:
      type: object
      required:
        - query
      properties:
        query:
          type: string
    ChatResponse:
      type: object
      properties:
        message:
          type: string
        data:
          type: object
          additionalProperties: true
  responses:
    BadRequestError:
      description: Bad Request
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
          example:
            message: Invalid request parameters.
    UnauthorizedError:
      description: Unauthorized
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
          example:
            message: Invalid API Key.
    InternalServerError:
      description: Internal Server Error
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
          example:
            message: An unexpected error occurred.
```

##### Privacy policy

https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/80/privacy

### Additional Settings

🔲 Use conversation data in your GPT to improve our models
