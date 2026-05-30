from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.post("/chat")
def chat(msg: Message):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {
                    "role": "system",
                    "content": "Tu es Stargate, une IA futuriste intelligente et utile."
                },
                {
                    "role": "user",
                    "content": msg.text
                }
            ]
        },
        timeout=60
    )

    data = response.json()

    return {
        "reply": data["choices"][0]["message"]["content"]
    }