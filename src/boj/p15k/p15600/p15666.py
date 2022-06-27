from typing import List


def n_and_m(n: int, m: int, array: List[int]) -> None:
    answer = set()

    def search(c: int, prev: List[int], n: int, m: int, arr: List[int]) -> None:
        nonlocal answer
        if c == m:
            answer.add(' '.join(list(map(str, prev))))
            return

        for i in arr:

            if not prev:
                search(c + 1, prev + [i], n, m, arr)
            elif prev[-1] <= i:
                search(c + 1, prev + [i], n, m, arr)

    search(0, [], n, m, sorted(array))
    for elem in sorted(answer):
        print(elem)
