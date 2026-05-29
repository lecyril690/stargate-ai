from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

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

@app.post("/chat")
def chat(msg: Message):

    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f'''
Tu es une IA Stargate futuriste.
Réponds comme une entité intelligente.

Utilisateur:
{msg.text}
''',
            "stream": False
        }
    )

    data = response.json()

    return {
        "reply": data["response"]
    }