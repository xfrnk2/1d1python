from itertools import permutations
from typing import List


def same_number_multiple(N: int, data: List[str]) -> None:

    for i in range(1, N + 1):
        origin_num = data[i - 1]
        ans = "impossible"
        for n in list(permutations(origin_num)):
            current = int(''.join(n))
            int_origin_num = int(origin_num)
            if current > int_origin_num and current % int_origin_num == 0:
                ans = "possible"
                break
        print(f"#{i} {ans}")
