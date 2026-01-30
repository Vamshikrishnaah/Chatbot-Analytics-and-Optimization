import os
from typing import List, Dict
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize FastAPI app
app = FastAPI(title="Simple Chatbot API")

# CORS (open for assignment/demo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq client
client = Groq(api_key=GROQ_API_KEY)

# ----------- Models -----------

class UserInput(BaseModel):
    message: str
    conversation_id: str
    role: str = "user"

class Conversation:
    def __init__(self):
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": "You are a helpful AI assistant."}
        ]

conversations: Dict[str, Conversation] = {}

# ----------- Utility Functions -----------

def get_or_create_conversation(conversation_id: str) -> Conversation:
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation()
    return conversations[conversation_id]

def query_groq_api(conversation: Conversation) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation.messages,
            temperature=0.7,
            max_tokens=512
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------- Routes -----------

@app.get("/")
def root():
    return {"status": "Chatbot API is running successfully"}

@app.post("/chat/")
def chat(input: UserInput):
    conversation = get_or_create_conversation(input.conversation_id)

    conversation.messages.append({
        "role": input.role,
        "content": input.message
    })

    response = query_groq_api(conversation)

    conversation.messages.append({
        "role": "assistant",
        "content": response
    })

    return {
        "conversation_id": input.conversation_id,
        "response": response
    }

# ----------- Run Server -----------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
