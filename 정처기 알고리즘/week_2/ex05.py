# insersion 정렬
# key를 기준으로 앞(현재 인덱스)과 비교함
# key보다 앞 요소가 작다면 다음 인덱스로 넘어감
# 만약 크다면 앞 요소와 key의 자리를 교체함

arr = [3, 2, 1, 4]
# 1 [2, 3, 1, 4]

count = 0
# i = 1
for i in range(len(arr) - 1):
    count += 1
    print(count)
    key = arr[i + 1]  # key = 1
    j = i  # j = 0
    while j >= 0 and arr[j] > key:  # arr[0] = 2 > 1
        arr[j + 1] = arr[j]  # arr[1] = arr[0] = [2, 2, 3, 4]
        j -= 1  # j = -1
        print(arr)
    arr[j + 1] = key  # arr[0] = 1
    print(arr)  # arr = [1, 2, 3, 4]
