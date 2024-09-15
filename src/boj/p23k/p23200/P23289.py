import sys

input = sys.stdin.readline


def init_wall():
    ret = set()
    for i in range(W):
        x, y, t = list(map(int, input().split()))
        if t == 0:
            ret.add(((x, y), (x - 1, y)))
            ret.add(((x - 1, y), (x, y)))
        else:
            ret.add(((x, y), (x, y + 1)))
            ret.add(((x, y + 1), (x, y)))
    return ret


def is_out(a, b):
    return R < a or C < b or a < 1 or b < 1


def is_all_field_block_upper_k(_field, _target):
    for _t in _target:
        a, b = _t
        if _field[a][b] < K:
            return False
    return True


def adjust(_field):
    weights = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C):
            a = _field[i][j]
            b = _field[i][j + 1]
            diff = abs(a - b) // 4
            if diff == 0 or ((i, j + 1), (i, j)) in wall or a == b:
                continue

            if a < b:
                weights[i][j] += diff
                weights[i][j + 1] -= diff
            else:
                weights[i][j] -= diff
                weights[i][j + 1] += diff

    for j in range(1, C + 1):
        for i in range(1, R):
            a = _field[i][j]
            b = _field[i + 1][j]
            diff = abs(a - b) // 4
            if diff == 0 or ((i + 1, j), (i, j)) in wall or a == b:
                continue

            if a < b:
                weights[i][j] += diff
                weights[i + 1][j] -= diff
            else:
                weights[i][j] -= diff
                weights[i + 1][j] += diff

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            _field[i][j] += weights[i][j]


def cool_sides(_field):
    for i in range(1, R + 1):
        if _field[i][1] > 0:
            _field[i][1] -= 1
        if _field[i][C] > 0:
            _field[i][C] -= 1

    for i in range(2, C):
        if _field[1][i] > 0:
            _field[1][i] -= 1
        if _field[R][i] > 0:
            _field[R][i] -= 1


class Fan:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def blow_along_d(self, a, b, temperature, _field, _visit):
        if temperature == 0 or is_out(a, b) or _visit[a][b]:
            return
        _visit[a][b] = True
        _field[a][b] += temperature

        if not ((a, b), (a + self.d[0], b + self.d[1])) in wall:
            self.blow_along_d(a + self.d[0], b + self.d[1], temperature - 1, _field, _visit)

        if self.d[0] == 0:
            if not ((a, b), (a - 1, b)) in wall and not ((a - 1, b), (a - 1, b + self.d[1])) in wall:
                self.blow_along_d(a + self.d[0] - 1, b + self.d[1], temperature - 1, _field, _visit)

            if not ((a, b), (a + 1, b)) in wall and not ((a + 1, b), (a + 1, b + self.d[1])) in wall:
                self.blow_along_d(a + self.d[0] + 1, b + self.d[1], temperature - 1, _field, _visit)

        else:
            if not ((a, b), (a, b - 1)) in wall and not ((a, b - 1), (a + self.d[0], b - 1)) in wall:
                self.blow_along_d(a + self.d[0], b + self.d[1] - 1, temperature - 1, _field, _visit)

            if not ((a, b), (a, b + 1)) in wall and not ((a, b + 1), (a + self.d[0], b + 1)) in wall:
                self.blow_along_d(a + self.d[0], b + self.d[1] + 1, temperature - 1, _field, _visit)


def run():
    chocolate_count = 0
    while 100 >= chocolate_count:
        for f in fan_list:
            nx, ny = f.x + f.d[0], f.y + f.d[1]
            visit = [[False for _ in range(C + 1)] for _ in range(R + 1)]
            f.blow_along_d(nx, ny, 5, field, visit)
        adjust(field)
        cool_sides(field)
        chocolate_count += 1
        if is_all_field_block_upper_k(field, target):
            break
    return chocolate_count


if __name__ == "__main__":
    R, C, K = map(int, input().split())
    field = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
    target = []
    fan_list = []
    input_field = [[0 for _ in range(C + 1)]]

    for i in range(1, R + 1):
        input_field.append([0] + list(map(int, input().split())))

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if input_field[i][j] == 5:
                target.append((i, j))
            elif input_field[i][j] == 0:
                continue
            else:
                obj = Fan(i, j, direction[input_field[i][j]])
                fan_list.append(obj)

    W = int(input())
    wall = init_wall()
    answer = run()
    print(answer)
