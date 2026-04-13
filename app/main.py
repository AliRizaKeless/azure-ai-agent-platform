from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from app.agents.router import route_question
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    logger.info(f"Received question: {q.question}")

    answer = route_question(q.question)

    logger.info(f"Generated answer: {answer}")

    return {
        "answer": answer
    }

