import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"
client = OpenAI(api_key=GROQ_API_KEY, base_url=BASE_URL)
MODEL = "llama3-70b-8192"
TEMPERATURE = 0.1

app_groq = FastAPI()

conversations = {}


class ChatMessage(BaseModel):
    message: str
    chat_id: str


@app_groq.post("/groq")
async def chat(chat_message: ChatMessage):
    response_message = generate_response(chat_message.message, chat_message.chat_id)
    print(conversations)
    return {"response": response_message}


@app_groq.get("/history")
async def get_history(chat_id: str = Query(...)):
    if chat_id in conversations:
        return {"history": conversations[chat_id]}
    else:
        return {"history": []}


def get_completion(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model=MODEL,
        temperature=TEMPERATURE,
    )
    return response.choices[0].message.content


def process_prompt(prompt):
    # Step 1: Extract the core question
    core_question = get_completion(
        f"{prompt}\n"
        f"Please extract core question, only extract the most "
        f"comprehensive and detailed one!"
    )

    # Step 2: Extract problem-solving information
    problem_solving_info = get_completion(
        f"{prompt}\n"
        f"Note: Please extract the problem-solving information related to "
        f"the core question ({core_question}), Only extract the most useful "
        f"information, list them one by one!"
    )

    # Step 3: Generate and extract the answer
    answer = get_completion(
        f"{prompt}\n"
        f"Hint: {problem_solving_info}\n"
        f"{core_question}\n"
        f"Please understand the Hint and question information, then solve the "
        f"problem step by step and show the answer."
    )

    return core_question, problem_solving_info, answer


def generate_response(message, chat_id):
    if chat_id not in conversations:
        conversations[chat_id] = []

    conversations[chat_id].append({"role": "user", "content": message})

    core_question, problem_solving_info, answer = process_prompt(message)

    conversations[chat_id].append({"role": "assistant", "content": answer})

    return answer


if __name__ == "__main__":
    uvicorn.run(app_groq, host="0.0.0.0", port=4424)
