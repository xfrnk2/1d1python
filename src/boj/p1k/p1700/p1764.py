from typing import List


def the_dbj(_d: List[str], _b: List[str]) -> None:
    d = set(_d)
    b = set(_b)
    res = []

    for person in d:
        if person in b:
            res.append(person)

    print(*sorted(res))
