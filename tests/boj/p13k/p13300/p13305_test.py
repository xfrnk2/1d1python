from src.boj.p13k.p13300.p13305 import gas_station
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, int]] = [
("4", "2 3 1", "5 2 4 1", 18),
("4", "3 3 4", "1 1 1 1", 10)
]


@pytest.mark.parametrize("n, distances, stations, expected", cases)
def test_gas_station(n: str, distances: str, stations: str, expected: int, capsys):  # noqa
    gas_station(n, distances, stations)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
