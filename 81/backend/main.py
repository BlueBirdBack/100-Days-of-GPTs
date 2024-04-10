from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
import uvicorn
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app_gemini = FastAPI()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-Key"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

api_key_header = APIKeyHeader(name=API_KEY_NAME)


def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key


@app_gemini.get("/gemini")
async def perfect(query: str, api_key: str = Depends(get_api_key)):
    genai.configure(api_key=GEMINI_API_KEY)
    # model = genai.GenerativeModel(
    #     "models/gemini-1.5-pro-latest",
    #     system_instruction="Perfect the given prompt for the highest clarity, brevity, and accuracy. Assign scores to both the initial and revised prompts on a scale of 0-100.",
    #     generation_config=genai.GenerationConfig(),
    # )

    # response = model.generate_content(query)

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    prompt = f"""Perfect the following prompt for the highest clarity, brevity, and accuracy. Assign scores to both the initial and revised prompts on a scale of 0-100.
<prompt>
{query}
</prompt>"""

    # print(prompt)
    response = model.generate_content(prompt)
    # print(type(response.text))
    print(response.text)
    return response.text


if __name__ == "__main__":
    uvicorn.run(app_gemini, host="0.0.0.0", port=4410)
