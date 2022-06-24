from typing import List


def prefix_sum(n: int, m: int, matrix: List[List[int]], section: List[List[int]]) -> List[int]:
    d = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i][j - 1] + d[i - 1][j] - d[i - 1][j - 1] + matrix[i - 1][
                j - 1]  # d[i - 1][j - 1]의 값이 두번 더해졌으므로 그 값만큼 1회 빼고, 현재 idx의 matrix 내 숫자 값을 더한다.

    answer = []
    for coordinates in section:
        x1, y1, x2, y2 = coordinates
        answer.append(
            d[x2][y2] - d[x2][y1 - 1] - d[x1 - 1][y2] + d[x1 - 1][y1 - 1])  # 위 d 배열 초기화와 동일한 방법의 점화식으로 구할 수 있었다.
    return answer
