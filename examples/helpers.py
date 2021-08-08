import json
import pathlib
from typing import Any, Dict, Iterator

# path
ROOT = pathlib.Path("./").resolve().parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"

meta_path = RAW / "metadata.jsonl"
texts_path = RAW / "texts.jsonl"

# typing classes
Publication = Dict[str, Any]


def read_jsonl(p: pathlib.PosixPath) -> Iterator[Publication]:
    """Yield .jsonl file's contents line by line."""
    with open(p) as lines:
        for line in lines:
            yield json.loads(line)
