import uuid
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from app.agents.router import route_question
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Azure AI Agent Platform",
    version="1.0.0"
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    request_id = str(uuid.uuid4())
    result = route_question(q.question)

    logger.info(f"Agent used: {result['agent']}")
    logger.info(f"Generated answer: {result['answer']}")

    result["request_id"] = request_id
    return result
