from openai import OpenAI
from app.agents.weather_agent import get_weather_answer

client = OpenAI()

def load_knowledge():
    with open("app/data/knowledge.txt", "r", encoding="utf-8") as f:
        return f.read()

def retrieve_relevant_knowledge(question: str, knowledge: str) -> dict:
    parsed_sections = parse_knowledge_sections(knowledge)

    best_match = None
    best_score = -1

    for section in parsed_sections:
        score = score_section(question, section["content"] + " " + section["source"])
        if score > best_score:
            best_score = score
            best_match = section

    if best_match:
        return best_match

    return {"source": "None", "content": "No specific knowledge found."}

knowledge_base = load_knowledge()

def parse_knowledge_sections(knowledge: str) -> list[dict]:
    sections = knowledge.split("\n\n")
    parsed_sections = []

    for section in sections:
        lines = section.strip().split("\n")
        if len(lines) >= 2:
            title = lines[0].replace("[", "").replace("]", "").strip()
            content = " ".join(lines[1:]).strip()
            parsed_sections.append({
                "source": title,
                "content": content
            })

    return parsed_sections

def score_section(question: str, content: str) -> int:
    question_words = set(question.lower().split())
    content_words = set(content.lower().split())
    return len(question_words.intersection(content_words))

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