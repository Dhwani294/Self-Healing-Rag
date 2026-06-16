import json
from pathlib import Path

META_FILE = Path("data/index_metadata.json")

def load_registry():

    if META_FILE.exists():
        return json.loads(META_FILE.read_text())

    return {}

def save_registry(registry):

    META_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    META_FILE.write_text(
        json.dumps(registry, indent=2)
    )