import xxhash

def compute_hash(text: str) -> str:
    return xxhash.xxh64(text).hexdigest()