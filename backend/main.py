from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Backend is running 🚀"}

@app.post("/chat")
def chat(msg: Message):
    return {"reply": f"You said: {msg.text}"}