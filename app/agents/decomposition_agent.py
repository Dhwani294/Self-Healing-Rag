from langchain_ollama import ChatOllama
from app.core.config import OLLAMA_MODEL

llm = ChatOllama(
    model=OLLAMA_MODEL
)


def decompose_query(query: str):
    prompt = f"""
You are a query decomposition engine.

Break the user query into
independent retrieval questions.

Rules:
- Return one question per line
- Maximum 5 questions
- Preserve original meaning

Query:
{query}
"""

    response = llm.invoke(
        prompt
    )

    questions = [
        q.strip("- ").strip()
        for q in response.content.split("\n")
        if q.strip()
    ]

    if not questions:
        return [query]

    return questions