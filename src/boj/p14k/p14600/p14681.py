def choose_quadrant(input_value_x: str, input_value_y: str) -> None:
    x, y = int(input_value_x), int(input_value_y)
    if x < 0 and y < 0:
        print(3)
        return
    if x < 0 and y > 0:
        print(2)
        return
    if x > 0 and y < 0:
        print(4)
        return
    print(1)
