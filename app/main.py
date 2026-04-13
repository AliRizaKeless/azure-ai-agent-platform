from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

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
    user_question = q.question.lower()

    # simple agent logic
    if "weather" in user_question:
        return {
            "answer": "This would call a weather API in a real system 🌤️"
        }

    # default: use AI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": q.question}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }