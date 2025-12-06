from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "hello world", "env_value": os.getenv("MY_ENV_VAR", "not set")}
