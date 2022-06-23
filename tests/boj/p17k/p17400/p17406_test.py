from src.boj.p17k.p17400.p17406 import array_rotation
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[int, int, int, List[List[int]], List[List[int]], int]] = [
(5, 6, 2, [[1, 2, 3, 2, 5, 6], [3, 8, 7, 2, 1, 3], [8, 2, 3, 1, 4, 5], [3, 4, 5, 1, 1, 1], [9, 3, 2, 1, 4, 3]], [[3, 4, 2], [4, 2, 1]], 12),

]


@pytest.mark.parametrize("n, m, k, array, rotation_info, expected", cases)
def test_array_rotation(n: int, m: int, k: int, array: List[List[int]], rotation_info: List[List[int]], expected: int, capsys):  # noqa
    array_rotation(n, m, k, array, rotation_info)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
