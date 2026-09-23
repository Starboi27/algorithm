# 행우선 탐색

import random

arr = []

for i in range(3):
    arr.append([random.randint(1, 100) for _ in range(3)])


sum_arr = [0] * 3

for i in range(3):
    sum_arr[i] = 0
    for j in range(3):
        sum_arr[i] += arr[i][j]

print(arr)
print(sum_arr)
