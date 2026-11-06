import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))

    for tm in range(m):
        idx, value = map(int, input().split())
        arr.insert(idx, value)

    print(f"#{tc} {arr[l]}")

# insert(idx, value) 함수로 풀 수 있음
