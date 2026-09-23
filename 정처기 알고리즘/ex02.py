# 열우선 탐색

import random

arr = [[random.randint(1, 100) for i in range(3)] for _ in range(3)]

print(arr)

mean_arr = [0] * 3

for i in range(3):
    for j in range(3):
        mean_arr[i] += arr[j][i]
    mean_arr[i] /= 3

print([f"{mean_arr[i]:.2f}" for i in range(3)])
