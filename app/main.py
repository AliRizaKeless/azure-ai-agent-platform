from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from app.agents.router import route_question

app = FastAPI()

client = OpenAI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask_ai(q: Question):
    return {
        "answer": route_question(q.question)
    }