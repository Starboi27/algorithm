import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")


def solve(short, long):
    result = 0
    for i in range(long - short + 1):
        total = 0
        for j in range(short):
            total += aj[j] * bj[i + j]

        result = max(result, total)

    return result


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        aj, bj = bj, aj

    result = solve(n, m)

    print(f"#{tc} {result}")

# 개 씨발 복습
