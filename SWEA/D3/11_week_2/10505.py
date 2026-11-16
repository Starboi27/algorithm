import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    avg = 0
    cnt = 0

    for i in arr:
        avg += i
    result = avg // n

    for i in arr:
        if result >= i:
            cnt += 1

    print(f"#{tc} {cnt}")


# 코드 최적화 복습
