def choose_quadrant(input_value_x: str, input_value_y: str) -> None:
    x, y = int(input_value_x), int(input_value_y)
    answer = 1
    if x < 0 and y < 0:
        answer = 3
    elif x < 0 and y > 0:
        answer = 2
    elif x > 0 and y < 0:
        answer = 4
    print(answer)
