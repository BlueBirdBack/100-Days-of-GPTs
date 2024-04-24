from fastapi import FastAPI
import uvicorn

app_hello = FastAPI()


@app_hello.get("/")
def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run("main:app_hello", host="0.0.0.0", port=4318)
