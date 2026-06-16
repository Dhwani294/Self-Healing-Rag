from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def embed_chunks(chunks):

    texts = [
        c["text"]
        for c in chunks
    ]

    vectors = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True
    )

    return vectors

