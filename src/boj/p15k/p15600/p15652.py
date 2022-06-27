from typing import List


def n_and_m(n: int, m: int) -> None:
    def search(c: int, n: int, m: int, prev: List[int]) -> None:
        if c == m:
            print(' '.join(list(map(str, prev))))
            return

        for i in range(1, n + 1):

            if not prev:
                search(c + 1, n, m, prev + [i])
            elif prev[-1] <= i:
                search(c + 1, n, m, prev + [i])

    search(0, n, m, [])
