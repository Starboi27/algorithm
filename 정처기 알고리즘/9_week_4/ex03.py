arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

dx = [-1, -1, -1, 0, 1, 1, 1]
dy = [-1, 0, 1, 0, -1, 0, 1]

max = 0

for x in range(1, 5):
    for y in range(1, 5):
        sum_arr = 0
        for i in range(7):
            # 새로운 좌표 설정
            new_X = x + dx[i]
            new_Y = y + dy[i]
            sum_arr += arr[new_X][new_Y]
        if max < sum_arr:
            max = sum_arr

print(max)
