from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from os import getenv, path
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

app_tokount = FastAPI()

load_dotenv(find_dotenv())
API_KEY = getenv("GEMINI_API_KEY")
model = genai.GenerativeModel("models/gemini-1.0-pro-latest")


class TokenCountRequest(BaseModel):
    text: str


@app_tokount.post("/tokount")
async def count_tokens(request: TokenCountRequest):
    token_count_response = model.count_tokens(request.text)
    token_count = token_count_response.total_tokens
    # print(request.text)
    # print(type(token_count))
    # print(token_count)
    return {"token_count": token_count}


if __name__ == "__main__":
    uvicorn.run(app_tokount, host="0.0.0.0", port=4401)
