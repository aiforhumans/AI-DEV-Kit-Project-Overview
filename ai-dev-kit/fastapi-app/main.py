import httpx
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(input: ChatInput):
    payload = {
        "model": "gpt-3.5-turbo",  # replace with your actual model
        "messages": [
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": input.message}
        ],
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://host.docker.internal:1234/v1/chat/completions",  # <-- bridge to Windows
            json=payload,
            timeout=30
        )

    result = response.json()
    return {
        "input": input.message,
        "response": result["choices"][0]["message"]["content"]
    }
