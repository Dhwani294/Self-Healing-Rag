from langchain_ollama import (
    ChatOllama
)

from app.core.config import (
    OLLAMA_MODEL
)

llm = ChatOllama(
    model=OLLAMA_MODEL
)


def rewrite_query(
    query,
    failure_reason
):
    prompt = f"""
The query:

{query}

produced poor retrieval results.

Reason:

{failure_reason}

Generate 3 improved search queries.

Return one query per line.
"""

    response = llm.invoke(
        prompt
    )

    rewrites = [
        r.strip()
        for r in response.content.split("\n")
        if r.strip()
    ]

    return rewrites[:3]