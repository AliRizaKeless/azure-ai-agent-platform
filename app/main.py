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

@app.post("/ask")
def ask_ai(q: Question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": q.question}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }