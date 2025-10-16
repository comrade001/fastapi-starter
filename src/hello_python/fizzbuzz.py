from __future__ import annotations

from typing import List


def fizzbuzz(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    out = ""
    if n % 3 == 0:
        out += "Fizz"
    if n % 5 == 0:
        out += "Buzz"
    return out or str(n)


def fizzbuzz_sequence(n: int) -> List[str]:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be non-negative")
    return [fizzbuzz(i) for i in range(1, n + 1)]
