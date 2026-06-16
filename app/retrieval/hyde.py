from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="mistral"
)

def generate_hypothetical_document(
    query: str
):

    prompt = f"""
Write a detailed answer to:

{query}

The answer is only used for retrieval.
"""

    response = llm.invoke(prompt)

    return response.content