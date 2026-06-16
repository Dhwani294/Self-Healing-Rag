from tavily import TavilyClient

from app.core.config import (
    TAVILY_API_KEY
)

client = TavilyClient(
    api_key=TAVILY_API_KEY
)

#Function

def web_search(
        query,
        max_results=5
):
    response = client.search(
        query=query,
        max_results=max_results
    )

#Return:

    return response["results"]

def build_web_context(
        results
):
    contexts = []

#Loop:

    for item in results:
        content = item.get(
            "content",
            ""
        )
        contexts.append(
            content
        )

#Return:

    return contexts
