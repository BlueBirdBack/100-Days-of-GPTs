from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from anthropic import Anthropic

import os
from dotenv import load_dotenv

load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

client = Anthropic(api_key=CLAUDE_API_KEY)

app_claude = FastAPI()

class Message(BaseModel):
    role: str
    content: str

DEFAULT_MODEL = "claude-3-haiku-20240307"
DEFAULT_MAX_TOKENS = 2048

class ChatRequest(BaseModel):
    messages: list[Message]

@app_claude.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = client.messages.create(
            model=DEFAULT_MODEL,
            max_tokens=DEFAULT_MAX_TOKENS,
            messages=[{"role": m.role, "content": m.content} for m in request.messages],
        )
        
        print(response)
        # Message(id='msg_01W1YU43VQNXVLn5NVJLXmkR', content=[ContentBlock(text='Hello! How can I assist you today?', type='text')], model='claude-3-haiku-20240307', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=9, output_tokens=12))

        # Extract the assistant's message from the response
        assistant_message = Message(role=response.role, content=response.content[0].text)

        # Add the assistant's message to the messages list
        request.messages.append(assistant_message)
        print(request.messages)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app_claude, host="0.0.0.0", port=4320)