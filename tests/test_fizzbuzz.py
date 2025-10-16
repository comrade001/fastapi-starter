import pytest
from hello_python.fizzbuzz import fizzbuzz, fizzbuzz_sequence


@pytest.fixture
def fb():
    return fizzbuzz


def test_with_fixture(fb):
    assert fb(9) == "Fizz"


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (4, "4"),
        (5, "Buzz"),
        (6, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (16, "16"),
        (30, "FizzBuzz"),
    ],
)
def test_fizzbuzz_unit(n: int, expected: str) -> None:
    assert fizzbuzz(n) == expected


@pytest.mark.parametrize("bad", [1.0, "3", None, 3 + 0j])
def test_fizzbuzz_type_errors(bad) -> None:
    with pytest.raises(TypeError):
        fizzbuzz(bad)


def test_fizzbuzz_sequence_len() -> None:
    seq = fizzbuzz_sequence(20)
    assert len(seq) == 20


def test_fizzbuzz_sequence_values() -> None:
    seq = fizzbuzz_sequence(16)
    assert seq[:6] == ["1", "2", "Fizz", "4", "Buzz", "Fizz"]
    assert seq[14] == "FizzBuzz"  # 15
