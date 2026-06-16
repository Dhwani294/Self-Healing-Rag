import uuid
from .hashing import compute_hash
from .metadata_store import (
    load_registry,
    save_registry
)
from qdrant_client import (
    QdrantClient
)

client = QdrantClient(
    url="http://localhost:6333"
)

from qdrant_client.models import (
    Distance,
    VectorParams
)

def create_collection():

    collections = [
        c.name
        for c
        in client.get_collections().collections
    ]

    if "documents" not in collections:

        client.create_collection(
            collection_name="documents",
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )
from qdrant_client.models import (
    PointStruct
)
def upsert_chunks(
        chunks,
        embeddings,
        source
):

    points = []

    for chunk, embedding in zip(
        chunks,
        embeddings
    ):

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding.tolist(),
                payload={
                    "text": chunk["text"],
                    "parent_id": chunk["parent_id"],
                    "child_id": chunk["child_id"],
                    "source": source
                }
            )
        )

    client.upsert(
        collection_name="documents",
        points=points
    )        
def should_index(
        source,
        text
):

    registry = load_registry()

    hash_value = compute_hash(text)

    if source in registry:

        if registry[source]["hash"] == hash_value:

            print(
                f"Skipping {source}"
            )

            return False

    registry[source] = {
        "hash": hash_value
    }

    save_registry(registry)

    return True
    