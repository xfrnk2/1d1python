import sys

def check_row(row):
    checked_row = [False] * N
    
    for i in range(N - 1):
        if map_data[row][i + 1] != map_data[row][i]:  # 비교 대상이 같지 않다면
            if map_data[row][i + 1] > map_data[row][i]:  # 비교 대상이 더 크면
                j = 0  # 현재 idx에서 1씩 감소
                while j < X:  # 경사로 최대길이만큼
                    if i - j < 0:  # idx 범위를 벗어나면 불가능
                        return False
                    if map_data[row][i + 1] - 1 != map_data[row][i - j]:
                        return False
                    if checked_row[i - j]:
                        return False
                    checked_row[i - j] = True
                    j += 1
            elif map_data[row][i + 1] < map_data[row][i]:  # 비교 대상이 더 작으면
                j = 1
                while j <= X:
                    if i + j >= N:  # idx 범위를 벗어나면 불가능
                        return False
                    if map_data[row][i + j] != map_data[row][i] - 1:
                        return False
                    if checked_row[i + j]:
                        return False
                    checked_row[i + j] = True
                    j += 1
                i += X - 1
    return True

def check_col(col):
    checked_col = [False] * N
    
    for i in range(N - 1):
        if map_data[i + 1][col] != map_data[i][col]:  # 비교 대상이 같지 않다면
            if map_data[i + 1][col] > map_data[i][col]:  # 비교 대상이 더 크면
                j = 0  # 현재 idx에서 1씩 감소
                while j < X:  # 경사로 최대길이만큼
                    if i - j < 0:  # idx 범위를 벗어나면 불가능
                        return False
                    if map_data[i + 1][col] - 1 != map_data[i - j][col]:
                        return False
                    if checked_col[i - j]:
                        return False
                    checked_col[i - j] = True
                    j += 1
            elif map_data[i + 1][col] < map_data[i][col]:  # 비교 대상이 더 작으면
                j = 1
                while j <= X:
                    if i + j >= N:  # idx 범위를 벗어나면 불가능
                        return False
                    if map_data[i + j][col] != map_data[i][col] - 1:
                        return False
                    if checked_col[i + j]:
                        return False
                    checked_col[i + j] = True
                    j += 1
                i += X - 1
    return True


input = sys.stdin.read()
data = input.split()
N = int(data[0])
X = int(data[1])
map_data = []

index = 2
for i in range(N):
    map_data.append(list(map(int, data[index:index + N])))
    index += N

ans = 0
for i in range(N):
    if check_col(i):
        ans += 1
    if check_row(i):
        ans += 1

print(ans)
