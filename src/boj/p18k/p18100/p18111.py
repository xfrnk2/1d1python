from typing import List


def minecraft(_info: str, _field: List[str]) -> None:
    N, M, B = map(int, _info.split())
    field = []
    for f in _field:
        field.extend(list(map(int, f.split())))
    times = []

    inclusive, exclusive = min(field), max(field) + 1
    for p in range(inclusive, exclusive):
        time: int = 0
        blocks: int = B
        for k in range(N * M):
            cur: int = field[k]
            if cur < p:
                time += p - cur
                blocks -= p - cur
            if cur > p:
                time += (cur - p) * 2
                blocks += cur - p
        if blocks >= 0:
            times.append((time, p))
    print(*min(times, key=lambda t: (t[0], -t[1])))
