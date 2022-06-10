def minecraft(info: str, row1: str, row2: str, row3: str) -> None:
    N, M, B = map(int, info.split())
    field = list(map(int, row1.split())) + list(map(int, row2.split())) + list(map(int, row3.split()))
    
    up_required_amount = 0
    down_required_amount = 0
    
    min_value, max_value = min(field), max(field)
    
    up_left_block = B
    down_left_block = B
    up_time = 0
    down_time = 0
    compare = []
    
    if B == 0:
        idx = 0
        while idx < len(field):
            amount = field[idx] - min_value
            down_left_block += amount
            down_time += amount * 2
            idx += 1
        print(down_time, min_value)
        return

    idx = 0
    # 범위를 벗어나지 않고 남은 블럭이 있을 경우 계속한다
    while up_left_block > 0 and idx < len(field):
        # 최댓값에서 현재 위치 값의 차이를 계산하고, 시간을 계산하여 넣는다.
        amount = max_value - field[idx]
        up_left_block += amount
        up_time += amount
        idx += 1
    compare.append((up_time, max_value))
    
    idx = 0
    while down_left_block > 0 and idx < len(field):
        amount = field[idx] - min_value
        down_left_block += amount
        down_time += amount * 2
        idx += 1
        
    compare.append((down_time, min_value))

    print(*min(compare, key= lambda x: (x[0], x[1])))
