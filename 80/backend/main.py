from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from openai import OpenAI
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app_news = FastAPI()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-Key"
PPLX_API_KEY = os.getenv("PPLX_API_KEY")

api_key_header = APIKeyHeader(name=API_KEY_NAME)


def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key


@app_news.get("/news")
async def chat(query: str, api_key: str = Depends(get_api_key)):
    client = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

    # Convert the query string to the required format
    messages = [
        {
            "role": "user",
            "content": query,
        },
    ]

    response = client.chat.completions.create(
        model="sonar-medium-online",
        messages=messages,
    )

    return response


if __name__ == "__main__":
    uvicorn.run(app_news, host="0.0.0.0", port=4409)