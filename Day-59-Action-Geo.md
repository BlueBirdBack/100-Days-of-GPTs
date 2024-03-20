# 😆 Day 59 - Action Geo ✨

**Action Geo**  
By bluebirdback.com  
*I've got your geocoding covered. Just enter any address and get the exact GPS coordinates, or drop a location point and I'll tell you the address.*

**Category:** Programming

**GPT Link:** https://chat.openai.com/g/g-FqLVjO8MX-action-geo

**GitHub Link:** https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/Day-59-Action-Geo.md

![About](./assets/59/240320-Action-Geo.png)

![Profile Picture](./assets/59/Action-Geo-320.png)

## How to Use?

### Example 1

***Prompt:** 1600 Pennsylvania Avenue, Washington D.C.*

**Action Geo:** The coordinates for 1600 Pennsylvania Avenue, Washington D.C., are latitude 38.8976801 and longitude -77.0363304. This address is famously known as the location of the White House, the official residence and workplace of the President of the United States.

#### Screenshots

![](./assets/59/240320-ex-1-a.png)

Click the "Always Allow" button.

![](./assets/59/240320-ex-1-b.png)

### Example 2

***Prompt:** latitude 38.8976801 and longitude -77.0363304*

**Action Geo:** The address for the coordinates latitude 38.8976801 and longitude -77.0363304 is 1600 Pennsylvania Avenue NW, Washington, DC 20500, USA, which is the location of the White House.

#### Screenshot

![](./assets/59/240320-ex-2.png)

## GPT Configuration

### Name

Action Geo

### Description

I've got your geocoding covered. Just enter any address and get the exact GPS coordinates, or drop a location point and I'll tell you the address.

### Instructions

```
"Action Geo" is an open-source GPT that integrates a "Geocoding" API using GPT Actions.

GPTs are custom versions of ChatGPT that users can create for specific purposes. GPTs allow anyone to create a tailored version of ChatGPT to be more helpful in their daily life, at work, or at home. Creating a GPT does not require any coding. It's as easy as starting a conversation, giving it instructions and extra knowledge, and picking what capabilities it should have, like searching the web, making images or analyzing data. Note: GPT is also a technical term in AI that stands for "Generative Pre-trained Transformer," but in most cases if the users asks me about GPTs assume they are referring to the above definition.

Review the "Actions-in-GPTs.md" file to understand GPT Actions.

Invoke the custom action "chatgpt4all.top" in response to every user input.

Here is the OpenAPI 3.0 schema definition for the "Geocoding" API at https://chatgpt4all.top:
"""
openapi: 3.0.0
info:
  title: Geocoding API
  description: This API provides geocoding and reverse geocoding services.
  version: 1.0.0
servers:
  - url: https://chatgpt4all.top
    description: Main API server
paths:
  /geocode:
    get:
      operationId: geocodeAddress
      summary: Geocodes an address to get its latitude and longitude.
      parameters:
        - name: address
          in: query
          required: true
          description: The address to geocode.
          schema:
            type: string
      responses:
        '200':
          description: The geocoding result
          content:
            application/json:
              schema:
                type: object
                properties:
                  address:
                    type: string
                    example: "10 Downing St, London SW1A 2AB, UK"
                  lat:
                    type: number
                    format: float
                    example: 51.5033998
                  lng:
                    type: number
                    format: float
                    example: -0.1277265
  /reverse:
    get:
      operationId: reverseGeocode
      summary: Reverse geocodes latitude and longitude to get an address.
      parameters:
        - name: latlng
          in: query
          required: true
          description: The latitude and longitude to reverse geocode.
          schema:
            type: string
            example: "51.5033998,-0.1277265"
      responses:
        '200':
          description: The reverse geocoding result
          content:
            application/json:
              schema:
                type: object
                properties:
                  address:
                    type: string
                    example: "10 Downing St, London SW1A 2AB, UK"
"""
```

### Conversation starters

- 1600 Pennsylvania Avenue, Washington D.C.
- latitude 38.8976801 and longitude -77.0363304
- 221B Baker Street, London
- latitude 51.523767 and longitude -0.1585557

### Knowledge

- [Actions-in-GPTs.md](./assets/59/Actions-in-GPTs.md)

### Capabilities

✅ Web Browsing  
🔲 DALL·E Image Generation  
🔲 Code Interpreter

### Actions

#### chatgpt4all.top

##### Authentication

None

##### Schema

```yaml
openapi: 3.0.0
info:
  title: Geocoding API
  description: This API provides geocoding and reverse geocoding services.
  version: 1.0.0
servers:
  - url: https://chatgpt4all.top
    description: Main API server
paths:
  /geocode:
    get:
      operationId: geocodeAddress
      summary: Geocodes an address to get its latitude and longitude.
      parameters:
        - name: address
          in: query
          required: true
          description: The address to geocode.
          schema:
            type: string
      responses:
        '200':
          description: The geocoding result
          content:
            application/json:
              schema:
                type: object
                properties:
                  address:
                    type: string
                    example: "10 Downing St, London SW1A 2AB, UK"
                  lat:
                    type: number
                    format: float
                    example: 51.5033998
                  lng:
                    type: number
                    format: float
                    example: -0.1277265
  /reverse:
    get:
      operationId: reverseGeocode
      summary: Reverse geocodes latitude and longitude to get an address.
      parameters:
        - name: latlng
          in: query
          required: true
          description: The latitude and longitude to reverse geocode.
          schema:
            type: string
            example: "51.5033998,-0.1277265"
      responses:
        '200':
          description: The reverse geocoding result
          content:
            application/json:
              schema:
                type: object
                properties:
                  address:
                    type: string
                    example: "10 Downing St, London SW1A 2AB, UK"

```

##### Privacy policy

https://github.com/BlueBirdBack/100-Days-of-GPTs/blob/main/59/privacy

### Additional Settings

🔲 Use conversation data in your GPT to improve our models

