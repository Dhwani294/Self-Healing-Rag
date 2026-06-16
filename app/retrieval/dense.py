from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(
    url="http://localhost:6333"
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def dense_search(
        query,
        top_k=10
):

    vector = model.encode(
        query
    ).tolist()

    results = client.query_points(
        collection_name="documents",
        query=vector,
        limit=top_k
    ).points

    formatted = []

    for point in results:

        formatted.append(
            {
                "text": point.payload["text"],
                "source": point.payload.get(
                    "source",
                    ""
                ),
                "score": point.score
            }
        )

    return formatted