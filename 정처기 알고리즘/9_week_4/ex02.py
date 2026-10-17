import random

arr = [[random.randint(1, 3) for i in range(3)] for j in range(3)]

sum_arr = [0] * 3

for i in range(3):
    for j in range(3):
        sum_arr[i] += arr[j][i]

mean_arr = [0] * 3

for k in range(3):
    mean_arr[k] = sum_arr[k] / 3

print(*[f"{mean_arr[i]:.2f}" for i in range(3)])
