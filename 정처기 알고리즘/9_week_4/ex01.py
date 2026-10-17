import random

arr = [[random.randint(1, 100) for i in range(3)] for j in range(3)]

sum_arr = [0] * 3

for i in range(3):
    for j in range(3):
        sum_arr[i] += arr[i][j]

print(sum_arr)
