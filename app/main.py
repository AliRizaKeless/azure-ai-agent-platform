import time
import uuid
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from datetime import datetime
from app.agents.router import route_question
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

APP_NAME = "Azure AI Agent Platform"

app = FastAPI(
    title="Azure AI Agent Platform",
    version="1.0.0"
)

START_TIME = time.time()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": f"{APP_NAME} is running 🚀",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "azure-ai-agent-platform"
    }

@app.get("/uptime")
def uptime():
    uptime_seconds = int(time.time() - START_TIME)
    return {"uptime_seconds": uptime_seconds}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.get("/docs-info")
def docs_info():
    return {
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

@app.post("/ask")
def ask_ai(q: Question):
    logger.info(f"Received question: {q.question}")

    request_id = str(uuid.uuid4())
    result = route_question(q.question)

    logger.info(f"Agent used: {result['agent']}")
    logger.info(f"Generated answer: {result['answer']}")

    result["request_id"] = request_id
    return result
