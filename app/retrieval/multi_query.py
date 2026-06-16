from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="mistral"
)

def generate_queries(query: str):

    prompt = f"""
Generate 3 alternative search queries.

Original Query:
{query}

Return only the rewritten queries.
One per line.
"""

    response = llm.invoke(prompt)

    queries = [
        q.strip()
        for q in response.content.split("\n")
        if q.strip()
    ]

    return [query] + queries[:3]