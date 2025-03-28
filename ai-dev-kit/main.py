import httpx
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to AI DEV Kit API 🎯"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/chat")
async def chat(input: ChatInput):
    payload = {
        "model": "gpt-3.5-turbo",  # or use the model you're running in LM Studio
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input.message}
        ],
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://host.docker.internal:1234/v1/chat/completions",
            json=payload,
            timeout=30
        )

    result = response.json()
    return {
        "input": input.message,
        "response": result["choices"][0]["message"]["content"]
    }
