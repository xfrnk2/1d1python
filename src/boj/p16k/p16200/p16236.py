from typing import List, Tuple


def check_is_movable(field: List[List[int]], x: int, y: int) -> boolean:
    return True


def get_eatable_fish(field: List[List[int]]):
    result: List[Tuple[int, int]]
    result = []
    
    for i in range(n):
            for j in range(n):
                if 2 < field[i][j]:
                    result.append((i, j))
    return result

def baby_shark(n: int, _field: List[List[int]]) -> int:
    field = []
    for f in _field:
        field.append(f)

    start = None
    size = 2
    move_count = 0

    for i in range(n):
        for j in range(n):
            if field[i][j] == 9:
                start = (i, j)
    print(start)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    is_continuable = True
    while is_continuable:
        eatable_fish = get_eatable_fish(field)
        if not eatable_fish:
            is_continuable = False
            break

        if len(eatable_fish) == 1:
            
        
