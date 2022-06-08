from typing import List, Tuple


def melon_field(melon: int, distances: List[Tuple[int]]) -> None:
    bigger_width = 0
    bigger_height = 0
    bigger_width_idx = 0
    bigger_height_idx = 0
    for idx, item in enumerate(distances):


        direction, distance = item #type: ignore # noqa
        if direction == 1 or direction == 2:
            if bigger_width < distance:
                bigger_width = distance
                bigger_width_idx = idx
        elif direction == 3 or direction == 4:
            if bigger_height < distance:
                bigger_height = distance
                bigger_height_idx = idx


    smaller_width = abs((distances[(bigger_width_idx - 1) % 6][1] - distances[(bigger_width_idx + 1) % 6][1]))#type: ignore # noqa
    smaller_height = abs(distances[(bigger_height_idx - 1) % 6][1] - distances[(bigger_height_idx + 1) % 6][1])#type: ignore # noqa
    bigger_square = bigger_width * bigger_height
    smaller_square = smaller_width * smaller_height
    print(melon * (bigger_square - smaller_square))
