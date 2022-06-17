def the_little_prince(start_point: str, end_point: str, planets: str) -> None:
    x1, y1 = map(int, start_point.split(" "))
    x2, y2 = map(int, end_point.split(" "))
    splitted_planets = list(planets.split(","))
    planet_list = []  # 행성의 좌표와 반지름을 담고 있는 리스트
    for i in range(len(splitted_planets)):
        planet_list.append(list(map(int, splitted_planets[i].split(" "))))

    count = 0
    for i in range(len(planet_list)):
        cx, cy, cr = planet_list[i]
        # 행성의 중심 좌표와 출발점, 시작점 사이의 거리를 구한다.
        dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        pow_cr = cr ** 2

        # 두 거리가 모두 행성의 반지름보다 작으면 출발점과 시작점 둘다 행성 내부에 위치한다.
        if pow_cr > dis1 and pow_cr > dis2:
            pass
        elif pow_cr > dis1:
            count += 1
        elif pow_cr > dis2:
            count += 1

    print(count)
