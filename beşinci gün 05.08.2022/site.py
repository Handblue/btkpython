from fastapi import FastAPI

app = FastAPI()

app.get("/0")
def root():
    return "hello world"

#uvicorn --port 900 -reload