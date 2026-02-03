import json
from pathlib import Path
DATA_FILE = Path("data/books.json")


def load_books():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []

def save_books(books):
    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(books, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )