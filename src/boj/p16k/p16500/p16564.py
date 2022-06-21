from typing import List


def hios_progamer(n: int, team: List[int], point: int) -> int:
    low, high = min(team), max(team) + point
    answer = low
    team.sort()

    while low <= high:
        pivot = (low + high) // 2
        temp_point = 0
        for member in team:
            if pivot <= member:
                break
            temp_point += pivot - member
        if temp_point <= point:
            answer = pivot
            low = pivot + 1
        else:
            high = pivot - 1
    print(answer)
