import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    # 입력
    n, m = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    # 상태정의
    if n > m:
        m, n = n, m
        list_a, list_b = list_b, list_a

    result = 0
    for i in range(m - n + 1):
        total = 0
        for j in range(n):
            total += list_a[j] * list_b[i + j]
        result = max(total, result)

    # 출력
    print(f"#{tc} {result}")
