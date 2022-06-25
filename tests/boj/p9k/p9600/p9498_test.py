from src.boj.p9k.p9400.p9498 import exam_score
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, str]] = [
    ("100", "A"),
    ("0", "F"),
    ("89", "B")
]


@pytest.mark.parametrize("user, expected", cases)
def test_exam_score(user: str, expected: str, capsys):  # noqa
    exam_score(user)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
