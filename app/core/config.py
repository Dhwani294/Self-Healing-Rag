from dotenv import load_dotenv
import os

load_dotenv()

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "mistral"
)

QDRANT_URL = os.getenv(
    "QDRANT_URL",
    "http://localhost:6333"
)

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379"
)

TAVILY_API_KEY = os.getenv(
    "TAVILY_API_KEY"
)