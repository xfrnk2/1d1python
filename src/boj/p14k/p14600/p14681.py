def choose_quadrant(x: str, y: str) -> None:
    x, y = int(x), int(y)
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
