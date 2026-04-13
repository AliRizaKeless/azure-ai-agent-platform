from openai import OpenAI
from app.agents.weather_agent import get_weather_answer

client = OpenAI()

def route_question(question: str) -> str:
    user_question = question.lower()

    if "weather" in user_question:
        return get_weather_answer()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content