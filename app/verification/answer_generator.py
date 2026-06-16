from langchain_ollama import ChatOllama
from app.core.config import OLLAMA_MODEL

llm = ChatOllama(
    model=OLLAMA_MODEL
)
def generate_answer(
        query,
        contexts
):



    context_text = "\n\n".join(
        contexts
    )



    prompt = f"""
Answer the question using ONLY
the provided context.

Question:
{query}

Context:
{context_text}

Provide a concise answer.
"""



    response = llm.invoke(
        prompt
    )

    return response.content