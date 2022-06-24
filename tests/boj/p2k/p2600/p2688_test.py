# from typing import Sequence, Tuple
# import pytest
#
# from src.boj.p2k.p2600.p2688 import no_decretion
#
# cases: Sequence[Tuple[int, int]] = [
#     (2, 55),
#     (3, 220),
#     (4, 715)
# ]
#
#
# @pytest.mark.parametrize("n, expected", cases)
# def test_no_decretion(n: int, expected: int, capsys):  # noqa
#     no_decretion(n)
#     captured = capsys.readouterr()
#     assert captured.out == f'{expected}\n'
