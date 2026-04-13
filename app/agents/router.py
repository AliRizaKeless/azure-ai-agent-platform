from openai import OpenAI

client = OpenAI()

def route_question(question: str) -> str:
    user_question = question.lower()

    if "weather" in user_question:
        return "This would call a weather API in a real system 🌤️"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content