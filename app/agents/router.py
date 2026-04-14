from openai import OpenAI
from app.agents.weather_agent import get_weather_answer

client = OpenAI()

def load_knowledge():
    with open("app/data/knowledge.txt", "r") as f:
        return f.read()

knowledge_base = load_knowledge()

def route_question(question: str) -> dict:
    user_question = question.lower()

    if "weather" in user_question:
        return {
            "agent": "weather",
            "answer": get_weather_answer()
        }

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
               {
                    "role": "system",
                    "content": f"Use the following knowledge when answering:\n{knowledge_base}"
               },
               {"role": "user", "content": question}
            ]
        )

        return {
            "agent": "ai",
            "answer": response.choices[0].message.content
        }

    except Exception as e:
        return {
            "agent": "system",
            "answer": f"An error occurred while processing the request: {str(e)}"
        }