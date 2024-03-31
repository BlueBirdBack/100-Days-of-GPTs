from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from os import getenv, path
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

app_gemyn = FastAPI()

conversations = {}

load_dotenv(find_dotenv())
API_KEY = getenv("GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-pro")


class ChatMessage(BaseModel):
    message: str
    chat_id: str


@app_gemyn.post("/gemyn")
async def chat(chat_message: ChatMessage):
    response_message = generate_response(chat_message.message, chat_message.chat_id)
    print(conversations)
    return {"response": response_message}


def generate_response(message, chat_id):
    if chat_id not in conversations:
        conversations[chat_id] = model.start_chat(history=[])

    chat = conversations[chat_id]
    response = chat.send_message(message)
    conversations[chat_id] = chat

    return response.text


if __name__ == "__main__":
    uvicorn.run(app_gemyn, host="0.0.0.0", port=4331)
