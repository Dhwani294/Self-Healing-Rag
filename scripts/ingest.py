from app.ingestion.loader import load_txt
from app.ingestion.chunker import create_chunks
from app.ingestion.embedder import embed_chunks
from app.ingestion.indexer import (
    create_collection,
    upsert_chunks
)

text = load_txt(
    "docs/company_policy.txt"
)

chunks = create_chunks(text)

vectors = embed_chunks(chunks)

create_collection()

upsert_chunks(
    chunks,
    vectors,
    "company_policy.txt"
)

print("Done")