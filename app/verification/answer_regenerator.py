from langchain_ollama import (
    ChatOllama
)

from app.core.config import (
    OLLAMA_MODEL
)

llm = ChatOllama(
    model=OLLAMA_MODEL
)



def regenerate_answer(
        query,
        contexts
):



    context_text = "\n\n".join(
        contexts
    )

    prompt = f"""
Generate an answer using ONLY
the provided context.

Do not use prior knowledge.

Question:
{query}

Context:
{context_text}
"""



    response = llm.invoke(
        prompt
    )

    return response.content