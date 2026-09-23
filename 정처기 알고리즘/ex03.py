# 모래시계 모양 최대 값 출력

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
for x in range(6):
    for y in range(6):
        value = 0
        for i in range(7):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < 6 and 0 <= newY < 6:
                value += arr[newX][newY]
            if max < value:
                max = value
print(max)
