from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run("main:app", 
                host="0.0.0.0", 
                port=443, 
                ssl_keyfile="/root/projects/chatgpt4all.top.key", 
                ssl_certfile="/root/projects/chatgpt4all.top.pem")
