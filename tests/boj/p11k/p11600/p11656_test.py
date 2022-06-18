from src.boj.p11k.p11600.p11656 import prefix_array
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, str]] = [
    ("baekjoon", ["aekjoon", "baekjoon", "ekjoon", "joon", "kjoon", "n", "on", "oon"])
]

@pytest.mark.parametrize("string, expected", cases)
def test_prefix_array(string: str, expected: str, capsys):  # noqa
    assert expected == prefix_array(string)