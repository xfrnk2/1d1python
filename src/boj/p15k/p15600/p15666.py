from typing import List


def n_and_m(_: int, m: int, _array: List[int]) -> None:
    array = sorted(set(_array))

    def search(c: int, prev: List[int]) -> None:
        nonlocal m, array
        if c == m:
            print(*prev)
            return

        for i in array:

            if not prev or prev[-1] <= i:
                search(c + 1, prev + [i])

    search(0, [])
