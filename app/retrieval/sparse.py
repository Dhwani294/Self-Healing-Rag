from rank_bm25 import BM25Okapi
from qdrant_client import QdrantClient

client = QdrantClient(
    url="http://localhost:6333"
)

bm25 = None
documents = []


def load_documents_from_qdrant():

    global bm25
    global documents

    records, _ = client.scroll(
        collection_name="documents",
        limit=1000,
        with_payload=True
    )

    documents = []

    for record in records:

        payload = record.payload

        documents.append(
            {
                "text": payload.get("text", ""),
                "source": payload.get("source", "")
            }
        )

    tokenized_docs = [
        doc["text"].split()
        for doc in documents
    ]

    bm25 = BM25Okapi(
        tokenized_docs
    )


def sparse_search(
        query,
        top_k=10
):

    global bm25

    if bm25 is None:
        load_documents_from_qdrant()

    tokens = query.split()

    scores = bm25.get_scores(
        tokens
    )

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]