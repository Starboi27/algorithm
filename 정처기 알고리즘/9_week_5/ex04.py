arr = [5, 1, 7, 18, 2]

for i in range(len(arr), 0, -1):
    for j in range(i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

# 버블소트
