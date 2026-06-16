# scripts/test_qdrant.py

from qdrant_client import QdrantClient

client = QdrantClient(
    url="http://localhost:6333"
)

result = client.query_points(
    collection_name="documents",
    query=[0.1] * 384,
    limit=1
)

print(result)