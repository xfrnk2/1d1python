import math


def turret(input_values) -> None:
    x1, y1, r1, x2, y2, r2 = list(map(int, input_values.split()))
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # 동심원이고 반지름이 같다.
    if distance == 0 and r1 == r2:
        print(-1)
        return
    # 두 원이 교차하여 서로 다른 두 점에서 만나는 경우
    if abs(r1 - r2) < distance < abs(r1 + r2):
        print(2)
        return
    # 두 원이 외접 또는 내접하는 경우
    if distance == r1 + r2 or abs(r1 - r2) == distance:
        print(1)
        return
    print(0)
