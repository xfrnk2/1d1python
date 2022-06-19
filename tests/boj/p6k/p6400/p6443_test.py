from typing import Sequence, Tuple, List
import pytest

from src.boj.p6k.p6400.p6443 import anagram

cases: Sequence[Tuple[str, List[str]]] = [
    ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
    ("acba", ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])
]


@pytest.mark.parametrize("string, expected", cases)
def test_anagram(string: str, expected: List[str], capsys):  # noqa
    result = anagram(string)
    assert result == expected
