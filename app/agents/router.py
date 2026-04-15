from openai import OpenAI
from app.agents.weather_agent import get_weather_answer

client = OpenAI()


def load_knowledge():
    with open("app/data/knowledge.txt", "r", encoding="utf-8") as f:
        return f.read()


def retrieve_relevant_knowledge(question: str, knowledge: str) -> dict:
    question_lower = question.lower()

    sections = knowledge.split("\n\n")
    for section in sections:
        if "azure" in question_lower and "[Azure]" in section:
            return {"source": "Azure", "content": section}
        if "fastapi" in question_lower and "[FastAPI]" in section:
            return {"source": "FastAPI", "content": section}
        if "docker" in question_lower and "[Docker]" in section:
            return {"source": "Docker", "content": section}

    return {"source": "None", "content": "No specific knowledge found."}


knowledge_base = load_knowledge()


def route_question(question: str) -> dict:
    user_question = question.lower()

    if "weather" in user_question:
        return {
            "agent": "weather",
            "source": "weather_agent",
            "answer": get_weather_answer()
    }

    relevant_knowledge = retrieve_relevant_knowledge(question, knowledge_base)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"Use the following knowledge when answering:\n{relevant_knowledge['content']}"
                },
                {"role": "user", "content": question}
            ]
        )

        return {
           "agent": "ai",
           "source": relevant_knowledge["source"],
           "answer": response.choices[0].message.content
        }

    except Exception as e:
        return {
            "agent": "system",
            "source": "error_handler",
            "answer": f"An error occurred while processing the request: {str(e)}"
    }