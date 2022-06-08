import math


def hockey(_w: str, _h: str, _x: str, _y: str, _p: str, player1: str, player2: str, player3: str) -> None:
    W = int(_w)
    H = int(_h)
    X = int(_x)
    Y = int(_y)
    P = int(_p) # noqa

    player_coordinates = []
    player_coordinates.append(tuple(map(int, player1.split())))
    player_coordinates.append(tuple(map(int, player2.split())))
    player_coordinates.append(tuple(map(int, player3.split())))
    count = 0

    for player in player_coordinates:  # type: tuple
        x: int
        y: int
        x, y = player[0], player[1]
        is_in_square = X <= x <= X + W and Y <= y <= Y + H
        if is_in_square:
            count += 1
            continue

        left_circle_point_x = X
        left_circle_point_y = Y + H // 2

        right_circle_point_x = X + W
        right_circle_point_y = Y + H // 2

        left_circle_point_dis = math.sqrt((left_circle_point_x - x) ** 2 + (left_circle_point_y - y) ** 2)
        right_circle_point_dis = math.sqrt((right_circle_point_x - x) ** 2 + (right_circle_point_y - y) ** 2)

        is_in_left_circle = left_circle_point_dis <= H // 2
        is_in_right_circle = right_circle_point_dis <= H // 2

        if is_in_left_circle or is_in_right_circle:
            count += 1
    print(count)
