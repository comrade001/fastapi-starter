from __future__ import annotations

from collections import Counter
from typing import Dict


def word_frequency(text: str) -> Dict[str, int]:
    """Return a dict with word counts from given text."""
    words = (
        text.lower()
        .replace(",", " ")
        .replace(".", " ")
        .replace(";", " ")
        .replace(":", " ")
        .replace("!", " ")
        .split()
    )
    return dict(Counter(words))
