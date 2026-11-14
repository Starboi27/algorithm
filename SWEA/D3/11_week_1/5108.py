import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(m):
        s, g = map(int, input().split())
        arr.append(g)  # append로 out-of-range 에방하고 길이를 늘린다

        for j in range(len(arr) - 1, s - 1, -1):
            arr[j] = arr[j - 1]

        arr[s] = g

    print(f"#{tc} {arr[l]}")
