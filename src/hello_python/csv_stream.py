from __future__ import annotations
from typing import Iterator


def stream_csv(path: str) -> Iterator[list[str]]:
    """Generator that yields one row (list of strings) at a time."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip().split(",")
